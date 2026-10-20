"""Rebuild a results CSV from ACA Job console logs (`RESULT {json}` lines on stdin).

  az containerapp job logs show -n <job> -g <rg> --container client --format text \
    | python -m probe.job.logs_to_csv results/<name>.csv

Also accepts Log Analytics exports where the line is embedded in a larger string.
"""

import csv
import json
import sys
from pathlib import Path

from probe.job.metrics import CSV_COLUMNS


def parse_lines(lines: list[str]) -> list[dict[str, object]]:
    rows = []
    for line in lines:
        i = line.find("RESULT {")
        if i < 0:
            continue
        payload = line[i + len("RESULT ") :].strip().rstrip('"')
        try:
            rows.append(json.loads(payload))
        except json.JSONDecodeError:
            continue
    return rows


def main() -> None:
    if len(sys.argv) != 2:
        sys.exit("usage: python -m probe.job.logs_to_csv OUT.csv < logs.txt")
    rows = parse_lines(sys.stdin.read().splitlines())
    out = Path(sys.argv[1])
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=CSV_COLUMNS, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)
    print(f"wrote {len(rows)} row(s) to {out}", file=sys.stderr)


if __name__ == "__main__":
    main()
