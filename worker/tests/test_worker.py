import asyncio
import json

import httpx
import pytest

from worker.agents import build_agent, parse_json, run_agent
from worker.config import RunConfig, Settings
from worker.llm_client import Model, call_context, longest_gap, parse_usage
from worker.orchestrator import execute, select_by_tokens, summarise
from worker.results import RECORD_COLUMNS, append_csv, parse_call_lines
from worker.store import MemoryStore
from worker.tests import fake_model
from worker.tools.doc_search import make_search_tool


def run(coro):
    return asyncio.run(coro)


def settings(**kw) -> Settings:
    return Settings(store_mode="memory", llm_base_url_override="http://fake/v1", **kw)


def asgi():
    return httpx.ASGITransport(app=fake_model.app)


class _Broken(httpx.AsyncByteStream):
    """Delivers some bytes, then the connection dies (what an idle-timeout cut looks like)."""

    def __init__(self, chunks: list[bytes], error: Exception | None) -> None:
        self.chunks, self.error = chunks, error

    async def __aiter__(self):
        for c in self.chunks:
            yield c
        if self.error:
            raise self.error

    async def aclose(self) -> None:
        return None


def event_chunk() -> bytes:
    """A valid opening SSE event, as a real Responses stream starts."""
    started = {**fake_model._response("m", False), "status": "in_progress", "output": []}
    return fake_model._sse({"type": "response.created", "sequence_number": 0, "response": started})


def mock_transport(status=200, chunks=(b"data: x\n\n",), error=None):
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(status, stream=_Broken(list(chunks), error))

    return httpx.MockTransport(handler)


async def call(st=None, path="direct", transport=None, attempts=None, **kw):
    recs = []

    async def rec(r):
        recs.append(r)

    m = Model(st or settings(), path, rec, max_attempts=attempts, transport=transport or asgi())
    try:
        res = await m.call("hi", max_output_tokens=100, **kw)
    finally:
        await m.aclose()
    return res, recs


@pytest.mark.parametrize("stream", [False, True])
def test_call_model_records_every_metric(stream):
    res, recs = run(call(stream=stream, label="cell-1"))
    assert res.ok and json.loads(res.text) == {"fake": True}
    r = res.record
    assert r["label"] == "cell-1" and r["http_status"] == 200 and r["outcome"] == "completed"
    assert r["ttfh_s"] is not None and r["ttfb_s"] is not None and r["total_s"] >= r["ttfb_s"]
    assert (r["prompt_tokens"], r["completion_tokens"], r["reasoning_tokens"]) == (11, 7, 5)
    assert r["request_ids"].startswith("x-request-id=") and r["client_request_id"]
    assert r["stream"] is stream and (("ttft_s" in r) is stream)
    assert len(recs) == 1
    assert set(r) - set(RECORD_COLUMNS) == set()  # every field is a CSV column


def test_silent_gap_is_measured_on_the_wire(live_fake):
    fake_model.FIRST_DELAY = 0.7
    st = Settings(store_mode="memory", llm_base_url_override=live_fake)

    async def go():
        m = Model(st, "direct", max_attempts=1)
        try:
            return await m.call("x", stream=True, max_output_tokens=50)
        finally:
            await m.aclose()

    r = run(go()).record
    assert r["ttfh_s"] < 0.5  # headers (and the first events) arrive immediately
    assert r["longest_gap_s"] >= 0.6  # then ~0.7 s of silence before the next bytes
    assert r["ttft_s"] >= 0.65  # the first token only arrives after the silence


def test_connection_cut_mid_stream_is_truncated():
    err = httpx.RemoteProtocolError("peer closed connection")
    res, recs = run(call(stream=True, transport=mock_transport(chunks=[event_chunk()], error=err)))
    r = res.record
    assert not res.ok and r["outcome"] == "truncated" and r["http_status"] == 200
    assert r["error_type"] == "RemoteProtocolError" and r["chunks"] == 1
    assert r["tail_silence_s"] is not None


def test_clean_close_without_completion_marker_is_truncated():
    res, _ = run(call(stream=True, transport=mock_transport(chunks=[event_chunk()])))
    assert res.record["outcome"] == "truncated"
    assert res.record["error_type"] == "StreamEndedWithoutCompletion"


def test_http_error_keeps_status_and_body():
    res, _ = run(
        call(transport=mock_transport(status=504, chunks=[b'{"error":"gateway timeout"}']))
    )
    r = res.record
    assert r["http_status"] == 504 and r["outcome"] == "http_error"
    assert "gateway timeout" in r["error_detail"]


def test_every_retry_attempt_is_a_record():
    st = settings(llm_max_attempts=3, llm_retry_backoff_s=0.01)
    res, recs = run(call(st=st, transport=mock_transport(status=503), attempts=3))
    assert [r["attempt"] for r in recs] == [1, 2, 3]
    assert all(r["http_status"] == 503 for r in recs) and not res.ok


def test_matrix_calls_never_retry():
    st = settings(llm_max_attempts=3)
    _, recs = run(call(st=st, transport=mock_transport(status=503), attempts=1))
    assert len(recs) == 1


