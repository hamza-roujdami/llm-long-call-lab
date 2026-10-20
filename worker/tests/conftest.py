import socket
import threading
import time

import pytest
import uvicorn

from worker.tests import fake_model


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
