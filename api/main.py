"""FastAPI: POST /runs starts a background worker job; GET /runs/{id} is polled by the UI."""

import csv
import io
import json
import os
import uuid
from datetime import UTC, datetime
from typing import Any, Literal

from fastapi import Body, Depends, FastAPI, Header, HTTPException
from fastapi.responses import PlainTextResponse
from pydantic import BaseModel, Field

from api import jobs
from api.store import MemoryStore

app = FastAPI(title="apim-timeout-lab api")

CALL_COLUMNS = [
    "run_id", "ts_utc", "kind", "round", "agent", "turn", "attempt", "path", "gateway_variant", "stream", "api",
    "reasoning_effort", "http_status", "outcome", "error_type", "error_detail", "ttfh_s", "ttfb_s",
    "longest_gap_s", "last_chunk_s", "total_s", "chunks", "input_chars", "prompt_tokens",
    "completion_tokens", "reasoning_tokens", "client_request_id", "request_ids",
]  # fmt: skip


class RunRequest(BaseModel):
    """Mirrors worker.config.RunConfig (validated again by the worker)."""

    path: Literal["direct", "gateway"] = "direct"
    gateway_variant: Literal["default", "stream"] = "stream"
    stream: bool = True
    api: Literal["responses", "chat"] = "responses"
    reasoning_effort: Literal["none", "minimal", "low", "medium", "high"] = "high"
    fact_tokens: int = Field(80_000, ge=1_000, le=400_000)
    section_fact_tokens: int = Field(20_000, ge=1_000, le=100_000)
    rounds: int = Field(1, ge=1, le=20)
    max_tool_turns: int = Field(2, ge=0, le=5)
    max_output_tokens: int = Field(16_000, ge=256, le=128_000)
    depth: Literal["normal", "exhaustive"] = "normal"
    note: str = Field("", max_length=200)


_store = MemoryStore()
_cred: Any = None


def get_store() -> MemoryStore:
    return _store


def require_internal(x_internal_token: str | None = Header(default=None)) -> None:
    expected = os.environ.get("INTERNAL_TOKEN", "")
    if not expected or x_internal_token != expected:
        raise HTTPException(401, "invalid internal token")


async def start_worker(run_id: str) -> None:
    global _cred
    if os.environ.get("STORE_MODE") == "memory":
        return
    if _cred is None:
        from azure.identity.aio import DefaultAzureCredential

        _cred = DefaultAzureCredential()
    await jobs.start_worker(_cred, run_id)


def summarise(calls: list[dict[str, Any]]) -> dict[str, Any]:
    llm = [c for c in calls if c.get("kind") == "llm"]

    def peak(k: str):
        vals = [c[k] for c in llm if c.get(k) is not None]
        return max(vals) if vals else None

    return {
        "llm_calls": len(llm),
        "failed_calls": sum(1 for c in llm if c.get("outcome") != "completed"),
        "max_ttfb_s": peak("ttfb_s"),
        "max_longest_gap_s": peak("longest_gap_s"),
        "max_call_total_s": peak("total_s"),
        "prompt_tokens": sum(c.get("prompt_tokens") or 0 for c in llm),
        "completion_tokens": sum(c.get("completion_tokens") or 0 for c in llm),
        "reasoning_tokens": sum(c.get("reasoning_tokens") or 0 for c in llm),
    }


@app.get("/health")
async def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/runs", status_code=202)
async def create_run(req: RunRequest, store=Depends(get_store)) -> dict[str, str]:
    now = datetime.now(UTC)
    run_id = f"{now:%Y%m%d-%H%M%S}-{uuid.uuid4().hex[:4]}"
    await store.create_run(
        run_id,
        {
            "status": "queued",
            "created_utc": now.isoformat(timespec="seconds"),
            "config_json": req.model_dump_json(),
            "note": req.note,
            "phase": "queued",
        },
    )
    try:
        await start_worker(run_id)
    except Exception as e:  # noqa: BLE001
        await store.update_run(run_id, status="failed", error=f"could not start worker: {e}"[:500])
        raise HTTPException(502, f"could not start worker: {e}") from e
    return {"run_id": run_id}


@app.get("/runs")
async def list_runs(store=Depends(get_store)) -> list[dict[str, Any]]:
    return await store.list_runs()


@app.get("/runs/{run_id}")
async def get_run(run_id: str, store=Depends(get_store)) -> dict[str, Any]:
    run = await store.get_run(run_id)
    if run is None:
        raise HTTPException(404, "run not found")
    calls = await store.list_calls(run_id)
    return {**run, "calls": calls, "live_summary": summarise(calls)}


@app.get("/runs/{run_id}/calls.csv", response_class=PlainTextResponse)
async def calls_csv(run_id: str, store=Depends(get_store)) -> PlainTextResponse:
    calls = await store.list_calls(run_id)
    buf = io.StringIO()
    w = csv.DictWriter(buf, fieldnames=CALL_COLUMNS, extrasaction="ignore")
    w.writeheader()
    w.writerows(calls)
    return PlainTextResponse(buf.getvalue(), media_type="text/csv")


@app.get("/runs/{run_id}/output")
async def get_output(run_id: str, store=Depends(get_store)) -> Any:
    out = await store.get_output(run_id)
    if out is None:
        raise HTTPException(404, "no output (yet)")
    return json.loads(json.dumps(out))


# Worker -> api callbacks (internal ingress only, plus a shared token).
@app.post("/internal/runs/{run_id}/update", dependencies=[Depends(require_internal)])
async def internal_update(
    run_id: str, fields: dict[str, Any] = Body(...), store=Depends(get_store)
) -> dict:
    await store.update_run(run_id, **fields)
    return {"ok": True}


@app.post("/internal/runs/{run_id}/calls", dependencies=[Depends(require_internal)])
async def internal_call(
    run_id: str, rec: dict[str, Any] = Body(...), store=Depends(get_store)
) -> dict:
    await store.add_call(run_id, rec)
    return {"ok": True}


@app.put("/internal/runs/{run_id}/output", dependencies=[Depends(require_internal)])
async def internal_output(
    run_id: str, data: dict[str, Any] = Body(...), store=Depends(get_store)
) -> dict:
    await store.put_output(run_id, data)
    return {"ok": True}
