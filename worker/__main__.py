"""Entry point of the worker container.

  python -m worker                                   HLD->LLD agent pipeline for RUN_ID (started by the api)
  python -m worker matrix max-output-tokens=N ...    long-call matrix (see run_matrix.py)

Matrix options may be written without dashes (`confirm-spend`, `repeat=2`), because `az containerapp job
start --args` cannot pass arguments that begin with a dash.
"""

import asyncio
import json
import sys
import uuid

from worker.config import RunConfig, Settings
from worker.llm_client import Model
from worker.orchestrator import execute
from worker.search_tool import DocSearch
from worker.store import make_store, now_utc


async def pipeline() -> int:
    st = Settings()
    credential = None
    if st.search_endpoint:
        from azure.identity.aio import DefaultAzureCredential

        credential = DefaultAzureCredential()
    store = make_store(st)
    run_id = st.run_id or f"local-{uuid.uuid4().hex[:8]}"
    try:
        run = await store.get_run(run_id)
        if run is None:  # local/memory mode: create the run from RUN_CONFIG_JSON
            await store.create_run(
                run_id,
                {
                    "status": "queued",
                    "created_utc": now_utc(),
                    "config_json": st.run_config_json or "{}",
                },
            )
            run = await store.get_run(run_id)
        cfg = RunConfig(**json.loads(run.get("config_json") or "{}"))
        search = (
            DocSearch(st.search_endpoint, st.search_index, credential)
            if st.search_endpoint
            else None
        )

        def make_model(recorder):
            return Model(st, cfg.path, recorder, run_id=run_id)

        try:
            summary = await execute(run_id, st, cfg, store, make_model, search)
        finally:
            if search:
                await search.aclose()
        print("SUMMARY " + json.dumps(summary), flush=True)
        return 0
    except Exception as e:  # noqa: BLE001
        print(f"RUN FAILED: {type(e).__name__}: {e}", file=sys.stderr, flush=True)
        return 1
    finally:
        await store.close()
        if credential:
            await credential.close()


def matrix_argv(tokens: list[str]) -> list[str]:
    """`confirm-spend repeat=2` -> `--confirm-spend --repeat 2` (dashes optional)."""
    out: list[str] = []
    for t in tokens:
        key, sep, value = t.lstrip("-").partition("=")
        out.append(f"--{key}")
        if sep:
            out.append(value)
    return out


if __name__ == "__main__":
    if sys.argv[1:2] == ["matrix"]:
        from worker.run_matrix import amain, parse_args

        sys.exit(asyncio.run(amain(parse_args(matrix_argv(sys.argv[2:])))))
    sys.exit(asyncio.run(pipeline()))
