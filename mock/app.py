"""Fake model backend with controllable silence, so timeouts can be measured.

Every endpoint ends with a completion marker (`data: [DONE]` for streams, `"done": true`
for /silent) so the client can tell a clean finish from a dropped connection.
TCP keepalive is deliberately NOT enabled: idle sockets stay idle, as in the scenarios under test.
"""

import asyncio
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
