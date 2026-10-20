"""Orchestrator: planner (large facts[] payload) -> section agents in parallel -> assembled output."""

import asyncio
import json
import time
from collections.abc import Callable
from typing import Any

from worker.agents.planner import PLANNER, PLANNER_EXHAUSTIVE
from worker.agents.section import SECTION_AGENTS
from worker.config import RunConfig, Settings
from worker.llm_client import LLMClient
from worker.store import Store, now_utc
from worker.tools.doc_search import SearchFn


def load_facts(path: str) -> list[dict[str, Any]]:
    with open(path) as f:
        return [json.loads(line) for line in f if line.strip()]


def select_by_tokens(facts: list[dict[str, Any]], budget_tokens: int) -> list[dict[str, Any]]:
    """Take facts in order until the rough token budget (chars/4) is used."""
    out, used = [], 0
    for f in facts:
        cost = len(json.dumps(f)) // 4 + 1
        if used + cost > budget_tokens:
            break
        out.append(f)
        used += cost
    return out


def summarise(calls: list[dict[str, Any]], elapsed_s: float) -> dict[str, Any]:
    llm = [c for c in calls if c.get("kind") == "llm"]

    def peak(key: str) -> float | None:
        vals = [c[key] for c in llm if c.get(key) is not None]
        return max(vals) if vals else None

    return {
        "elapsed_s": round(elapsed_s, 1),
        "llm_calls": len(llm),
        "failed_calls": sum(1 for c in llm if c.get("outcome") != "completed"),
        "max_ttfb_s": peak("ttfb_s"),
        "max_longest_gap_s": peak("longest_gap_s"),
        "max_call_total_s": peak("total_s"),
        "prompt_tokens": sum(c.get("prompt_tokens") or 0 for c in llm),
        "completion_tokens": sum(c.get("completion_tokens") or 0 for c in llm),
        "reasoning_tokens": sum(c.get("reasoning_tokens") or 0 for c in llm),
    }


async def execute(
    run_id: str,
    st: Settings,
    cfg: RunConfig,
    store: Store,
    make_llm: Callable[..., LLMClient],
    search: SearchFn | None,
) -> dict[str, Any]:
    facts = load_facts(st.facts_path)
    calls: list[dict[str, Any]] = []
    seq = 0
    lock = asyncio.Lock()

    async def record(rec: dict[str, Any]) -> None:
        nonlocal seq
        async with lock:
            seq += 1
            calls.append(rec)
            await store.add_call(run_id, seq, rec)
        print("CALL " + json.dumps({k: v for k, v in rec.items() if v is not None}), flush=True)

    async def record_tool(
        agent: str, tool: str, secs: float, err: str, turn: int, rnd: int
    ) -> None:
        await record(
            {
                "kind": "tool", "run_id": run_id, "ts_utc": now_utc(), "round": rnd, "agent": agent,
                "turn": turn, "attempt": 1, "path": tool, "total_s": round(secs, 3),
                "outcome": "error" if err else "completed", "error_type": err,
            }
        )  # fmt: skip

    llm = make_llm(st, cfg, run_id, record)
    t0 = time.monotonic()
    await store.update_run(run_id, status="running", started_utc=now_utc(), phase="starting")
    outputs: list[dict[str, Any]] = []
    total_agents = (1 + len(cfg.agents)) * cfg.rounds
    done = 0
    try:
        for rnd in range(1, cfg.rounds + 1):
            await store.update_run(
                run_id, phase=f"round {rnd}: planner", progress=f"{done}/{total_agents}"
            )
            planner_facts = select_by_tokens(facts, cfg.fact_tokens)
            planner = PLANNER_EXHAUSTIVE if cfg.depth == "exhaustive" else PLANNER
            plan = await planner.run(
                llm, json.dumps({"fact_count": len(planner_facts), "facts": planner_facts}), search=None, record_tool=record_tool,
                max_tool_turns=0, round_no=rnd,
            )  # fmt: skip
            done += 1
            await store.update_run(
                run_id, phase=f"round {rnd}: sections", progress=f"{done}/{total_agents}"
            )

            async def section(topic: str, rnd: int = rnd, plan: dict[str, Any] = plan):
                topic_facts = select_by_tokens(
                    [f for f in facts if f["topic"] == topic], cfg.section_fact_tokens
                )
                mine = [s for s in plan.get("sections", []) if s.get("agent") == topic]
                payload = json.dumps({"plan": mine, "facts": topic_facts})
                return topic, await SECTION_AGENTS[topic].run(
                    llm, payload, search=search, record_tool=record_tool,
                    max_tool_turns=cfg.max_tool_turns, round_no=rnd,
                )  # fmt: skip

            results = await asyncio.gather(*(section(t) for t in cfg.agents if t in SECTION_AGENTS))
            done += len(results)
            outputs.append({"round": rnd, "plan": plan, "sections": dict(results)})
        summary = summarise(calls, time.monotonic() - t0)
        await store.put_output(
            run_id, {"run_id": run_id, "config": cfg.model_dump(), "rounds": outputs}
        )
        await store.update_run(
            run_id, status="succeeded", finished_utc=now_utc(), phase="done",
            progress=f"{done}/{total_agents}", summary_json=json.dumps(summary),
        )  # fmt: skip
        return summary
    except Exception as e:
        summary = summarise(calls, time.monotonic() - t0)
        await store.update_run(
            run_id, status="failed", finished_utc=now_utc(), error=f"{type(e).__name__}: {e}"[:500],
            progress=f"{done}/{total_agents}", summary_json=json.dumps(summary),
        )  # fmt: skip
        raise
    finally:
        await llm.aclose()
