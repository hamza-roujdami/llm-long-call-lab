"""Run the long-call matrix: 3 paths x streaming off/on x {S, L}, against the REAL model.

  python -m worker.run_matrix --max-output-tokens 120000                 # dry run: prints the plan only
  python -m worker.run_matrix --max-output-tokens 120000 --confirm-spend # calibrate, then run the matrix

Cost guard: nothing touches the model unless --confirm-spend is given, and --max-output-tokens is a
required hard cap applied to every call. Retries are always off (one attempt per call).
Step 0 calibrates S (~300 s) and L (~450 s) on path 1 (direct, streaming) and stops with a report if the
target durations cannot be reached.
"""

import argparse
import asyncio
import json
import sys
import time
from collections.abc import Awaitable, Callable
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

from worker.config import PATHS, Settings
from worker.llm_client import CallResult, Model
from worker.orchestrator import load_chunks
from worker.prompts import (
    BASE_WORDS,
    DEFAULT_ITEMS,
    PROMPT_REASONING,
    TARGETS_S,
    build_prompt,
    to_items,
)
from worker.results import append_csv, results_dir


def calibration_file() -> Path:
    return results_dir() / "calibration.json"


def load_calibration() -> dict[str, Any]:
    f = calibration_file()
    return json.loads(f.read_text()) if f.exists() else {}


TOLERANCE = 0.15
START_FACTS = 250  # small first probe: measures the model's speed cheaply before scaling up


async def calibrate(
    name: str,
    target_s: float,
    call: Callable[[int], Awaitable[CallResult]],
    *,
    n_max: int,
    cap: int,
    start: int = START_FACTS,
    tol: float = TOLERANCE,
    max_iter: int = 6,
    max_step: float = 2.0,
) -> dict[str, Any]:
    """Scale the number of facts until one streamed call takes about target_s seconds.

    Each step is clamped to [1/max_step, max_step] x the previous size: the model does not scale linearly (a
    big list can make it answer shortly), so big jumps overshoot or get rejected by the token quota.
    """
    history: list[dict[str, Any]] = []
    n = start
    for _ in range(max_iter):
        n = max(1, min(n, n_max))
        res = await call(n)
        rec = res.record
        d, toks = rec.get("total_s"), rec.get("completion_tokens")
        history.append(
            {
                "n_facts": n,
                "total_s": d,
                "outcome": rec.get("outcome"),
                "http_status": rec.get("http_status"),
                "completion_tokens": toks,
            }
        )
        base = {"name": name, "target_s": target_s, "history": history}
        if not res.ok or d is None:
            return {**base, "status": "failed", "reason": res.error or rec.get("outcome", "error")}
        if toks and toks >= 0.98 * cap:
            return {**base, "status": "failed", "reason": "max_output_tokens cap reached; raise it"}
        if abs(d - target_s) <= tol * target_s:
            return {**base, "status": "ok", "n_facts": n, "measured_s": d}
        lead = rec.get("ttft_s") or 0.0
        n_next = int(n * (target_s - lead) / max(d - lead, 1.0))
        if n >= n_max and n_next > n_max:
            return {**base, "status": "failed", "reason": f"needs more than {n_max} facts"}
        n = max(int(n / max_step), min(n_next, int(n * max_step)))
    return {
        **base,
        "status": "failed",
        "reason": f"not within {int(tol * 100)}% after {max_iter} tries",
    }


SHORT_S = 240  # a call that ends before this tests nothing about the 230-240 s / 4-minute limits


def verdict(rec: dict[str, Any]) -> str:
    total = rec.get("total_s") or 0
    if rec.get("outcome") == "completed" and total < SHORT_S:
        return f"completed in {total:.0f}s: TOO SHORT to test the limits"
    return f"{rec.get('outcome')} http={rec.get('http_status')} {rec.get('error_type') or ''} total={total:.0f}s".strip()


def fit_items(items: list[dict[str, str]], max_tokens: int) -> int:
    """How many items fit in max_tokens (chars/3.5 estimate of the prompt JSON)."""
    used = 0
    for i, it in enumerate(items):
        used += (len(it["id"]) + len(it["text"]) + 20) / 3.5
        if used > max_tokens:
            return i
    return len(items)


def plan_cells(prompts: list[str], paths: list[str], streams: list[bool], repeat: int):
    return [
        (p, path, stream, rep)
        for p in prompts
        for path in paths
        for stream in streams
        for rep in range(1, repeat + 1)
    ]


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawTextHelpFormatter)
    ap.add_argument("--max-output-tokens", type=int, required=True, help="hard cap per call")
    ap.add_argument("--confirm-spend", action="store_true", help="actually call the real model")
    ap.add_argument("--repeat", type=int, default=1)
    ap.add_argument("--paths", default=",".join(PATHS))
    ap.add_argument("--prompts", default="S,L")
    ap.add_argument("--streams", default="off,on")
    ap.add_argument("--reasoning", default="high")
    ap.add_argument("--skip-calibration", action="store_true", help="use results/calibration.json")
    ap.add_argument("--calibrate-only", action="store_true")
    ap.add_argument(
        "--known", default="",
        help="reuse a calibration, e.g. S=485: skip calibrating that prompt (its measured time is not re-checked)",
    )  # fmt: skip
    ap.add_argument(
        "--max-input-tokens", type=int, default=90_000,
        help="largest prompt calibration may build (estimated), kept under the tokens/min quota",
    )  # fmt: skip
    ap.add_argument(
        "--cooldown-s", type=float, default=65.0,
        help="min seconds between the starts of two calls, so one call's tokens cannot trip the next call's rate limit",
    )  # fmt: skip
    return ap.parse_args(argv)


