"""Orchestrator as a Microsoft Agent Framework workflow:

    planner (+ ai_search) --fan-out--> cover | network | addressing | compute --fan-in--> assemble

The planner derives the section list; a content agent only runs when it was assigned sections.

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
    CONTENT_INSTRUCTIONS,
    DOMAIN_OWNER,
    PLANNER_EXHAUSTIVE,
    PLANNER_NORMAL,
    SHEET_TYPES,
    build_agent,
    run_agent,
    with_retries,
)
from worker.config import RunConfig, Settings
from worker.llm_client import Model, Recorder, call_context
from worker.outputs import build_artifacts
from worker.search_tool import SearchFn, make_search_tool
from worker.store import Store, now_utc

ENGAGEMENT_ID = "ENG-001"
SCOPE_INVENTORY = {
    "stacks": [
        {"stack": "Compute and Storage", "solutions": ["Virtualisation", "Backup"]},
        {"stack": "Network", "solutions": ["Core routing", "Firewalling", "Load balancing"]},
    ],
    "subnets": ["snet-app-01", "snet-data-01", "snet-mgmt-01", "snet-dmz-01"],
}


def load_chunks(path: str) -> list[dict[str, Any]]:
    with open(path) as f:
        return [json.loads(line) for line in f if line.strip()]


def to_fact(chunk: dict[str, Any]) -> dict[str, Any]:
    """A chunk as it appears in an envelope's facts[]."""
    keys = ("id", "content", "filename", "page_number", "section_path", "chunk_type")
    return {k: chunk[k] for k in keys}


def select_by_tokens(chunks: list[dict[str, Any]], budget_tokens: int) -> list[dict[str, Any]]:
    """Take chunks in order until the rough token budget (chars/4 of the JSON) is used."""
    out, used = [], 0
    for c in chunks:
        cost = len(json.dumps(to_fact(c))) // 4 + 1
        if used + cost > budget_tokens:
            break
        out.append(c)
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
    chunks: list[dict[str, Any]]
    client: Any  # MAF chat client over the timed HTTP client
    search: SearchFn | None
    record: Recorder
    store: Store
    total_agents: int
    attempts: int = 1
    backoff_s: float = 5.0
    done: int = 0
    plan: dict[str, Any] = field(
        default_factory=dict
    )  # latest planner output, for the round result

    async def run(self, agent_name: str, round_no: int, make_run) -> dict[str, Any]:
        """Run one agent with the pipeline's retry policy; every retry is recorded."""

        async def note(attempt: int, err: Exception) -> None:
            await self.record(
                {
                    "kind": "agent_retry", "run_id": self.run_id, "round": round_no, "agent": agent_name,
                    "attempt": attempt, "outcome": "retrying", "error_type": type(err).__name__,
                    "error_detail": str(err)[:300],
                }
            )  # fmt: skip

        return await with_retries(
            make_run, attempts=self.attempts, backoff_s=self.backoff_s, on_retry=note
        )

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
        facts = [
            to_fact(c)
            for c in select_by_tokens([c for c in d.chunks if c["in_slice"]], cfg.fact_tokens)
        ]
        instructions = PLANNER_EXHAUSTIVE if cfg.depth == "exhaustive" else PLANNER_NORMAL
        envelope = {
            "engagement_id": ENGAGEMENT_ID,
            "scope_inventory": SCOPE_INVENTORY,
            "fact_count": len(facts),
            "facts": facts,
        }
        with call_context(
            run_id=d.run_id,
            agent="planner",
            round_no=msg.round_no,
            path=cfg.path,
            stream=cfg.stream,
        ):
            tools = [make_search_tool(d.search, d.record, cfg.max_tool_calls)] if d.search else None
            agent = build_agent(
                d.client,
                "planner",
                instructions,
                tools=tools,
                reasoning_effort=cfg.reasoning_effort,
                max_output_tokens=cfg.max_output_tokens,
            )
            plan = await d.run(
                "planner",
                msg.round_no,
                lambda: run_agent(agent, json.dumps(envelope), stream=cfg.stream),
            )
        d.done += 1
        d.plan = plan
        await d.progress(f"round {msg.round_no}: content agents")
        await ctx.send_message(PlanDone(msg.round_no, plan))


def assigned_sections(plan: dict[str, Any], topic: str) -> list[dict[str, Any]]:
    """Sections the planner gave to this agent (owner_agent wins; sheet_type is the fallback)."""
    out = []
    for s in plan.get("sections") or []:
        if not isinstance(s, dict):
            continue
        owner = s.get("owner_agent") or SHEET_TYPES.get(str(s.get("sheet_type")))
        if owner == topic:
            out.append(s)
    return out


class ContentExecutor(Executor):
    """One content agent. It only calls the model when the planner assigned it sections."""

    def __init__(self, d: Deps, topic: str) -> None:
        super().__init__(id=topic)
        self.d, self.topic = d, topic

    @handler
    async def run(self, msg: PlanDone, ctx: WorkflowContext[SectionDone]) -> None:
        d, cfg, topic = self.d, self.d.cfg, self.topic
        mine = assigned_sections(msg.plan, topic)
        if not mine:
            d.done += 1
            await ctx.send_message(
                SectionDone(topic, {"sheets": [], "issues": ["no sections assigned"]})
            )
            return
        chunks = [c for c in d.chunks if c["in_slice"] and DOMAIN_OWNER.get(c["domain"]) == topic]
        facts = [to_fact(c) for c in select_by_tokens(chunks, cfg.section_fact_tokens)]
        payload = json.dumps({"engagement_id": ENGAGEMENT_ID, "sections": mine, "facts": facts})
        with call_context(
            run_id=d.run_id, agent=topic, round_no=msg.round_no, path=cfg.path, stream=cfg.stream
        ):
            tools = [make_search_tool(d.search, d.record, cfg.max_tool_calls)] if d.search else None
            agent = build_agent(
                d.client,
                topic,
                CONTENT_INSTRUCTIONS[topic],
                tools=tools,
                reasoning_effort=cfg.reasoning_effort,
                max_output_tokens=cfg.max_output_tokens,
            )
            output = await d.run(
                topic, msg.round_no, lambda: run_agent(agent, payload, stream=cfg.stream)
            )
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
    sections = [ContentExecutor(d, t) for t in d.cfg.agents if t in CONTENT_INSTRUCTIONS]
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
    n_sections = len([t for t in cfg.agents if t in CONTENT_INSTRUCTIONS])
    d = Deps(
        run_id=run_id,
        cfg=cfg,
        chunks=load_chunks(st.facts_path),
        client=model.agent_client(),
        search=search,
        record=record,
        store=store,
        total_agents=(1 + n_sections) * cfg.rounds,
        attempts=st.llm_max_attempts,
        backoff_s=st.llm_retry_backoff_s,
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
        last = outputs[-1]
        for name, data in build_artifacts(last["plan"], last["sections"]).items():
            await store.put_file(run_id, name, data)
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
