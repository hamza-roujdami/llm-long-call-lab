"""ai_search tool: keyword search over the synthetic design document in Azure AI Search."""

import json
import time
from collections.abc import Awaitable, Callable
from typing import Any

import httpx

SEARCH_SCOPE = "https://search.azure.com/.default"
API_VERSION = "2024-07-01"

TOOL_SPEC: dict[str, Any] = {
    "type": "function",
    "function": {
        "name": "ai_search",
        "description": (
            "Search the high-level design document. Returns up to 3 matching pages with page number, "
            "section and a text excerpt. Use it to verify a detail or find supporting evidence."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "keywords, e.g. 'BGP max-prefix core-3'",
                },
                "topic": {
                    "type": "string",
                    "enum": ["cover", "network", "addressing", "compute"],
                    "description": "optional topic filter",
                },
            },
            "required": ["query"],
        },
    },
}

SearchFn = Callable[[str, str | None], Awaitable[str]]


class DocSearch:
    def __init__(self, endpoint: str, index: str, credential) -> None:
        self.url = f"{endpoint.rstrip('/')}/indexes/{index}/docs/search?api-version={API_VERSION}"
        self.cred = credential
        self.http = httpx.AsyncClient(timeout=60)

    async def __call__(self, query: str, topic: str | None = None) -> str:
        token = (await self.cred.get_token(SEARCH_SCOPE)).token
        body: dict[str, Any] = {
            "search": query,
            "top": 3,
            "select": "page,topic,title,content",
            "queryType": "simple",
        }
        if topic:
            body["filter"] = f"topic eq '{topic}'"
        r = await self.http.post(self.url, json=body, headers={"Authorization": f"Bearer {token}"})
        r.raise_for_status()
        hits = [
            {"page": h["page"], "section": h["title"], "excerpt": h["content"][:600]}
            for h in r.json().get("value", [])
        ]
        return json.dumps(hits)

    async def aclose(self) -> None:
        await self.http.aclose()


async def run_tool(search: SearchFn, arguments: str) -> tuple[str, float, str]:
    """Execute one ai_search call. Returns (tool message content, seconds, error)."""
    t0 = time.monotonic()
    try:
        args = json.loads(arguments or "{}")
        out = await search(str(args.get("query", "")), args.get("topic"))
        return out, time.monotonic() - t0, ""
    except Exception as e:  # noqa: BLE001 - the model gets the error text, the run keeps going
        return (
            json.dumps({"error": f"{type(e).__name__}: {e}"[:300]}),
            time.monotonic() - t0,
            type(e).__name__,
        )
