"""Orchestrator as a Microsoft Agent Framework workflow:

    planner --fan-out--> cover | network | addressing | compute --fan-in--> assemble

Each executor wraps a MAF `Agent`; the model client under it is timed at the HTTP level (llm_client.py),
so every model call and every ai_search call becomes one record. One workflow run = one round.
"""

import json
import time
from collections.abc import Callable
from dataclasses import dataclass, field
from typing import Any, Never

from agent_framework import Executor, WorkflowBuilder, WorkflowContext, handler

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


@dataclass
class RoundStart:
    round_no: int


@dataclass
class PlanDone:
    round_no: int
    plan: dict[str, Any]


@dataclass
class SectionDone:
    topic: str
    output: dict[str, Any]


@dataclass
class Deps:
    run_id: str
    cfg: RunConfig
    facts: list[dict[str, Any]]
    client: Any  # MAF chat client over the timed HTTP client
    search: SearchFn | None
    record: Recorder
    store: Store
    total_agents: int
    done: int = 0
    plan: dict[str, Any] = field(
        default_factory=dict
    )  # latest planner output, for the round result

    async def progress(self, phase: str) -> None:
        await self.store.update_run(
            self.run_id, phase=phase, progress=f"{self.done}/{self.total_agents}"
        )


class PlannerExecutor(Executor):
    def __init__(self, d: Deps) -> None:
        super().__init__(id="planner")
        self.d = d

    @handler
    async def run(self, msg: RoundStart, ctx: WorkflowContext[PlanDone]) -> None:
        d, cfg = self.d, self.d.cfg
        await d.progress(f"round {msg.round_no}: planner")
        facts = select_by_tokens(d.facts, cfg.fact_tokens)
        instructions = PLANNER_EXHAUSTIVE if cfg.depth == "exhaustive" else PLANNER_NORMAL
        with call_context(
            run_id=d.run_id,
            agent="planner",
            round_no=msg.round_no,
            path=cfg.path,
            stream=cfg.stream,
        ):
            agent = build_agent(
                d.client,
                "planner",
                instructions,
                reasoning_effort=cfg.reasoning_effort,
                max_output_tokens=cfg.max_output_tokens,
            )
            payload = json.dumps({"fact_count": len(facts), "facts": facts})
            plan = await run_agent(agent, payload, stream=cfg.stream)
        d.done += 1
        d.plan = plan
        await d.progress(f"round {msg.round_no}: sections")
        await ctx.send_message(PlanDone(msg.round_no, plan))


class SectionExecutor(Executor):
    def __init__(self, d: Deps, topic: str) -> None:
        super().__init__(id=topic)
        self.d, self.topic = d, topic

    @handler
    async def run(self, msg: PlanDone, ctx: WorkflowContext[SectionDone]) -> None:
        d, cfg, topic = self.d, self.d.cfg, self.topic
        facts = select_by_tokens(
            [f for f in d.facts if f["topic"] == topic], cfg.section_fact_tokens
        )
        mine = [s for s in msg.plan.get("sections", []) if s.get("agent") == topic]
        payload = json.dumps({"plan": mine, "facts": facts})
        with call_context(
            run_id=d.run_id, agent=topic, round_no=msg.round_no, path=cfg.path, stream=cfg.stream
        ):
            tools = [make_search_tool(d.search, d.record, cfg.max_tool_calls)] if d.search else None
            agent = build_agent(
                d.client,
                topic,
                SECTION_INSTRUCTIONS[topic],
                tools=tools,
                reasoning_effort=cfg.reasoning_effort,
                max_output_tokens=cfg.max_output_tokens,
            )
            output = await run_agent(agent, payload, stream=cfg.stream)
        d.done += 1
        await ctx.send_message(SectionDone(topic, output))


class AssembleExecutor(Executor):
    def __init__(self, d: Deps) -> None:
        super().__init__(id="assemble")
        self.d = d

    @handler
    async def run(
        self, results: list[SectionDone], ctx: WorkflowContext[Never, dict[str, Any]]
    ) -> None:
        await ctx.yield_output(
            {"plan": self.d.plan, "sections": {r.topic: r.output for r in results}}
        )


def build_workflow(d: Deps):
    planner = PlannerExecutor(d)
    sections = [SectionExecutor(d, t) for t in d.cfg.agents if t in SECTION_INSTRUCTIONS]
    assemble = AssembleExecutor(d)
    return (
        WorkflowBuilder(start_executor=planner, output_from=[assemble])
        .add_fan_out_edges(planner, sections)
        .add_fan_in_edges(sections, assemble)
        .build()
    )


async def execute(
    run_id: str,
    st: Settings,
    cfg: RunConfig,
    store: Store,
    make_model: Callable[[Recorder], Model],
    search: SearchFn | None,
) -> dict[str, Any]:
    calls: list[dict[str, Any]] = []
    seq = 0

    async def record(rec: dict[str, Any]) -> None:
        nonlocal seq
        seq += 1
        calls.append(rec)
        await store.add_call(run_id, seq, rec)
        print("CALL " + json.dumps({k: v for k, v in rec.items() if v is not None}), flush=True)

    model = make_model(record)
    n_sections = len([t for t in cfg.agents if t in SECTION_INSTRUCTIONS])
    d = Deps(
        run_id=run_id,
        cfg=cfg,
        facts=load_facts(st.facts_path),
        client=model.agent_client(),
        search=search,
        record=record,
        store=store,
        total_agents=(1 + n_sections) * cfg.rounds,
    )
    t0 = time.monotonic()
    await store.update_run(run_id, status="running", started_utc=now_utc(), phase="starting")
    try:
        workflow = build_workflow(d)
        outputs: list[dict[str, Any]] = []
        for rnd in range(1, cfg.rounds + 1):
            result = await workflow.run(RoundStart(rnd))
            outputs.append({"round": rnd, **result.get_outputs()[0]})
        summary = summarise(calls, time.monotonic() - t0)
        await store.put_output(
            run_id, {"run_id": run_id, "config": cfg.model_dump(), "rounds": outputs}
        )
        await store.update_run(
            run_id,
            status="succeeded",
            finished_utc=now_utc(),
            phase="done",
            progress=f"{d.done}/{d.total_agents}",
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
            progress=f"{d.done}/{d.total_agents}",
            summary_json=json.dumps(summary),
        )
        raise
    finally:
        await model.aclose()
