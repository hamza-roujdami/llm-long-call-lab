"""Planner and section agents, built on Microsoft Agent Framework (Agent + function tool).

The prompts are generic and written for this lab; they are not copied from any customer.
"""

import json
import re
from typing import Any

from agent_framework import Agent

from worker.agents.planner import PLANNER_EXHAUSTIVE, PLANNER_NORMAL
from worker.agents.section import SECTION_INSTRUCTIONS
from worker.llm_client import current_context

__all__ = [
    "PLANNER_EXHAUSTIVE",
    "PLANNER_NORMAL",
    "SECTION_INSTRUCTIONS",
    "build_agent",
    "run_agent",
]


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
