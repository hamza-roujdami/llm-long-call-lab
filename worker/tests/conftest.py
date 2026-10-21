import importlib.util
import json
import os
import socket
import tempfile
import threading
import time
from pathlib import Path

import pytest
import uvicorn

from worker.tests import fake_model


def _generate_facts() -> None:
    """Synthetic HLD chunks are generated, not committed: build a small copy for the tests."""
    root = Path(__file__).resolve().parents[2]
    spec = importlib.util.spec_from_file_location(
        "gen", root / "data" / "generate_synthetic_docs.py"
    )
    gen = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(gen)
    chunks = gen.generate(slice_chunks=24, extra_chunks=6, seed=42)
    path = Path(tempfile.mkdtemp()) / "hld.jsonl"
    path.write_text("".join(json.dumps(c) + "\n" for c in chunks))
    os.environ["FACTS_PATH"] = str(path)


# Hermetic: a developer's .env (retries, pacing, endpoints) must never change test behaviour.
for _k, _v in {
    "LLM_MAX_ATTEMPTS": "1", "LLM_RETRY_BACKOFF_S": "5", "LLM_TPM_BUDGET": "0", "LLM_BASE_URL_OVERRIDE": "",
    "APIM_URL": "", "APIM_KEY": "", "FOUNDRY_ENDPOINT": "", "SEARCH_ENDPOINT": "",
    "APPLICATIONINSIGHTS_CONNECTION_STRING": "",
}.items():  # fmt: skip
    os.environ[_k] = _v

_generate_facts()


@pytest.fixture
def live_fake():
    """Real uvicorn server for the fake model: the in-process ASGI transport buffers whole
    responses, which would hide silent gaps."""
    with socket.socket() as sock:
        sock.bind(("127.0.0.1", 0))
        port = sock.getsockname()[1]
    server = uvicorn.Server(
        uvicorn.Config(fake_model.app, host="127.0.0.1", port=port, log_level="error")
    )
    thread = threading.Thread(target=server.run, daemon=True)
    thread.start()
    while not server.started:
        time.sleep(0.05)
    yield f"http://127.0.0.1:{port}/v1"
    server.should_exit = True
    thread.join(timeout=5)
    fake_model.FIRST_DELAY = 0.0
