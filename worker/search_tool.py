"""ai_search tool: keyword search over the synthetic design document in Azure AI Search.

Shape mirrors a typical RAG tool: ai_search(query, domain?, top?) returns whole page chunks with page
number and section path. Exposed to Microsoft Agent Framework agents as a function tool.
"""

import json
import time
from collections.abc import Awaitable, Callable
from typing import Annotated, Any

import httpx
from agent_framework import tool
from pydantic import Field

from worker.llm_client import Recorder, _noop, current_context

SEARCH_SCOPE = "https://search.azure.com/.default"
API_VERSION = "2024-07-01"
DOMAINS = ("cover", "network", "addressing", "compute")

SearchFn = Callable[[str, str | None, int], Awaitable[str]]


class DocSearch:
    def __init__(self, endpoint: str, index: str, credential) -> None:
        self.url = f"{endpoint.rstrip('/')}/indexes/{index}/docs/search?api-version={API_VERSION}"
        self.cred = credential
        self.http = httpx.AsyncClient(timeout=60)

    async def __call__(self, query: str, domain: str | None = None, top: int = 5) -> str:
        token = (await self.cred.get_token(SEARCH_SCOPE)).token
        body: dict[str, Any] = {
            "search": query,
            "top": max(1, min(int(top), 10)),
            "select": "page,topic,title,content",
            "queryType": "simple",
        }
        if domain in DOMAINS:
            body["filter"] = f"topic eq '{domain}'"
        r = await self.http.post(self.url, json=body, headers={"Authorization": f"Bearer {token}"})
        r.raise_for_status()
        return json.dumps(
            [
                {
                    "page_number": h["page"],
                    "section_path": h["title"],
                    "domain": h["topic"],
                    "chunk": h["content"][:1500],
                }
                for h in r.json().get("value", [])
            ]
        )

    async def aclose(self) -> None:
        await self.http.aclose()


def make_search_tool(search: SearchFn, recorder: Recorder = _noop, max_calls: int = 3):
    """Wrap a search function as an Agent Framework tool that also records its own timing."""

    @tool(
        name="ai_search",
        description=(
            "Search the high-level design document with Azure AI Search. Returns whole page chunks "
            "with page_number and section_path. Use it to verify a detail or find supporting evidence."
        ),
        max_invocations=max_calls,
    )
    async def ai_search(
        query: Annotated[str, Field(description="what to find, in plain words")],
        domain: Annotated[
            str | None, Field(description="optional: cover|network|addressing|compute")
        ] = None,
        top: Annotated[int, Field(description="results to return, 1-10 (default 5)")] = 5,
    ) -> str:
        ctx = current_context()
        t0, err = time.monotonic(), ""
        try:
            return await search(query, domain, top)
        except Exception as e:  # noqa: BLE001 - the model gets the error text, the run keeps going
            err = type(e).__name__
            return json.dumps({"error": f"{type(e).__name__}: {e}"[:300]})
        finally:
            await recorder(
                {
                    "kind": "tool",
                    "run_id": ctx.run_id,
                    "label": ctx.label,
                    "round": ctx.round_no,
                    "agent": ctx.agent,
                    "path": "ai_search",
                    "total_s": round(time.monotonic() - t0, 3),
                    "outcome": "error" if err else "completed",
                    "error_type": err,
                }
            )

    return ai_search
