"""Planner and section agents, built on Microsoft Agent Framework (Agent + function tool).

The prompts are generic and written for this lab; they are not copied from any customer.
"""

import json
import re
from typing import Any

from agent_framework import Agent

from worker.llm_client import current_context

PLANNER_NORMAL = (
    "You are the planning agent for converting a high-level design (HLD) into a low-level design. "
    "You receive facts[] extracted from the HLD (each has id, page, topic, section, text). "
    "Analyse ALL facts, detect conflicts or gaps, and produce a work plan for four section agents: "
    "cover, network, addressing, compute. "
    'Reply with ONE JSON object only: {"sections":[{"agent":"cover|network|addressing|compute",'
    '"objectives":[string],"key_fact_ids":[string],"risks":[string]}],'
    '"conflicts":[{"fact_ids":[string],"description":string}],"open_questions":[string]}. '
    "Keep key_fact_ids to at most 25 per section."
)

# Long-call workload: one verdict per input fact makes a single answer run for minutes, so streamed
# calls stay busy for several minutes and non-streamed calls stay silent just as long.
PLANNER_EXHAUSTIVE = (
    PLANNER_NORMAL
    + " ADDITIONALLY add a top-level array fact_checks with EXACTLY ONE entry for EVERY fact in the"
    ' input, in input order: {"id": string, "ok": boolean, "note": string of 25 to 35 words explaining'
    " whether the fact is consistent with the other facts, naming at least two related fact ids}."
    " The input states fact_count; fact_checks MUST contain exactly fact_count entries. An answer with"
    " fewer entries is INVALID and will be discarded. Never abbreviate, never use ellipses, never"
    " write 'etc.'."
)

_SCHEMA = (
    'Reply with ONE JSON object only: {"section": string, "summary": string, '
    '"tables":[{"title":string,"columns":[string],"rows":[[string]]}], '
    '"findings":[{"fact_ids":[string],"text":string}], "issues":[string]}. '
    "Use the ai_search tool to verify at least one detail before answering, and cite page numbers."
)

_FOCUS = {
    "cover": "document control, scope, requirements and assumptions",
    "network": "VLANs, routing and BGP peering, firewall policy and load balancing",
    "addressing": "IPv4 supernets, subnets, DHCP scopes and NAT pools",
    "compute": "clusters, workload placement, datastores and backup tiers",
}

SECTION_INSTRUCTIONS = {
    topic: (
        f"You are the {topic} section agent writing the low-level design section on {focus}. "
        "You receive the planner's instructions for your section and the relevant facts[]. "
        "Produce concise tables and findings; flag inconsistencies as issues. " + _SCHEMA
    )
    for topic, focus in _FOCUS.items()
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
    instructions: str,
    *,
    tools: list[Any] | None = None,
    reasoning_effort: str = "high",
    max_output_tokens: int,
) -> Agent:
    options: dict[str, Any] = {"max_tokens": max_output_tokens}
    if reasoning_effort and reasoning_effort != "none":
        options["reasoning"] = {"effort": reasoning_effort}
    return Agent(client, instructions, name=name, tools=tools or None, default_options=options)


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