def test_parse_usage_takes_last_object_from_sse_tail():
    tail = b'data: {"response":{"usage":null}}\n\ndata: {"response":{"usage":{"input_tokens":5,"output_tokens":9,"output_tokens_details":{"reasoning_tokens":4}}}}\n\n'
    assert parse_usage(tail) == {"prompt_tokens": 5, "completion_tokens": 9, "reasoning_tokens": 4}
    assert parse_usage(b"no usage here") == {}
    assert longest_gap([0.0, 1.0, 301.0]) == 300.0


def test_results_csv_roundtrip(tmp_path):
    p = tmp_path / "runs.csv"
    assert append_csv(p, {"label": "a", "total_s": 1.5}) and append_csv(p, {"label": "b"})
    lines = p.read_text().splitlines()
    assert lines[0].split(",") == RECORD_COLUMNS and len(lines) == 3
    assert parse_call_lines(["noise", 'x CALL {"label": "z"}'])[0]["label"] == "z"
    assert append_csv(tmp_path / "ro" / "x.csv", {}) is True


@pytest.mark.parametrize("stream", [False, True])
def test_agent_framework_agent_with_tool_loop(stream):
    searched = []

    async def search(query, domain, top):
        searched.append(query)
        return "[]"

    async def go():
        recs = []

        async def rec(r):
            recs.append(r)

        m = Model(settings(), "direct", rec, transport=asgi())
        tool = make_search_tool(search, rec, 3)
        with call_context(run_id="r", agent="network", path="direct", stream=stream):
            agent = build_agent(
                m.agent_client(), "network", "be brief", tools=[tool], max_output_tokens=100
            )
            out = await run_agent(agent, "go", stream=stream)
        await m.aclose()
        return out, recs

    out, recs = run(go())
    assert out == {"fake": True} and searched == ["vlan"]
    assert [r["kind"] for r in recs] == ["llm", "tool", "llm"]
    assert [r["turn"] for r in recs if r["kind"] == "llm"] == [1, 2]
    assert all(r["agent"] == "network" for r in recs)


def test_parse_json_variants():
    assert parse_json('```json\n{"a": 1}\n```') == {"a": 1}
    assert parse_json('Here you go: {"a": {"b": 2}} done') == {"a": {"b": 2}}
    with pytest.raises(ValueError):
        parse_json("no json")


def test_select_by_tokens_and_summarise():
    facts = [{"id": f"F{i}", "text": "x" * 400} for i in range(100)]
    assert 0 < len(select_by_tokens(facts, 1000)) < 100
    calls = [
        {"kind": "llm", "outcome": "completed", "ttfb_s": 1.0, "longest_gap_s": 5.0, "total_s": 9.0,
         "prompt_tokens": 10, "completion_tokens": 2, "reasoning_tokens": 1},
        {"kind": "llm", "outcome": "truncated", "ttfb_s": 3.0, "total_s": 4.0},
        {"kind": "tool", "total_s": 0.1},
    ]  # fmt: skip
    s = summarise(calls, 12.3)
    assert s["llm_calls"] == 2 and s["failed_calls"] == 1 and s["max_longest_gap_s"] == 5.0


@pytest.mark.parametrize("stream", [False, True])
def test_pipeline_end_to_end(stream, tmp_path):
    facts = [
        {"id": f"F{i}", "page": i, "topic": t, "section": "s", "text": f"{t} fact {i}"}
        for i, t in enumerate(["cover", "network", "addressing", "compute"] * 3)
    ]
    fp = tmp_path / "facts.jsonl"
    fp.write_text("".join(json.dumps(f) + "\n" for f in facts))
    st = settings(facts_path=str(fp))
    store = MemoryStore()

    async def fake_search(query, domain, top):
        return "[]"

    async def go():
        await store.create_run("r1", {"status": "queued"})
        cfg = RunConfig(rounds=2, stream=stream, max_output_tokens=500)
        return await execute(
            "r1",
            st,
            cfg,
            store,
            lambda rec: Model(st, "direct", rec, transport=asgi()),
            fake_search,
        )

    summary = run(go())
    assert store.runs["r1"]["status"] == "succeeded" and store.runs["r1"]["progress"] == "10/10"
    kinds = [c["kind"] for c in store.calls["r1"]]
    assert kinds.count("tool") == 8 and kinds.count("llm") == 2 * (1 + 4 * 2)
    assert summary["failed_calls"] == 0
    sections = store.outputs["r1"]["rounds"][0]["sections"]
    assert set(sections) == {"cover", "network", "addressing", "compute"}
    assert all("parse_error" not in s for s in sections.values())


def test_failed_run_is_recorded(tmp_path):
    fp = tmp_path / "f.jsonl"
    fp.write_text(
        json.dumps({"id": "F1", "page": 1, "topic": "cover", "section": "s", "text": "t"}) + "\n"
    )
    st = settings(facts_path=str(fp))
    store = MemoryStore()

    async def go():
        await store.create_run("r1", {"status": "queued"})
        make = lambda rec: Model(st, "direct", rec, transport=mock_transport(status=500))  # noqa: E731
        with pytest.raises(Exception):  # noqa: B017 - the agent framework wraps the HTTP error
            await execute("r1", st, RunConfig(max_output_tokens=100), store, make, None)

    run(go())
    assert store.runs["r1"]["status"] == "failed" and store.runs["r1"]["error"]
    assert any(c["http_status"] == 500 for c in store.calls["r1"])
