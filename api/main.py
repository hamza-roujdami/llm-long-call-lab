"""FastAPI: POST /runs starts a background worker job; GET /runs/{id} is polled by the UI."""

import csv
import io
import json
import os
import uuid
from datetime import UTC, datetime
from typing import Any, Literal

import httpx
from fastapi import Body, Depends, FastAPI, Header, HTTPException
from fastapi.responses import PlainTextResponse
from pydantic import BaseModel, Field

app = FastAPI(title="apim-timeout-lab api")

ARM = "https://management.azure.com"
ARM_API_VERSION = "2024-03-01"


class MemoryStore:
    def __init__(self) -> None:
        self.runs: dict[str, dict[str, Any]] = {}
        self.calls: dict[str, list[dict[str, Any]]] = {}
        self.outputs: dict[str, dict[str, Any]] = {}

    async def create_run(self, run_id, fields):
        self.runs[run_id] = {"id": run_id, **fields}

    async def update_run(self, run_id, **fields):
        self.runs.setdefault(run_id, {"id": run_id}).update(fields)

    async def add_call(self, run_id, rec):
        self.calls.setdefault(run_id, []).append(rec)

    async def put_output(self, run_id, data):
        self.outputs[run_id] = data

    async def get_run(self, run_id):
        return self.runs.get(run_id)

    async def list_runs(self, limit=25):
        return sorted(self.runs.values(), key=lambda r: r.get("created_utc", ""), reverse=True)[
            :limit
        ]

    async def list_calls(self, run_id):
        return self.calls.get(run_id, [])

    async def get_output(self, run_id):
        return self.outputs.get(run_id)


async def start_job(credential, run_id: str) -> str:
    """Start the worker as a Container Apps Job execution through ARM."""
    job_id = os.environ["JOB_RESOURCE_ID"]
    # An execution override replaces the container definition, so the full env is passed each time.
    env = json.loads(os.environ.get("WORKER_ENV_JSON", "[]")) + [
        {"name": "RUN_ID", "value": run_id}
    ]
    body = {
        "containers": [
            {
                "name": os.environ.get("WORKER_CONTAINER", "worker"),
                "image": os.environ["WORKER_IMAGE"],
                "env": env,
                "resources": {"cpu": 1.0, "memory": "2Gi"},
            }
        ]
    }
    token = (await credential.get_token(f"{ARM}/.default")).token
    async with httpx.AsyncClient(timeout=60) as http:
        r = await http.post(
            f"{ARM}{job_id}/start?api-version={ARM_API_VERSION}",
            json=body,
            headers={"Authorization": f"Bearer {token}"},
        )
    if r.status_code >= 300:
        raise RuntimeError(f"job start failed: {r.status_code} {r.text[:300]}")
    return (r.json().get("name") or r.headers.get("location", "")) if r.content else ""


CALL_COLUMNS = [
    "ts_utc", "run_id", "label", "round", "agent", "turn", "attempt", "kind", "path", "stream",
    "input_bytes", "http_status", "outcome", "error_type", "error_detail",
    "ttfh_s", "ttfb_s", "ttft_s", "longest_gap_s", "last_chunk_s", "tail_silence_s", "total_s",
    "chunks", "bytes", "prompt_tokens", "completion_tokens", "reasoning_tokens",
    "request_ids", "client_request_id",
]  # fmt: skip


class RunRequest(BaseModel):
    """Mirrors worker.config.RunConfig (validated again by the worker)."""

    path: Literal["direct", "apim-default", "apim-stream"] = "direct"
    stream: bool = True
    reasoning_effort: Literal["none", "minimal", "low", "medium", "high"] = "high"
    fact_tokens: int = Field(80_000, ge=1_000, le=400_000)
    section_fact_tokens: int = Field(20_000, ge=1_000, le=100_000)
    rounds: int = Field(1, ge=1, le=20)
    max_tool_calls: int = Field(3, ge=0, le=10)
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
    await start_job(_cred, run_id)


def summarise(calls: list[dict[str, Any]]) -> dict[str, Any]:
    llm = [c for c in calls if c.get("kind") == "llm"]

    def peak(k: str):
        vals = [c[k] for c in llm if c.get(k) is not None]
        return max(vals) if vals else None

    return {
        "llm_calls": len(llm),
        "failed_calls": sum(1 for c in llm if c.get("outcome") != "completed"),
        "max_ttfb_s": peak("ttfb_s"),
        "max_ttft_s": peak("ttft_s"),
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
