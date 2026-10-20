"""Start the worker as a Container Apps Job execution through ARM."""

import json
import os

import httpx

ARM = "https://management.azure.com"
API_VERSION = "2024-03-01"


async def start_worker(credential, run_id: str) -> str:
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
            f"{ARM}{job_id}/start?api-version={API_VERSION}",
            json=body,
            headers={"Authorization": f"Bearer {token}"},
        )
    if r.status_code >= 300:
        raise RuntimeError(f"job start failed: {r.status_code} {r.text[:300]}")
    return (r.json().get("name") or r.headers.get("location", "")) if r.content else ""