async def amain(args: argparse.Namespace) -> int:
    st = Settings()
    facts = to_items(load_chunks(st.facts_path))
    prompts = [p for p in args.prompts.split(",") if p]
    paths = [p for p in args.paths.split(",") if p]
    streams = [s == "on" for s in args.streams.split(",") if s]
    cells = plan_cells(prompts, paths, streams, args.repeat)
    calls_planned = len(cells) + (0 if args.skip_calibration else 3 * len(prompts))
    print(
        f"PLAN {len(cells)} matrix cell(s) + up to {calls_planned - len(cells)} calibration call(s); "
        f"worst case {calls_planned * args.max_output_tokens:,} output tokens "
        f"(cap {args.max_output_tokens:,}/call); {len(facts)} synthetic items available; "
        f"foundry={'set' if st.foundry_endpoint else 'MISSING'} apim={'set' if st.apim_url and st.apim_key else 'MISSING'}",
        flush=True,
    )
    if not args.confirm_spend:
        print("DRY RUN: add --confirm-spend to call the real model.", flush=True)
        return 0

    run_id = datetime.now(UTC).strftime("%Y%m%dT%H%M%SZ")
    csv_path = results_dir() / "runs.csv"

    async def record(rec: dict[str, Any]) -> None:
        append_csv(csv_path, rec)
        print("CALL " + json.dumps({k: v for k, v in rec.items() if v is not None}), flush=True)

    models: dict[str, Model] = {}
    last_start = 0.0

    async def spacing() -> None:
        nonlocal last_start
        wait = last_start + args.cooldown_s - time.monotonic()
        if last_start and wait > 0:
            print(f"COOLDOWN {wait:.0f}s", flush=True)
            await asyncio.sleep(wait)
        last_start = time.monotonic()

    def model_for(path: str) -> Model:
        if path not in models:
            models[path] = Model(st, path, record, max_attempts=1, run_id=run_id)
        return models[path]

    try:
        calibration = {} if not args.skip_calibration else load_calibration()
        known = {k: int(v) for k, _, v in (x.partition("=") for x in args.known.split(",") if x)}
        for name, knob in known.items():  # S: items, L: words per note
            n = knob if name == "S" else calibration.get("S", {}).get("n_facts", DEFAULT_ITEMS)
            calibration[name] = {
                "n_facts": n,
                "words": BASE_WORDS if name == "S" else knob,
                "measured_s": None,
                "target_s": TARGETS_S[name],
                "reused": True,
            }
        if not args.skip_calibration:
            for name in [p for p in prompts if p not in known]:
                s_items = calibration.get("S", {}).get("n_facts", DEFAULT_ITEMS)

                async def call(knob: int, name: str = name, s_items: int = s_items) -> CallResult:
                    await spacing()
                    n, words = (knob, BASE_WORDS) if name == "S" else (s_items, knob)
                    system, user = build_prompt(n, facts, words)
                    return await model_for("direct").call(
                        user,
                        system=system,
                        stream=True,
                        reasoning_effort=args.reasoning,
                        max_output_tokens=args.max_output_tokens,
                        label=f"calibrate-{name}-{'n' if name == 'S' else 'w'}{knob}",
                        agent="calibration",
                    )

                result = await calibrate(
                    name,
                    TARGETS_S[name],
                    call,
                    n_max=fit_items(facts, args.max_input_tokens) if name == "S" else 200,
                    cap=args.max_output_tokens,
                    start=START_FACTS if name == "S" else 45,
                )
                print("CALIBRATION " + json.dumps(result), flush=True)
                if result["status"] != "ok":
                    print(f"STOP: calibration of {name} failed: {result['reason']}", flush=True)
                    return 2
                calibration[name] = {
                    "n_facts": result["n_facts"] if name == "S" else s_items,
                    "words": BASE_WORDS if name == "S" else result["n_facts"],
                    "measured_s": result["measured_s"],
                    "target_s": result["target_s"],
                }
            try:
                calibration_file().parent.mkdir(parents=True, exist_ok=True)
                calibration_file().write_text(json.dumps(calibration, indent=2) + "\n")
            except OSError:
                pass  # ephemeral job file system: the CALIBRATION log lines are the record
        missing = [p for p in prompts if p not in calibration]
        if missing:
            print(f"STOP: no calibration for {missing}; run without --skip-calibration", flush=True)
            return 2
        if args.calibrate_only:
            return 0

        outcomes: list[str] = []
        for prompt_name, path, stream, rep in cells:
            system, user = build_prompt(
                calibration[prompt_name]["n_facts"],
                facts,
                calibration[prompt_name].get("words", BASE_WORDS),
            )
            label = f"{path}|stream={'on' if stream else 'off'}|{prompt_name}|r{rep}"
            await spacing()
            print(f"CELL start {label}", flush=True)
            res = await model_for(path).call(
                user,
                system=system,
                stream=stream,
                reasoning_effort=PROMPT_REASONING.get(prompt_name) or args.reasoning,
                max_output_tokens=args.max_output_tokens,
                label=label,
                agent="matrix",
            )
            r = res.record
            print(
                f"CELL done  {label}: {r.get('outcome')} http={r.get('http_status')} "
                f"ttfh={r.get('ttfh_s')} ttft={r.get('ttft_s')} gap={r.get('longest_gap_s')} "
                f"total={r.get('total_s')} {res.error}",
                flush=True,
            )
            outcomes.append(f"{label}: {verdict(r)}")
        print("MATRIX " + json.dumps(outcomes), flush=True)
        return 0
    finally:
        for m in models.values():
            await m.aclose()


def main() -> None:
    sys.exit(asyncio.run(amain(parse_args())))


if __name__ == "__main__":
    main()
