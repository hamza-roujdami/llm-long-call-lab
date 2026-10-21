"""Run state and per-call telemetry: reported to the api (which holds it), or in memory for tests."""

import asyncio
from datetime import UTC, datetime
from typing import Any, Protocol

from worker.config import Settings


def now_utc() -> str:
    return datetime.now(UTC).isoformat(timespec="seconds")


class Store(Protocol):
    async def get_run(self, run_id: str) -> dict[str, Any] | None: ...
    async def create_run(self, run_id: str, fields: dict[str, Any]) -> None: ...
    async def update_run(self, run_id: str, **fields: Any) -> None: ...
    async def add_call(self, run_id: str, seq: int, rec: dict[str, Any]) -> None: ...
    async def put_output(self, run_id: str, data: dict[str, Any]) -> None: ...
    async def put_file(self, run_id: str, name: str, data: bytes) -> None: ...
    async def close(self) -> None: ...


def _clean(d: dict[str, Any]) -> dict[str, Any]:
    """Table entities reject None and non-scalar values."""
    return {k: v for k, v in d.items() if v is not None and isinstance(v, str | int | float | bool)}


class MemoryStore:
    def __init__(self) -> None:
        self.runs: dict[str, dict[str, Any]] = {}
        self.calls: dict[str, list[dict[str, Any]]] = {}
        self.outputs: dict[str, dict[str, Any]] = {}
        self.files: dict[str, dict[str, bytes]] = {}

    async def get_run(self, run_id):
        return self.runs.get(run_id)

    async def create_run(self, run_id, fields):
        self.runs[run_id] = dict(fields)

    async def update_run(self, run_id, **fields):
        self.runs.setdefault(run_id, {}).update(fields)

    async def add_call(self, run_id, seq, rec):
        self.calls.setdefault(run_id, []).append(dict(rec))

    async def put_output(self, run_id, data):
        self.outputs[run_id] = data

    async def put_file(self, run_id, name, data):
        self.files.setdefault(run_id, {})[name] = data

    async def close(self) -> None:
        return None


class HttpStore:
    """Reports run state to the api (internal ingress). Callbacks never fail the run."""

    def __init__(self, base_url: str, token: str) -> None:
        import httpx

        self._http = httpx.AsyncClient(
            base_url=base_url.rstrip("/"), headers={"x-internal-token": token}, timeout=30
        )

    async def _send(self, method: str, url: str, body: Any) -> None:
        for attempt in range(3):
            try:
                r = await self._http.request(method, url, json=body)
                r.raise_for_status()
                return
            except Exception as e:  # noqa: BLE001 - telemetry must not break the run
                if attempt == 2:
                    print(f"WARN store {method} {url} failed: {type(e).__name__}: {e}", flush=True)
                await asyncio.sleep(1 + attempt)

    async def get_run(self, run_id):
        r = await self._http.get(f"/runs/{run_id}")
        return r.json() if r.status_code == 200 else None

    async def create_run(self, run_id, fields):
        raise NotImplementedError("runs are created by the api")

    async def update_run(self, run_id, **fields):
        await self._send("POST", f"/internal/runs/{run_id}/update", _clean(fields))

    async def add_call(self, run_id, seq, rec):
        await self._send("POST", f"/internal/runs/{run_id}/calls", _clean(rec))

    async def put_output(self, run_id, data):
        await self._send("PUT", f"/internal/runs/{run_id}/output", data)

    async def put_file(self, run_id, name, data):
        for attempt in range(3):
            try:
                r = await self._http.put(f"/internal/runs/{run_id}/files/{name}", content=data)
                r.raise_for_status()
                return
            except Exception as e:  # noqa: BLE001 - artifacts must not fail the run
                if attempt == 2:
                    print(f"WARN store put_file {name} failed: {type(e).__name__}: {e}", flush=True)
                await asyncio.sleep(1 + attempt)

    async def close(self) -> None:
        await self._http.aclose()


def make_store(st: Settings) -> Store:
    if st.store_mode == "memory":
        return MemoryStore()
    return HttpStore(st.api_url, st.internal_token)
