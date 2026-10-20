"""LLM client with per-call telemetry. Path: direct (Foundry) | gateway (APIM); stream on/off;
API: Responses (default) | Chat Completions.

Every attempt (including retries) produces one record with: time to response headers, time to
first byte/chunk, longest silent gap on the connection, total time, HTTP status, tokens and
correlation ids. The SDK's own retries are disabled so that retry behaviour is explicit and visible.

Note: GPT-6 Sol rejects function tools together with reasoning_effort on /chat/completions
(observed, HTTP 400), so tool-using agents need the Responses API.
"""

import asyncio
import time
import uuid
from collections.abc import Awaitable, Callable
from contextvars import ContextVar
from dataclasses import dataclass, field
from datetime import UTC, datetime
from typing import Any

import httpx
import openai

from worker.config import RunConfig, Settings

ID_HEADERS = (
    "x-request-id",
    "apim-request-id",
    "x-ms-request-id",
    "request-id",
    "x-ms-client-request-id",
    "x-ms-region",
    "x-mock-request-id",
)
RETRYABLE_STATUS = {408, 409, 429, 500, 502, 503, 504}
FOUNDRY_SCOPE = "https://cognitiveservices.azure.com/.default"

Recorder = Callable[[dict[str, Any]], Awaitable[None]]


@dataclass
class _Attempt:
    t0: float = 0.0
    t_headers: float | None = None
    status: int | None = None
    headers: dict[str, str] = field(default_factory=dict)


_current: ContextVar[_Attempt | None] = ContextVar("llm_attempt", default=None)


async def _on_response(resp: httpx.Response) -> None:
    a = _current.get()
    if a is not None and a.t_headers is None:  # headers are in; the body has not been read yet
        a.t_headers = time.monotonic()
        a.status = resp.status_code
        a.headers = {k.lower(): v for k, v in resp.headers.items()}


@dataclass
class ChatResult:
    content: str = ""
    tool_calls: list[dict[str, Any]] = field(default_factory=list)
    finish_reason: str = ""
    response_id: str = ""


@dataclass
class _Usage:
    prompt: int | None = None
    completion: int | None = None
    reasoning: int | None = None


class LLMCallError(RuntimeError):
    pass


def longest_gap(points: list[float]) -> float | None:
    return max((b - a for a, b in zip(points, points[1:], strict=False)), default=None)


def _is_retryable(e: BaseException) -> bool:
    if isinstance(e, openai.APIStatusError):
        return e.status_code in RETRYABLE_STATUS
    return isinstance(e, openai.APIConnectionError | httpx.TransportError | asyncio.TimeoutError)


def _flat_tool(spec: dict[str, Any]) -> dict[str, Any]:
    """Chat-style {"type":"function","function":{...}} -> Responses-style flat function tool."""
    return {"type": "function", **spec["function"]}


