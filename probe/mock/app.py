"""Fake model backend with controllable silence, so timeouts can be measured.

Every endpoint ends with a completion marker (`data: [DONE]` for streams, `"done": true`
for /silent) so the client can tell a clean finish from a dropped connection.
TCP keepalive is deliberately NOT enabled: idle sockets stay idle, as in the scenarios under test.
"""

import asyncio
import json
import logging
import time
import uuid
from collections.abc import AsyncIterator

from fastapi import Depends, FastAPI, Header, HTTPException, Query, Request
from fastapi.responses import JSONResponse, StreamingResponse
from pydantic_settings import BaseSettings

logger = logging.getLogger("mock")
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s")

MAX_SECONDS = 1800
DONE = b"data: [DONE]\n\n"


class Settings(BaseSettings):
    mock_api_key: str = ""
    chat_first_delay: float = 0.0  # seconds of silence before the first chat byte


settings = Settings()
app = FastAPI(title="apim-timeout-lab mock model")


def require_key(x_mock_key: str | None = Header(default=None)) -> None:
    if settings.mock_api_key and x_mock_key != settings.mock_api_key:
        raise HTTPException(status_code=401, detail="missing or invalid x-mock-key")


def _request_id(request: Request) -> str:
    return request.headers.get("x-client-request-id") or str(uuid.uuid4())


def _chunk(seq: int, started: float) -> bytes:
    return f'data: {{"seq": {seq}, "t": {time.monotonic() - started:.2f}}}\n\n'.encode()


async def _emit_for(
    duration: float, interval: float, seq: int, started: float
) -> AsyncIterator[bytes]:
    """Yield a chunk now and every `interval` seconds until `duration` has elapsed."""
    end = time.monotonic() + duration
    while True:
        yield _chunk(seq, started)
        seq += 1
        remaining = end - time.monotonic()
        if remaining <= 0:
            return
        await asyncio.sleep(min(interval, remaining))


def _stream_response(gen: AsyncIterator[bytes], rid: str) -> StreamingResponse:
    return StreamingResponse(
        gen,
        media_type="text/event-stream",
        headers={"x-mock-request-id": rid, "Cache-Control": "no-cache", "X-Accel-Buffering": "no"},
    )


@app.get("/health")
async def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/silent", dependencies=[Depends(require_key)])
async def silent(request: Request, delay: float = Query(0, ge=0, le=MAX_SECONDS)) -> JSONResponse:
    """Send nothing (not even headers) for `delay` seconds, then a JSON body."""
    rid = _request_id(request)
    logger.info("silent start rid=%s delay=%s", rid, delay)
    await asyncio.sleep(delay)
    logger.info("silent end rid=%s", rid)
    return JSONResponse({"done": True, "delay": delay}, headers={"x-mock-request-id": rid})


@app.get("/stream", dependencies=[Depends(require_key)])
async def stream(
    request: Request,
    total: float = Query(60, gt=0, le=MAX_SECONDS),
    interval: float = Query(5, gt=0, le=MAX_SECONDS),
) -> StreamingResponse:
    """Emit one chunk immediately, then one every `interval` seconds, for `total` seconds."""
    rid = _request_id(request)

    async def gen() -> AsyncIterator[bytes]:
        started = time.monotonic()
        logger.info("stream start rid=%s total=%s interval=%s", rid, total, interval)
        try:
            async for c in _emit_for(total, interval, 0, started):
                yield c
            yield DONE
            logger.info("stream end rid=%s", rid)
        except asyncio.CancelledError:
            logger.info("stream cancelled rid=%s after=%.1fs", rid, time.monotonic() - started)
            raise

    return _stream_response(gen(), rid)


@app.get("/gap", dependencies=[Depends(require_key)])
async def gap(
    request: Request,
    first: float = Query(10, ge=0, le=MAX_SECONDS),
    gap: float = Query(300, ge=0, le=MAX_SECONDS),
    then: float = Query(30, ge=0, le=MAX_SECONDS),
    interval: float = Query(1, gt=0, le=MAX_SECONDS),
) -> StreamingResponse:
    """Chunks for `first` s, total silence for `gap` s, then chunks for `then` s."""
    rid = _request_id(request)

    async def gen() -> AsyncIterator[bytes]:
        started = time.monotonic()
        logger.info("gap start rid=%s first=%s gap=%s then=%s", rid, first, gap, then)
        try:
            seq = 0
            async for c in _emit_for(first, interval, seq, started):
                seq += 1
                yield c
            await asyncio.sleep(gap)
            async for c in _emit_for(then, interval, seq, started):
                seq += 1
                yield c
            yield DONE
            logger.info("gap end rid=%s", rid)
        except asyncio.CancelledError:
            logger.info("gap cancelled rid=%s after=%.1fs", rid, time.monotonic() - started)
            raise

    return _stream_response(gen(), rid)


def _chat_payload(model: str, tool_call: bool) -> dict:
    msg: dict = {"role": "assistant", "content": None if tool_call else '{"mock": true}'}
    if tool_call:
        msg["tool_calls"] = [
            {
                "id": "call_mock1",
                "type": "function",
                "function": {"name": "ai_search", "arguments": '{"query": "vlan"}'},
            }
        ]
    return {
        "id": "chatcmpl-mock",
        "object": "chat.completion",
        "created": int(time.time()),
        "model": model,
        "choices": [
            {
                "index": 0,
                "message": msg,
                "finish_reason": "tool_calls" if tool_call else "stop",
            }
        ],
        "usage": {
            "prompt_tokens": 11,
            "completion_tokens": 7,
            "total_tokens": 18,
            "completion_tokens_details": {"reasoning_tokens": 5},
        },
    }


