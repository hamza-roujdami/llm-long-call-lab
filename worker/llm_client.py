"""The only place that talks to the model.

* `Model` builds an OpenAI client for one of three paths (direct | apim-default | apim-stream) whose
  HTTP transport times every call at the wire level: time to response headers, time to first body
  byte, time to first token, longest silent gap between chunks, total time, HTTP status, request IDs
  and token usage. One record per HTTP attempt, whatever sits on top (plain call or an agent loop).
* `call_model()` is the one-shot call used by the matrix: a Microsoft Agent Framework `Agent` with no tools.
* `Model.agent_client()` hands the same instrumented client to Microsoft Agent Framework.

SDK retries are disabled. Retries (only when LLM_MAX_ATTEMPTS > 1) happen in the transport, before
any body byte was delivered, and every attempt is its own record. No TCP keepalive is configured:
idle connections stay idle, which is exactly what the lab measures.

GPT-6 Sol rejects function tools together with reasoning_effort on /chat/completions (observed,
HTTP 400), so this client uses the Responses API only.
"""

import asyncio
import json
import re
import time
import uuid
from collections.abc import Awaitable, Callable, Iterator
from contextlib import contextmanager
from contextvars import ContextVar
from dataclasses import dataclass, field
from datetime import UTC, datetime
from typing import Any

import httpx
import openai

from worker.config import Settings
from worker.tracing import annotate_span

FOUNDRY_SCOPE = "https://cognitiveservices.azure.com/.default"
ID_HEADERS = (
    "x-request-id",
    "apim-request-id",
    "x-ms-request-id",
    "request-id",
    "x-ms-client-request-id",
    "x-ms-region",
)
RETRYABLE_STATUS = {408, 409, 429, 500, 502, 503, 504}
TOKEN_MARKERS = (b"output_text.delta", b"function_call_arguments.delta")
COMPLETION_MARKERS = (b"response.completed", b"response.failed", b"response.incomplete")
TAIL_BYTES = 16384

Recorder = Callable[[dict[str, Any]], Awaitable[None]]


async def _noop(_: dict[str, Any]) -> None:
    return None


@dataclass
class CallContext:
    run_id: str = ""
    label: str = ""
    agent: str = ""
    round_no: int = 1
    path: str = ""
    stream: bool = False
    turn: int = 0
    records: list[dict[str, Any]] = field(default_factory=list)


_ctx: ContextVar[CallContext | None] = ContextVar("call_ctx", default=None)


@contextmanager
def call_context(**kw: Any) -> Iterator[CallContext]:
    ctx = CallContext(**kw)
    token = _ctx.set(ctx)
    try:
        yield ctx
    finally:
        _ctx.reset(token)


def current_context() -> CallContext:
    return _ctx.get() or CallContext()


def longest_gap(points: list[float]) -> float | None:
    return max((b - a for a, b in zip(points, points[1:], strict=False)), default=None)


_USAGE = re.compile(r'"usage"\s*:\s*\{')


def parse_usage(tail: bytes) -> dict[str, int | None]:
    """Last non-null `usage` object in the tail of a response body (JSON or SSE)."""
    s = tail.decode("utf-8", "ignore")
    last = None
    for m in _USAGE.finditer(s):
        last = m
    if last is None:
        return {}
    try:
        obj, _ = json.JSONDecoder().raw_decode(s[last.end() - 1 :])
    except ValueError:
        return {}
    details = obj.get("output_tokens_details") or obj.get("completion_tokens_details") or {}
    return {
        "prompt_tokens": obj.get("input_tokens", obj.get("prompt_tokens")),
        "completion_tokens": obj.get("output_tokens", obj.get("completion_tokens")),
        "reasoning_tokens": details.get("reasoning_tokens"),
    }


def _ids(headers: httpx.Headers) -> str:
    return ";".join(f"{h}={headers[h]}" for h in ID_HEADERS if h in headers)


