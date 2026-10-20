import asyncio
import time

import httpx
import pytest

from probe.mock.app import app, settings


def get(path: str, **kw) -> tuple[httpx.Response, float]:
    async def go():
        t = time.monotonic()
        async with httpx.AsyncClient(
            transport=httpx.ASGITransport(app=app), base_url="http://t"
        ) as c:
            r = await c.get(path, **kw)
        return r, time.monotonic() - t

    return asyncio.run(go())


def test_health():
    r, _ = get("/health")
    assert r.json() == {"status": "ok"}


def test_silent_waits_then_done():
    r, took = get("/silent", params={"delay": 0.5})
    assert r.status_code == 200 and r.json()["done"] is True
    assert took >= 0.5


def test_stream_chunks_and_done_marker():
    r, took = get("/stream", params={"total": 1, "interval": 0.25})
    assert r.text.rstrip().endswith("data: [DONE]")
    assert r.text.count('"seq"') >= 4
    assert took >= 1


def test_gap_has_silence_between_chunks():
    r, took = get("/gap", params={"first": 0.2, "gap": 1, "then": 0.2, "interval": 0.1})
    assert r.text.rstrip().endswith("data: [DONE]")
    assert took >= 1.4


def test_rejects_out_of_range():
    r, _ = get("/silent", params={"delay": 99999})
    assert r.status_code == 422


def test_key_enforced_when_configured(monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setattr(settings, "mock_api_key", "s3cret")
    assert get("/silent", params={"delay": 0})[0].status_code == 401
    ok, _ = get("/silent", params={"delay": 0}, headers={"x-mock-key": "s3cret"})
    assert ok.status_code == 200