class LLMClient:
    def __init__(
        self,
        st: Settings,
        cfg: RunConfig,
        run_id: str,
        recorder: Recorder,
        credential=None,
        transport: httpx.AsyncBaseTransport | None = None,
    ) -> None:
        self.st, self.cfg, self.run_id, self.record = st, cfg, run_id, recorder
        headers: dict[str, str] = {}
        api_key: str | Callable[[], Awaitable[str]]
        if st.direct_base_url_override and cfg.path == "direct":
            base_url = st.direct_base_url_override
            api_key = "unused"
            headers["x-mock-key"] = st.direct_key_override
        elif cfg.path == "direct":
            from azure.identity.aio import get_bearer_token_provider

            base_url = f"{st.foundry_endpoint.rstrip('/')}/openai/v1/"
            api_key = get_bearer_token_provider(credential, FOUNDRY_SCOPE)
        else:
            base_url = f"{st.apim_url.rstrip('/')}/llm-{cfg.gateway_variant}"
            api_key = "unused"  # APIM authenticates to Foundry itself; callers use the APIM key
            headers["api-key"] = st.apim_key
            headers["Ocp-Apim-Subscription-Key"] = st.apim_key
        http = httpx.AsyncClient(
            timeout=httpx.Timeout(st.llm_read_timeout_s, connect=30),
            event_hooks={"response": [_on_response]},
            transport=transport,
        )
        self.client = openai.AsyncOpenAI(
            base_url=base_url,
            api_key=api_key,
            http_client=http,
            max_retries=0,
            default_headers=headers,
        )

    async def aclose(self) -> None:
        await self.client.close()

    def conversation(self, agent: str, system: str, round_no: int = 1) -> "Conversation":
        return Conversation(self, agent, system, round_no)

    async def _attempts(
        self,
        base: dict[str, Any],
        runner: Callable[[dict[str, Any], list[float], _Usage], Awaitable[ChatResult]],
    ) -> ChatResult:
        last: Exception | None = None
        for attempt in range(1, max(1, self.st.llm_max_attempts) + 1):
            rec = {
                **base,
                "kind": "llm",
                "run_id": self.run_id,
                "ts_utc": datetime.now(UTC).isoformat(timespec="seconds"),
                "attempt": attempt,
                "path": self.cfg.path,
                "gateway_variant": self.cfg.gateway_variant if self.cfg.path == "gateway" else "",
                "stream": self.cfg.stream,
                "api": self.cfg.api,
                "reasoning_effort": self.cfg.reasoning_effort,
                "client_request_id": str(uuid.uuid4()),
            }
            try:
                res = await self._instrumented(rec, runner)
                rec["outcome"] = "completed"
                await self.record(rec)
                return res
            except Exception as e:  # noqa: BLE001 - every failure mode is data
                last = e
                rec["outcome"] = (
                    "truncated" if rec.get("http_status") == 200 and rec.get("chunks") else "error"
                )
                if isinstance(e, openai.APIStatusError):
                    rec["http_status"] = e.status_code
                rec["error_type"] = type(e).__name__
                rec["error_detail"] = str(e)[:300]
                await self.record(rec)
                if attempt < self.st.llm_max_attempts and _is_retryable(e):
                    await asyncio.sleep(self.st.llm_retry_backoff_s * attempt)
                    continue
                break
        raise LLMCallError(f"{base['agent']}: {type(last).__name__}: {last}") from last

    async def _instrumented(self, rec, runner) -> ChatResult:
        a = _Attempt(t0=time.monotonic())
        token = _current.set(a)
        chunk_times: list[float] = []
        usage = _Usage()
        try:
            return await runner(rec, chunk_times, usage)
        finally:
            end = time.monotonic()
            _current.reset(token)
            rec["http_status"] = a.status
            rec["total_s"] = round(end - a.t0, 3)
            rec["ttfh_s"] = round(a.t_headers - a.t0, 3) if a.t_headers else None
            rec["chunks"] = len(chunk_times)
            if chunk_times:
                rec["ttfb_s"] = round(chunk_times[0] - a.t0, 3)
                pts = ([a.t_headers] if a.t_headers else []) + chunk_times
                gap = longest_gap(pts)
                rec["longest_gap_s"] = round(gap, 3) if gap is not None else None
                rec["last_chunk_s"] = round(chunk_times[-1] - a.t0, 3)
            elif a.t_headers and not self.cfg.stream:
                rec["ttfb_s"] = rec["ttfh_s"]
            rec["request_ids"] = ";".join(
                f"{h}={a.headers[h]}" for h in ID_HEADERS if h in a.headers
            )
            rec["prompt_tokens"] = usage.prompt
            rec["completion_tokens"] = usage.completion
            rec["reasoning_tokens"] = usage.reasoning

    # ---- Chat Completions ----------------------------------------------------------------
    async def chat_call(self, base, messages, tools) -> ChatResult:
        async def run(rec, times: list[float], usage: _Usage) -> ChatResult:
            kwargs: dict[str, Any] = {
                "model": self.st.model,
                "messages": messages,
                "max_completion_tokens": self.cfg.max_output_tokens,
                "extra_headers": {"x-ms-client-request-id": rec["client_request_id"]},
            }
            if self.cfg.reasoning_effort and self.cfg.reasoning_effort != "none":
                kwargs["reasoning_effort"] = self.cfg.reasoning_effort
            if tools:
                kwargs["tools"] = tools
            if not self.cfg.stream:
                resp = await self.client.chat.completions.create(**kwargs)
                choice = resp.choices[0]
                self._chat_usage(resp.usage, usage)
                return ChatResult(
                    content=choice.message.content or "",
                    tool_calls=[
                        {"id": t.id, "name": t.function.name, "arguments": t.function.arguments}
                        for t in (choice.message.tool_calls or [])
                    ],
                    finish_reason=choice.finish_reason or "",
                )
            stream = await self.client.chat.completions.create(
                **kwargs, stream=True, stream_options={"include_usage": True}
            )
            content: list[str] = []
            calls: dict[int, dict[str, str]] = {}
            finish = ""
            async for chunk in stream:
                times.append(time.monotonic())
                if chunk.usage:
                    self._chat_usage(chunk.usage, usage)
                for ch in chunk.choices:
                    if ch.delta.content:
                        content.append(ch.delta.content)
                    for tc in ch.delta.tool_calls or []:
                        c = calls.setdefault(tc.index, {"id": "", "name": "", "arguments": ""})
                        c["id"] = tc.id or c["id"]
                        if tc.function:
                            c["name"] += tc.function.name or ""
                            c["arguments"] += tc.function.arguments or ""
                    finish = ch.finish_reason or finish
            return ChatResult("".join(content), [calls[i] for i in sorted(calls)], finish)

        return await self._attempts(base, run)

    @staticmethod
    def _chat_usage(u, out: _Usage) -> None:
        if u is None:
            return
        out.prompt, out.completion = u.prompt_tokens, u.completion_tokens
        out.reasoning = getattr(
            getattr(u, "completion_tokens_details", None), "reasoning_tokens", None
        )

    # ---- Responses API -------------------------------------------------------------------
    async def responses_call(self, base, input_items, tools, previous_id) -> ChatResult:
        async def run(rec, times: list[float], usage: _Usage) -> ChatResult:
            kwargs: dict[str, Any] = {
                "model": self.st.model,
                "input": input_items,
                "max_output_tokens": self.cfg.max_output_tokens,
                "store": True,  # lets follow-up turns send only tool outputs (previous_response_id)
                "extra_headers": {"x-ms-client-request-id": rec["client_request_id"]},
            }
            if self.cfg.reasoning_effort and self.cfg.reasoning_effort != "none":
                kwargs["reasoning"] = {"effort": self.cfg.reasoning_effort}
            if tools:
                kwargs["tools"] = [_flat_tool(t) for t in tools]
            if previous_id:
                kwargs["previous_response_id"] = previous_id
            if not self.cfg.stream:
                final = await self.client.responses.create(**kwargs)
            else:
                final = None
                stream = await self.client.responses.create(**kwargs, stream=True)
                async for ev in stream:
                    times.append(time.monotonic())
                    if ev.type == "response.completed":
                        final = ev.response
                    elif ev.type in ("response.failed", "response.incomplete", "error"):
                        detail = getattr(getattr(ev, "response", None), "error", None) or getattr(
                            ev, "message", ""
                        )
                        raise RuntimeError(f"stream ended with {ev.type}: {detail}"[:300])
                if final is None:
                    raise RuntimeError("stream ended without response.completed")
            u = getattr(final, "usage", None)
            if u is not None:
                usage.prompt, usage.completion = u.input_tokens, u.output_tokens
                usage.reasoning = getattr(
                    getattr(u, "output_tokens_details", None), "reasoning_tokens", None
                )
            calls = [
                {"id": it.call_id, "name": it.name, "arguments": it.arguments}
                for it in final.output
                if it.type == "function_call"
            ]
            text = "".join(
                part.text
                for it in final.output
                if it.type == "message"
                for part in it.content
                if getattr(part, "type", "") == "output_text"
            )
            return ChatResult(text, calls, getattr(final, "status", "") or "", final.id)

        return await self._attempts(base, run)