class _TimedStream(httpx.AsyncByteStream):
    def __init__(
        self,
        inner: httpx.AsyncByteStream,
        rec: dict[str, Any],
        ctx: CallContext,
        recorder: Recorder,
        t0: float,
        t_headers: float,
        want_stream: bool,
        pacer: "TokenPacer | None" = None,
    ) -> None:
        self.inner, self.rec, self.ctx, self.recorder = inner, rec, ctx, recorder
        self.pacer = pacer
        self.t0, self.t_headers, self.want_stream = t0, t_headers, want_stream
        self.times: list[float] = []
        self.t_token: float | None = None
        self.nbytes = 0
        self.tail = b""
        self.prev = b""
        self.saw_completion = (
            False  # a terminal event passed by (not only in the tail: it leads a huge event)
        )
        self.done = False

    async def __aiter__(self):
        try:
            async for chunk in self.inner:
                if chunk:
                    now = time.monotonic()
                    self.times.append(now)
                    self.nbytes += len(chunk)
                    if self.t_token is None and any(m in self.prev + chunk for m in TOKEN_MARKERS):
                        self.t_token = now
                    if any(m in self.prev + chunk for m in COMPLETION_MARKERS):
                        self.saw_completion = True
                    self.prev = chunk[-64:]
                    self.tail = (self.tail + chunk)[-TAIL_BYTES:]
                yield chunk
        except BaseException as e:  # noqa: BLE001 - includes cancellation and consumer abort
            await self._finish(e)
            raise
        await self._finish(None)

    async def aclose(self) -> None:
        await self._finish(GeneratorExit())  # closed before the body was fully read
        await self.inner.aclose()

    async def _finish(self, exc: BaseException | None) -> None:
        if self.done:
            return
        self.done = True
        end = time.monotonic()
        r, t0 = self.rec, self.t0
        r["total_s"] = round(end - t0, 3)
        r["chunks"] = len(self.times)
        r["bytes"] = self.nbytes
        if self.times:
            r["ttfb_s"] = round(self.times[0] - t0, 3)
            gap = longest_gap([self.t_headers, *self.times])
            r["longest_gap_s"] = round(gap, 3) if gap is not None else None
            r["last_chunk_s"] = round(self.times[-1] - t0, 3)
            r["tail_silence_s"] = round(end - self.times[-1], 3)
        else:
            r["tail_silence_s"] = round(end - self.t_headers, 3)
        if self.t_token is not None:
            r["ttft_s"] = round(self.t_token - t0, 3)
        r.update({k: v for k, v in parse_usage(self.tail).items() if v is not None})
        if self.pacer and r.get("prompt_tokens"):
            self.pacer.observe(
                (self.ctx.agent, self.ctx.round_no),
                r["prompt_tokens"] + (r.get("completion_tokens") or 0),
            )
        status = r.get("http_status") or 0
        if not 200 <= status < 300:
            r["outcome"] = "http_error"
            r["error_detail"] = self.tail.decode("utf-8", "ignore")[:300]
        elif b"rate limit" in self.tail.lower():
            r["outcome"] = "truncated"  # the error arrived inside a 200 stream
            r["error_type"] = "RateLimit"
            r["error_detail"] = self.tail.decode("utf-8", "ignore")[-300:]
        elif exc is not None:
            aborted = isinstance(exc, GeneratorExit | asyncio.CancelledError)
            r["outcome"] = "aborted" if aborted else "truncated"
            r["error_type"], r["error_detail"] = type(exc).__name__, str(exc)[:300]
        elif self.want_stream and not self.saw_completion:
            r["outcome"] = "truncated"
            r["error_type"] = "StreamEndedWithoutCompletion"
        else:
            r["outcome"] = "completed"
        annotate_span(r)
        await _emit(self.recorder, self.ctx, r)


async def _emit(recorder: Recorder, ctx: CallContext, rec: dict[str, Any]) -> None:
    ctx.records.append(rec)
    await recorder(rec)


