"""Long-call measurement client for the ACA Job -> APIM -> model lab.

Examples:
  python -m probe.job.run --list
  python -m probe.job.run --scenario apim-stream-450
  python -m probe.job.run --target direct --endpoint stream --param total=20 --param interval=2

Retries are disabled so every measured call is a single attempt. Results are appended to a CSV
and ALSO printed as `RESULT {json}` lines, because ACA Job file systems are ephemeral and the
console log (Log Analytics) is the durable copy. See client/logs_to_csv.py.
"""

import argparse
import asyncio
import csv
import json
import os
import sys
import time
import uuid
from datetime import UTC, datetime
from pathlib import Path

import httpx
from pydantic_settings import BaseSettings, SettingsConfigDict

from probe.job.metrics import CSV_COLUMNS, Result, classify, has_done_marker, longest_gap, pick_ids
from probe.job.scenarios import SCENARIOS, Scenario


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    mock_base_url: str = ""
    mock_api_key: str = ""
    apim_base_url: str = ""
    apim_subscription_key: str = ""
    apim_stream_path: str = "lab"
    apim_buffered_path: str = "lab-buffered"
    results_dir: str = "results"
    client_timeout_s: float = 900.0  # per-read timeout; deliberately longer than every scenario


def _utc_now() -> str:
    return datetime.now(UTC).isoformat(timespec="seconds")


def build_request(sc: Scenario, st: Settings) -> tuple[str, dict[str, str]]:
    headers = {"Accept-Encoding": "identity"}  # no compression: keep chunk timing observable
    if sc.target == "direct":
        base = st.mock_base_url.rstrip("/")
        headers["x-mock-key"] = st.mock_api_key
    else:
        path = st.apim_buffered_path if sc.apim_variant == "buffered" else st.apim_stream_path
        base = f"{st.apim_base_url.rstrip('/')}/{path.strip('/')}"
        headers["Ocp-Apim-Subscription-Key"] = st.apim_subscription_key
    return f"{base}/{sc.endpoint}", headers


async def run_http(sc: Scenario, st: Settings, run_id: str, idx: int) -> Result:
    url, headers = build_request(sc, st)
    rid = str(uuid.uuid4())
    headers["x-client-request-id"] = rid
    res = Result(
        run_id=run_id,
        started_utc=_utc_now(),
        scenario=sc.name,
        hypothesis=sc.hypothesis,
        target=sc.target,
        path=url.split("//", 1)[-1].split("/", 1)[-1],
        query="&".join(f"{k}={v}" for k, v in sc.params.items()),
        client_stream=sc.client_stream,
        parallel_index=idx,
        parallel_total=sc.parallel,
        client_request_id=rid,
    )
    times: list[float] = []
    tail = b""
    error: BaseException | None = None
    t0 = time.monotonic()
    try:
        async with httpx.AsyncClient(timeout=httpx.Timeout(st.client_timeout_s, connect=30)) as c:
            async with c.stream("GET", url, params=sc.params, headers=headers) as r:
                res.http_status = r.status_code
                res.ttfh_s = time.monotonic() - t0
                res.server_request_ids = pick_ids(dict(r.headers))
                if sc.client_stream:
                    async for chunk in r.aiter_raw():
                        if not chunk:
                            continue
                        times.append(time.monotonic() - t0)
                        res.bytes += len(chunk)
                        tail = (tail + chunk)[-256:]
                else:
                    body = await r.aread()
                    res.bytes = len(body)
                    tail = body[-256:]
    except (httpx.HTTPError, OSError) as e:
        error = e
        res.error_type = type(e).__name__
        res.error_detail = str(e)[:200]
    res.total_s = time.monotonic() - t0
    return _finish(res, times, tail, error)


def _finish(res: Result, times: list[float], tail: bytes, error: BaseException | None) -> Result:
    res.chunks = len(times)
    res.ttfb_s = times[0] if times else None
    res.longest_gap_s = longest_gap(times)
    res.last_chunk_s = times[-1] if times else None
    res.outcome = classify(res.http_status, has_done_marker(tail), error)
    if res.outcome == "http_error":
        res.error_detail = tail.decode(errors="replace")[:200]
    return res


def write_csv(path: Path, results: list[Result]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    new = not path.exists()
    with path.open("a", newline="") as f:
        w = csv.DictWriter(f, fieldnames=CSV_COLUMNS)
        if new:
            w.writeheader()
        for r in results:
            w.writerow(r.row())


def _round(d: dict[str, object]) -> dict[str, object]:
    return {k: round(v, 3) if isinstance(v, float) else v for k, v in d.items()}


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawTextHelpFormatter)
    p.add_argument("--scenario", default=os.environ.get("SCENARIO"), choices=[*SCENARIOS])
    p.add_argument("--list", action="store_true", help="list scenarios and exit")
    p.add_argument("--target", choices=["direct", "apim"])
    p.add_argument("--endpoint", choices=["silent", "stream", "gap"])
    p.add_argument("--param", action="append", default=[], metavar="K=V")
    p.add_argument("--no-stream", action="store_true", help="read the body in one go")
    p.add_argument("--apim-variant", choices=["stream", "buffered"], default="stream")
    p.add_argument("--parallel", type=int, default=1)
    p.add_argument("--out", help="CSV path (default results/<scenario>-<utc>.csv)")
    return p.parse_args(argv)


def resolve(args: argparse.Namespace) -> Scenario:
    if args.scenario:
        return SCENARIOS[args.scenario]
    if not (args.target and args.endpoint):
        sys.exit("choose --scenario NAME, or --target and --endpoint (see --list)")
    params = {k: float(v) for k, v in (kv.split("=", 1) for kv in args.param)}
    return Scenario(
        "custom",
        "",
        args.target,
        args.endpoint,
        params,
        client_stream=not args.no_stream,
        apim_variant=args.apim_variant,
        parallel=args.parallel,
    )


async def amain(args: argparse.Namespace) -> list[Result]:
    st = Settings()
    run_id = datetime.now(UTC).strftime("%Y%m%dT%H%M%SZ")
    sc = resolve(args)
    return list(await asyncio.gather(*(run_http(sc, st, run_id, i) for i in range(sc.parallel))))


def main(argv: list[str] | None = None) -> None:
    args = parse_args(argv)
    if args.list:
        for s in SCENARIOS.values():
            print(
                f"{s.name:28} {s.hypothesis:3} {s.target:6} {s.endpoint:6} {s.params} "
                f"stream={s.client_stream} variant={s.apim_variant} parallel={s.parallel}"
            )
        return
    results = asyncio.run(amain(args))
    label = args.scenario or "custom"
    out = (
        Path(args.out)
        if args.out
        else Path(Settings().results_dir)
        / (f"{label}-{datetime.now(UTC).strftime('%Y%m%dT%H%M%SZ')}.csv")
    )
    for r in results:
        print("RESULT " + json.dumps(_round(r.row())), flush=True)
    try:
        write_csv(out, results)
        print(f"wrote {len(results)} row(s) to {out}", file=sys.stderr)
    except OSError as e:
        print(f"CSV not written ({e}); RESULT lines above are the record", file=sys.stderr)


if __name__ == "__main__":
    main()
