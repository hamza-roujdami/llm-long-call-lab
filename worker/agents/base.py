"""Minimal agent: a system prompt, a JSON answer, and an optional ai_search tool loop."""

import json
import re
from dataclasses import dataclass
from typing import Any

from worker.llm_client import LLMClient
from worker.tools.doc_search import TOOL_SPEC, SearchFn, run_tool


def parse_json(text: str) -> dict[str, Any]:
    """Models sometimes wrap JSON in code fences or prose; take the outermost object."""
    text = re.sub(r"^```(?:json)?|```$", "", text.strip(), flags=re.MULTILINE).strip()
    start, end = text.find("{"), text.rfind("}")
    if start < 0 or end < start:
        raise ValueError("no JSON object in model output")
    return json.loads(text[start : end + 1])


@dataclass
class Agent:
    name: str
    system: str
    use_search: bool = False

    async def run(
        self,
        llm: LLMClient,
        payload: str,
        *,
        search: SearchFn | None,
        record_tool,
        max_tool_turns: int,
        round_no: int,
    ) -> dict[str, Any]:
        conv = llm.conversation(self.name, self.system, round_no)
        tools_on = [TOOL_SPEC] if (self.use_search and search) else None
        res = await conv.ask(payload, tools_on if max_tool_turns > 0 else None)
        for turn in range(max_tool_turns):
            if not (res.tool_calls and tools_on):
                break
            outputs = []
            for t in res.tool_calls:
                out, secs, err = await run_tool(search, t["arguments"])
                await record_tool(self.name, t["name"], secs, err, turn, round_no)
                outputs.append((t["id"], out))
            last_turn = turn == max_tool_turns - 1
            res = await conv.tool_results(outputs, None if last_turn else tools_on)
        if res.tool_calls:
            return {"parse_error": "tool loop exhausted"}
        try:
            return parse_json(res.content)
        except ValueError as e:
            return {"parse_error": str(e), "raw": res.content[:2000]}