class TokenPacer:
    """Client-side pacing for a tokens-per-minute quota (pipeline only; never used by the matrix).

    Estimates a request's tokens from its body size and waits until the last `window_s` seconds have room,
    so big multi-turn agents run slowly instead of failing with a rate-limit error. The wait happens BEFORE
    a call's timers start, so it never counts as call latency.
    """

    def __init__(self, tokens_per_window: int, window_s: float = 60.0) -> None:
        self.budget, self.window = tokens_per_window, window_s
        self.events: list[tuple[float, int]] = []
        self.context: dict[
            tuple[str, int], int
        ] = {}  # (agent, round) -> tokens of the conversation so far
        self._lock = asyncio.Lock()

    @staticmethod
    def estimate(body: bytes) -> int:
        return max(1, int(len(body) / 3.5))

    def estimate_request(self, body: bytes, chain: tuple[str, int]) -> int:
        """Tokens the service will count. A continuation (previous_response_id) sends only the new bytes but is
        billed for the whole conversation, so add the context size observed on the previous turn of the chain."""
        base = 0
        if b"previous_response_id" in body:
            base = self.context.get(chain, 0)
        return base + self.estimate(body)

    def observe(self, chain: tuple[str, int], context_tokens: int) -> None:
        self.context[chain] = context_tokens

    async def acquire(self, tokens: int) -> None:
        while True:
            async with self._lock:
                now = time.monotonic()
                self.events = [(t, n) for t, n in self.events if now - t < self.window]
                if not self.events or sum(n for _, n in self.events) + tokens <= self.budget:
                    self.events.append((now, tokens))
                    return
                wait = self.events[0][0] + self.window - now
            await asyncio.sleep(max(wait, 0.05) + 0.05)


class TimedTransport(httpx.AsyncBaseTransport):
    def __init__(
        self,
        inner: httpx.AsyncBaseTransport,
        recorder: Recorder,
        max_attempts: int = 1,
        backoff_s: float = 5.0,
        pacer: TokenPacer | None = None,
    ) -> None:
        self.inner, self.recorder, self.pacer = inner, recorder, pacer
        self.max_attempts, self.backoff_s = max(1, max_attempts), backoff_s

    async def handle_async_request(self, request: httpx.Request) -> httpx.Response:
        ctx = _ctx.get() or CallContext()
        ctx.turn += 1
        try:
            want_stream = bool(json.loads(request.content).get("stream"))
        except (ValueError, httpx.RequestNotRead):
            want_stream = False
        for attempt in range(1, self.max_attempts + 1):
            if self.pacer:
                await self.pacer.acquire(
                    self.pacer.estimate_request(request.content, (ctx.agent, ctx.round_no))
                )
            client_request_id = str(uuid.uuid4())
            request.headers["x-ms-client-request-id"] = client_request_id
            rec: dict[str, Any] = {
                "ts_utc": datetime.now(UTC).isoformat(timespec="seconds"),
                "run_id": ctx.run_id,
                "label": ctx.label,
                "round": ctx.round_no,
                "agent": ctx.agent,
                "turn": ctx.turn,
                "attempt": attempt,
                "kind": "llm",
                "path": ctx.path,
                "stream": want_stream,
                "input_bytes": len(request.content),
                "client_request_id": client_request_id,
            }
            t0 = time.monotonic()
            try:
                resp = await self.inner.handle_async_request(request)
            except Exception as e:
                rec.update(
                    outcome="error",
                    error_type=type(e).__name__,
                    error_detail=str(e)[:300],
                    total_s=round(time.monotonic() - t0, 3),
                )
                await _emit(self.recorder, ctx, rec)
                if attempt < self.max_attempts and isinstance(e, httpx.TransportError):
                    await asyncio.sleep(self.backoff_s * attempt)
                    continue
                raise
            t_headers = time.monotonic()
            rec["http_status"] = resp.status_code
            rec["ttfh_s"] = round(t_headers - t0, 3)
            rec["request_ids"] = _ids(resp.headers)
            if resp.status_code in RETRYABLE_STATUS and attempt < self.max_attempts:
                detail = b"".join([c async for c in resp.stream])[:300]
                await resp.stream.aclose()
                rec.update(
                    outcome="http_error",
                    error_detail=detail.decode("utf-8", "ignore"),
                    total_s=round(time.monotonic() - t0, 3),
                )
                await _emit(self.recorder, ctx, rec)
                await asyncio.sleep(self.backoff_s * attempt)
                continue
            stream = _TimedStream(
                resp.stream, rec, ctx, self.recorder, t0, t_headers, want_stream, self.pacer
            )
            return httpx.Response(
                resp.status_code,
                headers=resp.headers,
                stream=stream,
                extensions=resp.extensions,
                request=request,
            )
        raise RuntimeError("unreachable")


