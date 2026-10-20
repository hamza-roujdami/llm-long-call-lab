import asyncio
import json
import socket
import threading
import time

import httpx
import pytest
import uvicorn

from probe.mock.app import app as mock_app
from probe.mock.app import settings as mock_settings
from worker.agents.base import parse_json
from worker.config import RunConfig, Settings
from worker.llm_client import LLMCallError, LLMClient
from worker.orchestrator import execute, select_by_tokens, summarise
from worker.store import MemoryStore

TOOLS = [{"type": "function", "function": {"name": "ai_search", "parameters": {"type": "object"}}}]
APIS = ["chat", "responses"]


def _settings(**kw) -> Settings:
    return Settings(
        store_mode="memory", direct_base_url_override="http://mock/v1", direct_key_override="", **kw
    )


def _llm(st, cfg, recorder, transport=None):
    t = transport or httpx.ASGITransport(app=mock_app)
    return LLMClient(st, cfg, "r1", recorder, transport=t)


def run(coro):
    return asyncio.run(coro)


async def _ask(cfg, recs, tools=None, st=None, transport=None, follow_up=False):
    async def rec(r):
        recs.append(r)

    llm = _llm(st or _settings(), cfg, rec, transport)
    try:
        conv = llm.conversation("t", "be brief")
        res = await conv.ask("hi", tools)
        if follow_up:
            res = await conv.tool_results([(res.tool_calls[0]["id"], "[]")], None)
        return res
    finally:
        await llm.aclose()


@pytest.mark.parametrize("api", APIS)
@pytest.mark.parametrize("stream", [False, True])
def test_llm_client_records_telemetry(stream, api):
    recs = []
    res = run(_ask(RunConfig(stream=stream, api=api), recs))
    assert json.loads(res.content) == {"mock": True}
    r = recs[0]
    assert r["outcome"] == "completed" and r["http_status"] == 200 and r["api"] == api
    assert r["ttfh_s"] is not None and r["ttfb_s"] is not None and r["total_s"] >= r["ttfb_s"]
    assert r["prompt_tokens"] == 11 and r["reasoning_tokens"] == 5
    assert "x-mock-request-id=" in r["request_ids"]
    if stream:
        assert r["chunks"] >= 2 and r["longest_gap_s"] is not None
    else:
        assert r["chunks"] == 0


@pytest.mark.parametrize("api", APIS)
@pytest.mark.parametrize("stream", [False, True])
def test_tool_call_then_follow_up(stream, api):
    recs = []
    res = run(_ask(RunConfig(stream=stream, api=api), recs, tools=TOOLS, follow_up=True))
    assert json.loads(res.content) == {"mock": True}
    assert [r["turn"] for r in recs] == [0, 1]
    assert all(r["outcome"] == "completed" for r in recs)


@pytest.mark.parametrize("api", APIS)
def test_first_turn_returns_tool_call(api):
    recs = []
    res = run(_ask(RunConfig(stream=True, api=api), recs, tools=TOOLS))
    assert res.tool_calls[0]["name"] == "ai_search"
    assert json.loads(res.tool_calls[0]["arguments"]) == {"query": "vlan"}


@pytest.fixture
def live_mock():
    """Real uvicorn server: the in-process ASGI transport buffers whole responses, hiding gaps."""
    with socket.socket() as sock:
        sock.bind(("127.0.0.1", 0))
        port = sock.getsockname()[1]
    server = uvicorn.Server(
        uvicorn.Config(mock_app, host="127.0.0.1", port=port, log_level="error")
    )
    thread = threading.Thread(target=server.run, daemon=True)
    thread.start()
    while not server.started:
        time.sleep(0.05)
    yield f"http://127.0.0.1:{port}/v1"
    server.should_exit = True
    thread.join(timeout=5)


@pytest.mark.parametrize("api", APIS)
def test_silent_gap_is_measured(api, monkeypatch, live_mock):
    monkeypatch.setattr(mock_settings, "chat_first_delay", 0.6)
    recs = []
    st = Settings(store_mode="memory", direct_base_url_override=live_mock)

    async def go():
        async def rec(r):
            recs.append(r)

        llm = LLMClient(st, RunConfig(stream=True, api=api), "r1", rec)
        await llm.conversation("t", "s").ask("x")
        await llm.aclose()

    run(go())
    r = recs[0]
    assert r["ttfh_s"] < 0.4  # headers arrive immediately
    assert r["longest_gap_s"] >= 0.5  # then the connection is silent
    if api == "chat":
        assert r["ttfb_s"] >= 0.55  # no chunk at all until the silence ends
    else:
        assert r["ttfb_s"] < 0.4  # Responses sends created/in_progress events first


