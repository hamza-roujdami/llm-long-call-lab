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
    """Synthetic facts are generated, not committed: build a small copy for the tests."""
    root = Path(__file__).resolve().parents[2]
    spec = importlib.util.spec_from_file_location(
        "gen", root / "data" / "generate_synthetic_docs.py"
    )
    gen = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(gen)
    facts, _, _ = gen.generate(pages=20, seed=42)
    path = Path(tempfile.mkdtemp()) / "facts.jsonl"
    path.write_text("".join(json.dumps(f) + "\n" for f in facts))
    os.environ["FACTS_PATH"] = str(path)


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