@dataclass
class CallResult:
    text: str = ""
    record: dict[str, Any] = field(default_factory=dict)
    error: str = ""

    @property
    def ok(self) -> bool:
        return not self.error and self.record.get("outcome") == "completed"


class Model:
    def __init__(
        self,
        st: Settings,
        path: str,
        recorder: Recorder = _noop,
        *,
        max_attempts: int | None = None,
        transport: httpx.AsyncBaseTransport | None = None,
        run_id: str = "",
    ) -> None:
        self.st, self.path, self.run_id = st, path, run_id
        self._credential = None
        self._maf_client = None
        headers: dict[str, str] = {}
        api_key: Any = "unused"
        if st.llm_base_url_override:
            base_url = st.llm_base_url_override
        elif path == "direct":
            from azure.identity.aio import DefaultAzureCredential, get_bearer_token_provider

            self._credential = (
                DefaultAzureCredential()
            )  # AZURE_CLIENT_ID picks the managed identity
            base_url = f"{st.foundry_endpoint.rstrip('/')}/openai/v1/"
            api_key = get_bearer_token_provider(self._credential, FOUNDRY_SCOPE)
        else:
            variant = path.removeprefix("apim-")
            base_url = f"{st.apim_url.rstrip('/')}/llm-{variant}"
            # APIM authenticates to Foundry itself; callers only present the APIM subscription key.
            headers = {"api-key": st.apim_key, "Ocp-Apim-Subscription-Key": st.apim_key}
        timed = TimedTransport(
            transport or httpx.AsyncHTTPTransport(retries=0),
            recorder,
            max_attempts=st.llm_max_attempts if max_attempts is None else max_attempts,
            backoff_s=st.llm_retry_backoff_s,
            pacer=TokenPacer(st.llm_tpm_budget)
            if st.llm_tpm_budget and max_attempts != 1
            else None,
        )
        http = httpx.AsyncClient(
            transport=timed, timeout=httpx.Timeout(st.llm_read_timeout_s, connect=30)
        )
        self.client = openai.AsyncOpenAI(
            base_url=base_url,
            api_key=api_key,
            http_client=http,
            max_retries=0,
            default_headers=headers,
        )

    def agent_client(self):
        """Microsoft Agent Framework chat client (Responses API) over the instrumented HTTP client."""
        from agent_framework.openai import OpenAIChatClient

        if self._maf_client is None:
            self._maf_client = OpenAIChatClient(model=self.st.model, async_client=self.client)
        return self._maf_client

    async def call(
        self,
        prompt: str,
        *,
        system: str | None = None,
        stream: bool = False,
        reasoning_effort: str = "high",
        max_output_tokens: int,
        label: str = "",
        agent: str = "call_model",
    ) -> CallResult:
        """One model call through a Microsoft Agent Framework `Agent` (no tools, one HTTP request).

        Never raises: failures are data and come back in the result.
        """
        from worker.agents import build_agent  # lazy: agents imports this module

        text = ""
        error = ""
        with call_context(
            run_id=self.run_id, label=label, agent=agent, path=self.path, stream=stream
        ) as ctx:
            try:
                maf_agent = build_agent(
                    self.agent_client(),
                    agent,
                    system,
                    reasoning_effort=reasoning_effort,
                    max_output_tokens=max_output_tokens,
                )
                if stream:
                    updates = maf_agent.run(prompt, stream=True)
                    async for _ in updates:
                        pass
                    text = (await updates.get_final_response()).text
                else:
                    text = (await maf_agent.run(prompt)).text
            except Exception as e:  # noqa: BLE001
                error = f"{type(e).__name__}: {e}"[:300]
        rec = ctx.records[-1] if ctx.records else {"outcome": "error", "error_detail": error}
        return CallResult(text, rec, error)

    async def aclose(self) -> None:
        await self.client.close()
        if self._credential is not None:
            await self._credential.close()


async def call_model(
    prompt: str,
    *,
    path: str = "direct",
    stream: bool = False,
    settings: Settings | None = None,
    recorder: Recorder = _noop,
    **kw: Any,
) -> CallResult:
    """call_model(prompt, path=direct|apim-default|apim-stream, stream=bool): one timed model call."""
    m = Model(settings or Settings(), path, recorder, max_attempts=1)
    try:
        return await m.call(prompt, stream=stream, **kw)
    finally:
        await m.aclose()
