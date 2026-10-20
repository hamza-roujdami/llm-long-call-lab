"""Entry point: `python -m worker` runs the run named by RUN_ID (Container Apps Job)."""

import asyncio
import json
import sys
import uuid

from worker.config import RunConfig, Settings
from worker.llm_client import LLMClient
from worker.orchestrator import execute
from worker.store import make_store, now_utc
from worker.tools.doc_search import DocSearch


async def amain() -> int:
    st = Settings()
    credential = None
    if st.search_endpoint or (st.foundry_endpoint and not st.direct_base_url_override):
        from azure.identity.aio import DefaultAzureCredential

        credential = DefaultAzureCredential()  # AZURE_CLIENT_ID selects the user-assigned identity
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
        try:
            summary = await execute(run_id, st, cfg, store, LLMClient_factory(credential), search)
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


def LLMClient_factory(credential):  # noqa: N802 - tiny closure, named like the class it builds
    def make(st, cfg, run_id, recorder):
        return LLMClient(st, cfg, run_id, recorder, credential=credential)

    return make


if __name__ == "__main__":
    sys.exit(asyncio.run(amain()))