@pytest.mark.parametrize("api", APIS)
def test_retry_visible_per_attempt(api):
    calls = {"n": 0}

    def handler(request: httpx.Request) -> httpx.Response:
        calls["n"] += 1
        return httpx.Response(503, json={"error": {"message": "busy"}})

    recs = []
    st = _settings(llm_max_attempts=3, llm_retry_backoff_s=0.01)
    with pytest.raises(LLMCallError):
        run(
            _ask(
                RunConfig(stream=False, api=api),
                recs,
                st=st,
                transport=httpx.MockTransport(handler),
            )
        )
    assert calls["n"] == 3
    assert [r["attempt"] for r in recs] == [1, 2, 3]
    assert all(r["http_status"] == 503 and r["outcome"] == "error" for r in recs)


def test_parse_json_variants():
    assert parse_json('```json\n{"a": 1}\n```') == {"a": 1}
    assert parse_json('Here you go: {"a": {"b": 2}} done') == {"a": {"b": 2}}
    with pytest.raises(ValueError):
        parse_json("no json")


def test_select_by_tokens_respects_budget():
    facts = [{"id": f"F{i}", "text": "x" * 400} for i in range(100)]
    picked = select_by_tokens(facts, 1000)
    assert 0 < len(picked) < 100
    assert select_by_tokens(facts, 10**9) == facts


def test_summarise():
    calls = [
        {"kind": "llm", "outcome": "completed", "ttfb_s": 1.0, "longest_gap_s": 5.0, "total_s": 9.0,
         "prompt_tokens": 10, "completion_tokens": 2, "reasoning_tokens": 1},
        {"kind": "llm", "outcome": "error", "ttfb_s": 3.0, "total_s": 4.0},
        {"kind": "tool", "total_s": 0.1},
    ]  # fmt: skip
    s = summarise(calls, 12.3)
    assert s["llm_calls"] == 2 and s["failed_calls"] == 1 and s["max_ttfb_s"] == 3.0
    assert s["max_longest_gap_s"] == 5.0 and s["prompt_tokens"] == 10


@pytest.mark.parametrize("api", APIS)
def test_pipeline_end_to_end_with_fake_model(api, tmp_path):
    facts = [
        {"id": f"F{i}", "page": i, "topic": t, "section": "s", "text": f"{t} fact {i}"}
        for i, t in enumerate(["cover", "network", "addressing", "compute"] * 3)
    ]
    fp = tmp_path / "facts.jsonl"
    fp.write_text("".join(json.dumps(f) + "\n" for f in facts))
    st = _settings(facts_path=str(fp))
    store = MemoryStore()
    searched = []

    async def fake_search(query, topic):
        searched.append((query, topic))
        return "[]"

    def make(st_, cfg_, run_id, rec):
        return _llm(st_, cfg_, rec)

    async def go():
        await store.create_run("r1", {"status": "queued"})
        return await execute("r1", st, RunConfig(rounds=2, api=api), store, make, fake_search)

    summary = run(go())
    assert store.runs["r1"]["status"] == "succeeded" and store.runs["r1"]["progress"] == "10/10"
    kinds = [c["kind"] for c in store.calls["r1"]]
    assert kinds.count("tool") == 8 and kinds.count("llm") == 2 * (1 + 4 * 2)
    assert searched[0] == ("vlan", None)
    assert summary["failed_calls"] == 0
    out = store.outputs["r1"]
    assert len(out["rounds"]) == 2 and set(out["rounds"][0]["sections"]) == {
        "cover", "network", "addressing", "compute",
    }  # fmt: skip
    assert all("parse_error" not in s for s in out["rounds"][0]["sections"].values())


def test_failed_run_is_recorded(tmp_path):
    fp = tmp_path / "f.jsonl"
    fp.write_text(
        json.dumps({"id": "F1", "page": 1, "topic": "cover", "section": "s", "text": "t"}) + "\n"
    )
    st = _settings(facts_path=str(fp))
    store = MemoryStore()

    def make(st_, cfg_, run_id, rec):
        return _llm(st_, cfg_, rec, httpx.MockTransport(lambda r: httpx.Response(500, json={})))

    async def go():
        await store.create_run("r1", {"status": "queued"})
        with pytest.raises(LLMCallError):
            await execute("r1", st, RunConfig(), store, make, None)

    run(go())
    assert store.runs["r1"]["status"] == "failed" and "LLMCallError" in store.runs["r1"]["error"]
