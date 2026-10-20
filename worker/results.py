"""Per-call result records: CSV schema, append, and rebuilding a CSV from job console logs."""

import csv
import json
import os
import sys
from pathlib import Path
from typing import Any

RECORD_COLUMNS = [
    "ts_utc", "run_id", "label", "round", "agent", "turn", "attempt", "kind", "path", "stream",
    "input_bytes", "http_status", "outcome", "error_type", "error_detail",
    "ttfh_s", "ttfb_s", "ttft_s", "longest_gap_s", "last_chunk_s", "tail_silence_s", "total_s",
    "chunks", "bytes", "prompt_tokens", "completion_tokens", "reasoning_tokens",
    "request_ids", "client_request_id",
]  # fmt: skip


def results_dir() -> Path:
    return Path(os.environ.get("RESULTS_DIR", "results"))


def append_csv(path: Path, rec: dict[str, Any]) -> bool:
    """Append one record; returns False (instead of raising) if the file system is read-only."""
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        new = not path.exists()
        with path.open("a", newline="") as f:
            w = csv.DictWriter(f, fieldnames=RECORD_COLUMNS, extrasaction="ignore")
            if new:
                w.writeheader()
            w.writerow(rec)
        return True
    except OSError:
        return False


def parse_call_lines(lines: list[str]) -> list[dict[str, Any]]:
    out = []
    for line in lines:
        i = line.find("CALL {")
        if i < 0:
            continue
        try:
            out.append(json.loads(line[i + len("CALL ") :].strip().rstrip('"')))
        except json.JSONDecodeError:
            continue
    return out


def main() -> None:
    """Rebuild a CSV from job console logs: ... | python -m worker.results OUT.csv"""
    if len(sys.argv) != 2:
        sys.exit("usage: python -m worker.results OUT.csv < logs.txt")
    rows = parse_call_lines(sys.stdin.read().splitlines())
    out = Path(sys.argv[1])
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=RECORD_COLUMNS, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)
    print(f"wrote {len(rows)} row(s) to {out}", file=sys.stderr)


if __name__ == "__main__":
    main()