class Conversation:
    """One agent's multi-turn exchange, independent of which API carries it."""

    def __init__(self, llm: LLMClient, agent: str, system: str, round_no: int) -> None:
        self.llm, self.agent, self.system, self.round_no = llm, agent, system, round_no
        self.turn = 0
        self.messages: list[dict[str, Any]] = [{"role": "system", "content": system}]
        self.prev_id: str | None = None
        self.last: ChatResult | None = None

    def _base(self, input_chars: int) -> dict[str, Any]:
        return {
            "round": self.round_no,
            "agent": self.agent,
            "turn": self.turn,
            "input_chars": input_chars,
        }

    async def _send(self, new_items: list[dict[str, Any]], tools) -> ChatResult:
        if self.llm.cfg.api == "chat":
            self.messages += new_items
            chars = sum(len(str(m.get("content") or "")) for m in self.messages)
            res = await self.llm.chat_call(self._base(chars), self.messages, tools)
        else:
            items = new_items
            if self.prev_id is None:
                items = [{"role": "developer", "content": self.system}] + new_items
            chars = sum(len(str(m.get("content") or m.get("output") or "")) for m in items)
            res = await self.llm.responses_call(self._base(chars), items, tools, self.prev_id)
            self.prev_id = res.response_id
        self.turn += 1
        self.last = res
        return res

    async def ask(self, user_text: str, tools=None) -> ChatResult:
        return await self._send([{"role": "user", "content": user_text}], tools)

    async def tool_results(self, results: list[tuple[str, str]], tools=None) -> ChatResult:
        """results: (call_id, output) for each tool call in the previous assistant turn."""
        assert self.last is not None
        if self.llm.cfg.api == "chat":
            self.messages.append(
                {
                    "role": "assistant",
                    "content": self.last.content or None,
                    "tool_calls": [
                        {
                            "id": t["id"],
                            "type": "function",
                            "function": {"name": t["name"], "arguments": t["arguments"]},
                        }
                        for t in self.last.tool_calls
                    ],
                }
            )
            new = [{"role": "tool", "tool_call_id": cid, "content": out} for cid, out in results]
        else:
            new = [
                {"type": "function_call_output", "call_id": cid, "output": out}
                for cid, out in results
            ]
        return await self._send(new, tools)