@app.post("/v1/chat/completions", dependencies=[Depends(require_key)])
async def chat_completions(request: Request):
    """OpenAI-compatible fake: optional silence, then JSON or SSE. Calls ai_search once if offered."""
    body = await request.json()
    rid = _request_id(request)
    delay = float(request.headers.get("x-mock-first-delay", settings.chat_first_delay))
    asked_tool_call = bool(body.get("tools")) and not any(
        m.get("role") == "tool" for m in body.get("messages", [])
    )
    payload = _chat_payload(body.get("model", "mock"), asked_tool_call)
    headers = {"x-mock-request-id": rid}
    if not body.get("stream"):
        await asyncio.sleep(delay)
        return JSONResponse(payload, headers=headers)

    async def gen() -> AsyncIterator[bytes]:
        await asyncio.sleep(delay)
        choice = payload["choices"][0]
        base = {k: payload[k] for k in ("id", "object", "created", "model")}
        base["object"] = "chat.completion.chunk"
        if asked_tool_call:
            deltas = [
                {
                    "role": "assistant",
                    "tool_calls": [{"index": 0, **choice["message"]["tool_calls"][0]}],
                }
            ]
        else:
            text = choice["message"]["content"]
            deltas = [{"role": "assistant", "content": ""}] + [
                {"content": text[i : i + 4]} for i in range(0, len(text), 4)
            ]
        for d in deltas:
            yield f"data: {json.dumps({**base, 'choices': [{'index': 0, 'delta': d}]})}\n\n".encode()
            await asyncio.sleep(0.05)
        last = {
            **base,
            "choices": [{"index": 0, "delta": {}, "finish_reason": choice["finish_reason"]}],
        }
        yield f"data: {json.dumps(last)}\n\n".encode()
        usage = {**base, "choices": [], "usage": payload["usage"]}
        yield f"data: {json.dumps(usage)}\n\n".encode()
        yield DONE

    return _stream_response(gen(), rid)


def _response_obj(model: str, tool_call: bool, status: str = "completed") -> dict:
    if tool_call:
        output: list[dict] = [
            {
                "type": "function_call",
                "id": "fc_mock1",
                "call_id": "call_mock1",
                "name": "ai_search",
                "arguments": '{"query": "vlan"}',
                "status": "completed",
            }
        ]
    else:
        output = [
            {
                "type": "message",
                "id": "msg_mock1",
                "role": "assistant",
                "status": "completed",
                "content": [{"type": "output_text", "text": '{"mock": true}', "annotations": []}],
            }
        ]
    return {
        "id": f"resp_mock_{uuid.uuid4().hex[:8]}",
        "object": "response",
        "created_at": int(time.time()),
        "status": status,
        "model": model,
        "output": output if status == "completed" else [],
        "usage": {
            "input_tokens": 11,
            "output_tokens": 7,
            "total_tokens": 18,
            "output_tokens_details": {"reasoning_tokens": 5},
            "input_tokens_details": {"cached_tokens": 0},
        },
        "parallel_tool_calls": True,
        "tool_choice": "auto",
        "tools": [],
        "metadata": {},
    }


def _sse(event: dict) -> bytes:
    return f"event: {event['type']}\ndata: {json.dumps(event)}\n\n".encode()


@app.post("/v1/responses", dependencies=[Depends(require_key)])
async def responses(request: Request):
    """OpenAI Responses-API fake: optional silence after the opening events, then output."""
    body = await request.json()
    rid = _request_id(request)
    delay = float(request.headers.get("x-mock-first-delay", settings.chat_first_delay))
    items = body.get("input") or []
    first_turn = not body.get("previous_response_id") and not any(
        isinstance(i, dict) and i.get("type") == "function_call_output" for i in items
    )
    tool_call = bool(body.get("tools")) and first_turn
    model = body.get("model", "mock")
    headers = {"x-mock-request-id": rid}
    if not body.get("stream"):
        await asyncio.sleep(delay)
        return JSONResponse(_response_obj(model, tool_call), headers=headers)

    async def gen() -> AsyncIterator[bytes]:
        final = _response_obj(model, tool_call)
        started = {**final, "status": "in_progress", "output": []}
        yield _sse({"type": "response.created", "sequence_number": 0, "response": started})
        yield _sse({"type": "response.in_progress", "sequence_number": 1, "response": started})
        await asyncio.sleep(delay)  # "reasoning": connection open, nothing sent
        seq = 2
        if not tool_call:
            for piece in ('{"mock"', ": true}"):
                yield _sse(
                    {
                        "type": "response.output_text.delta",
                        "sequence_number": seq,
                        "item_id": "msg_mock1",
                        "output_index": 0,
                        "content_index": 0,
                        "delta": piece,
                    }
                )
                seq += 1
                await asyncio.sleep(0.05)
        yield _sse({"type": "response.completed", "sequence_number": seq, "response": final})

    return _stream_response(gen(), rid)
