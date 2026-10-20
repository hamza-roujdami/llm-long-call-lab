"""Orchestrator: planner (large facts[] payload) -> section agents in parallel -> assembled output.

Every agent is a Microsoft Agent Framework `Agent`; the model client under it is timed at the HTTP level
(see llm_client.py), so each model call and each ai_search call becomes one record.
"""

import asyncio
import json
import time
from collections.abc import Callable
from typing import Any

from worker.agents import (
    PLANNER_EXHAUSTIVE,
    PLANNER_NORMAL,
    SECTION_INSTRUCTIONS,
    build_agent,
    run_agent,
)
from worker.config import RunConfig, Settings
from worker.llm_client import Model, Recorder, call_context
from worker.search_tool import SearchFn, make_search_tool
from worker.store import Store, now_utc


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
        "max_ttft_s": peak("ttft_s"),
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
    make_model: Callable[[Recorder], Model],
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

    model = make_model(record)
    client = model.agent_client()
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
            instructions = PLANNER_EXHAUSTIVE if cfg.depth == "exhaustive" else PLANNER_NORMAL
            with call_context(
                run_id=run_id, agent="planner", round_no=rnd, path=cfg.path, stream=cfg.stream
            ):
                planner = build_agent(
                    client,
                    "planner",
                    instructions,
                    reasoning_effort=cfg.reasoning_effort,
                    max_output_tokens=cfg.max_output_tokens,
                )
                payload = json.dumps({"fact_count": len(planner_facts), "facts": planner_facts})
                plan = await run_agent(planner, payload, stream=cfg.stream)
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
                with call_context(
                    run_id=run_id, agent=topic, round_no=rnd, path=cfg.path, stream=cfg.stream
                ):
                    tools = (
                        [make_search_tool(search, record, cfg.max_tool_calls)] if search else None
                    )
                    agent = build_agent(
                        client,
                        topic,
                        SECTION_INSTRUCTIONS[topic],
                        tools=tools,
                        reasoning_effort=cfg.reasoning_effort,
                        max_output_tokens=cfg.max_output_tokens,
                    )
                    return topic, await run_agent(agent, payload, stream=cfg.stream)

            results = await asyncio.gather(
                *(section(t) for t in cfg.agents if t in SECTION_INSTRUCTIONS)
            )
            done += len(results)
            outputs.append({"round": rnd, "plan": plan, "sections": dict(results)})
        summary = summarise(calls, time.monotonic() - t0)
        await store.put_output(
            run_id, {"run_id": run_id, "config": cfg.model_dump(), "rounds": outputs}
        )
        await store.update_run(
            run_id,
            status="succeeded",
            finished_utc=now_utc(),
            phase="done",
            progress=f"{done}/{total_agents}",
            summary_json=json.dumps(summary),
        )
        return summary
    except Exception as e:
        summary = summarise(calls, time.monotonic() - t0)
        await store.update_run(
            run_id,
            status="failed",
            finished_utc=now_utc(),
            error=f"{type(e).__name__}: {e}"[:500],
            progress=f"{done}/{total_agents}",
            summary_json=json.dumps(summary),
        )
        raise
    finally:
        await model.aclose()
