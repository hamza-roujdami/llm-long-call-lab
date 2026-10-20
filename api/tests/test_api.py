import asyncio

import httpx
import pytest

from api import main
from api.store import MemoryStore


@pytest.fixture
def client(monkeypatch):
    monkeypatch.setenv("STORE_MODE", "memory")
    monkeypatch.setenv("INTERNAL_TOKEN", "tok")
    main._store = MemoryStore()
    transport = httpx.ASGITransport(app=main.app)

    def call(method: str, url: str, **kw):
        async def go():
            async with httpx.AsyncClient(transport=transport, base_url="http://t") as c:
                return await c.request(method, url, **kw)

        return asyncio.run(go())

    yield call
    main._store = MemoryStore()


def test_create_poll_and_csv(client):
    r = client("POST", "/runs", json={"path": "apim-default", "stream": False})
    assert r.status_code == 202
    run_id = r.json()["run_id"]
    store = main._store
    store.calls[run_id] = [
        {"kind": "llm", "agent": "planner", "outcome": "completed", "ttfb_s": 2.5, "longest_gap_s": 90.0,
         "total_s": 120.0, "prompt_tokens": 100, "completion_tokens": 10, "reasoning_tokens": 4},
        {"kind": "tool", "agent": "network", "total_s": 0.2},
    ]  # fmt: skip
    got = client("GET", f"/runs/{run_id}").json()
    assert got["status"] == "queued" and '"path":"apim-default"' in got["config_json"]
    assert (
        got["live_summary"]["max_longest_gap_s"] == 90.0 and got["live_summary"]["llm_calls"] == 1
    )
    assert client("GET", "/runs").json()[0]["id"] == run_id
    csv_text = client("GET", f"/runs/{run_id}/calls.csv").text
    assert csv_text.splitlines()[0].startswith("ts_utc,run_id,label") and "planner" in csv_text


def test_validation_and_missing(client):
    assert client("POST", "/runs", json={"rounds": 0}).status_code == 422
    assert client("POST", "/runs", json={"reasoning_effort": "ultra"}).status_code == 422
    assert client("GET", "/runs/nope").status_code == 404
    assert client("GET", "/runs/nope/output").status_code == 404


def test_internal_callbacks_require_token_and_feed_polling(client):
    run_id = client("POST", "/runs", json={}).json()["run_id"]
    h = {"x-internal-token": "tok"}
    assert (
        client("POST", f"/internal/runs/{run_id}/update", json={"status": "running"}).status_code
        == 401
    )
    assert (
        client(
            "POST",
            f"/internal/runs/{run_id}/update",
            json={"status": "running", "phase": "p"},
            headers=h,
        ).status_code
        == 200
    )
    call = {
        "kind": "llm",
        "agent": "planner",
        "outcome": "completed",
        "ttfb_s": 1.5,
        "longest_gap_s": 40.0,
    }
    assert client("POST", f"/internal/runs/{run_id}/calls", json=call, headers=h).status_code == 200
    assert (
        client("PUT", f"/internal/runs/{run_id}/output", json={"rounds": []}, headers=h).status_code
        == 200
    )
    got = client("GET", f"/runs/{run_id}").json()
    assert got["status"] == "running" and got["phase"] == "p"
    assert got["live_summary"]["max_longest_gap_s"] == 40.0 and len(got["calls"]) == 1
    assert client("GET", f"/runs/{run_id}/output").json() == {"rounds": []}
