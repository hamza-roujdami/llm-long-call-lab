"""Planner and section agents, built on Microsoft Agent Framework (Agent + function tool).

The prompts are generic and written for this lab; they are not copied from any customer.
"""

import asyncio
import json
import re
from collections.abc import Awaitable, Callable
from typing import Any

from agent_framework import Agent

from worker.llm_client import current_context

# --- Prompts: generic, written for this lab (nothing copied from any customer) ---------------------

SHEET_TYPES = {
    "cover": "cover",
    "firewall_rules": "network",
    "ip_routing": "network",
    "lb_rules": "network",
    "subnets": "addressing",
    "certificates": "addressing",
    "compute_vms": "compute",
}  # sheet_type -> owner agent

PLANNER_NORMAL = (
    "You are the planning agent that turns a high-level design (HLD) into a low-level design workbook. "
    "You decide WHICH sheets the workbook needs for this engagement and nothing else; you write no cell content. "
    "The input envelope has engagement_id, scope_inventory and facts[]: a starting slice of the HLD, each fact "
    "being {id, content, filename, page_number, section_path, chunk_type: prose|table|iac}. "
    "facts[] is NOT the whole HLD. You have ONE tool, ai_search(query, domain?, top?), which searches the whole HLD "
    "and returns whole chunks. BEFORE you finalise the plan, search for what facts[] may be missing: the segment (VLAN) "
    "table, the cluster role table with host counts, the subscription table. Take segment names, VLAN ids, CIDRs and "
    "host counts ONLY from facts[] or ai_search results; never invent a value. "
    "Sheet types and owners: cover->cover; firewall_rules, ip_routing, lb_rules->network; subnets, certificates->addressing; "
    "compute_vms->compute (one per compute segment). The list is derived, not fixed: emit a sheet only for a construct "
    "the HLD supports and record the rest in omitted_candidates with a reason. Cover is always present, order 1. "
    "Every non-cover section needs non-empty source_chunks citing filename and page_number. "
    "Reply with ONE JSON object only, no prose, no code fences: "
    '{"engagement_id": string, "sections": [{"section_id": string, "sheet_name": string, "sheet_type": string, '
    '"owner_agent": "cover|network|addressing|compute", "order": number, "scope_ref": string|null, '
    '"mandatory": boolean, "rationale": string, "source_chunks": [{"filename": string, "page_number": number}]}], '
    '"omitted_candidates": [{"sheet_name": string, "reason": string}], "warnings": [string], '
    '"detected_vlans": [{"id": string, "name": string, "cidr": string|null, "platform": string, '
    '"evidence": {"filename": string, "page_number": number, "quote": string}}], '
    '"has_bgp": boolean, "has_nat": boolean}.'
)

# Long-call workload: one review entry per input fact makes a single answer run for minutes, so streamed
# calls stay busy for several minutes and non-streamed calls stay silent just as long.
PLANNER_EXHAUSTIVE = (
    PLANNER_NORMAL
    + " ADDITIONALLY add a top-level array chunk_reviews with EXACTLY ONE entry for EVERY fact in the input, in"
    ' input order: {"id": string, "ok": boolean, "note": string of 25 to 35 words explaining whether the chunk is'
    " consistent with the other chunks, naming at least two related chunk ids}. The input states fact_count;"
    " chunk_reviews MUST contain exactly fact_count entries. An answer with fewer entries is INVALID and will be"
    " discarded. Never abbreviate, never use ellipses, never write 'etc.'."
)

_CONTENT_SCHEMA = (
    'Reply with ONE JSON object only: {"sheets": [{"section_id": string, "sheet_name": string, '
    '"columns": [string], "rows": [[string]], "notes": string}], "issues": [string]}. '
    "Produce one sheet per assigned section, with one row per documented item. Take every value from facts[] or "
    "ai_search results; cite page numbers in notes; leave a cell empty rather than invent it. "
    "Use the ai_search tool to verify at least one detail before answering."
)

_FOCUS = {
    "cover": "document control, scope, requirements and assumptions",
    "network": "firewall rules, IP routing and load-balancer rules",
    "addressing": "subnets, DHCP scopes, NAT pools and certificates",
    "compute": "clusters, virtual machines per segment, datastores and backup tiers",
}

CONTENT_INSTRUCTIONS = {
    topic: (
        f"You are the {topic} content agent of an LLD workbook, covering {focus}. "
        "You receive engagement_id, the sections the planner assigned to you (sections[]) and the relevant facts[] "
        "(each {id, content, filename, page_number, section_path, chunk_type}). " + _CONTENT_SCHEMA
    )
    for topic, focus in _FOCUS.items()
}

# Domain of each chunk -> content agent that reads it.
DOMAIN_OWNER = {
    "cover": "cover",
    "network": "network",
    "addressing": "addressing",
    "security": "addressing",
    "compute": "compute",
}


def parse_json(text: str) -> dict[str, Any]:
    """Models sometimes wrap JSON in code fences or prose; take the outermost object."""
    text = re.sub(r"^```(?:json)?|```$", "", text.strip(), flags=re.MULTILINE).strip()
    start, end = text.find("{"), text.rfind("}")
    if start < 0 or end < start:
        raise ValueError("no JSON object in model output")
    return json.loads(text[start : end + 1])


def build_agent(
    client: Any,
    name: str,
    instructions: str | None,
    *,
    tools: list[Any] | None = None,
    reasoning_effort: str = "high",
    max_output_tokens: int,
) -> Agent:
    options: dict[str, Any] = {"max_tokens": max_output_tokens}
    if reasoning_effort and reasoning_effort != "none":
        options["reasoning"] = {"effort": reasoning_effort}
    return Agent(
        client,
        instructions,
        id=f"lab-{name}",
        name=name,
        tools=tools or None,
        default_options=options,
    )


async def run_agent(agent: Agent, payload: str, *, stream: bool) -> dict[str, Any]:
    """Run one agent (streaming or not) and parse its JSON answer."""
    current_context().agent = agent.name or ""
    if stream:
        updates = agent.run(payload, stream=True)
        async for _ in updates:
            pass
        response = await updates.get_final_response()
    else:
        response = await agent.run(payload)
    try:
        return parse_json(response.text)
    except ValueError as e:
        return {"parse_error": str(e), "raw": response.text[:2000]}


async def with_retries(
    fn: Callable[[], Awaitable[dict[str, Any]]],
    *,
    attempts: int,
    backoff_s: float,
    on_retry: Callable[[int, Exception], Awaitable[None]] | None = None,
) -> dict[str, Any]:
    """Re-run a whole agent when it fails (pipeline mode only; the matrix never retries).

    Needed because a rate-limit error can arrive INSIDE a stream after HTTP 200 (observed), where an
    HTTP-level retry cannot see it. Waits backoff_s * attempt between tries.
    """
    for attempt in range(1, max(1, attempts) + 1):
        try:
            return await fn()
        except Exception as e:  # noqa: BLE001 - cancellation is a BaseException and passes through
            if attempt >= attempts:
                raise
            if on_retry:
                await on_retry(attempt, e)
            await asyncio.sleep(backoff_s * attempt)
    raise RuntimeError("unreachable")
