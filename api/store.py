"""Run state held by the api (single replica). The durable record of every call is also the
worker's console log in Log Analytics (`CALL {json}` lines); export CSVs from results via /runs/{id}/calls.csv."""

from typing import Any


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
