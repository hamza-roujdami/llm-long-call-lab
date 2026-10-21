"""Calibrated long-call prompts.

S and L are the same task at two sizes: review N synthetic facts and write one verdict per fact, which
makes the answer (and therefore the call) long. N is calibrated against the real model so S takes about
300 s and L about 450 s on the direct path; the result is saved to results/calibration.json by run_matrix.py.
"""

import json
import re
from typing import Any

SYSTEM = (
    "You are a meticulous design reviewer. You receive facts[] extracted from a synthetic "
    "high-level design document. Reply with ONE JSON object only: "
    '{"verdicts":[{"id": string, "ok": boolean, "note": string}]}. '
    "verdicts MUST contain EXACTLY ONE entry for EVERY input fact, in input order. Each note is 25 to 35 "
    "words, says whether the fact is consistent with the other facts and names at least two related "
    "fact ids. Never abbreviate, never use ellipses, never write 'etc.'; an answer with fewer entries "
    "than fact_count is invalid."
)
TARGETS_S = {"S": 300, "L": 450}


def build_prompt(n_facts: int, facts: list[dict[str, Any]]) -> tuple[str, str]:
    """(system, user) for the first n_facts facts."""
    picked = facts[:n_facts]
    user = json.dumps({"fact_count": len(picked), "facts": picked})
    return SYSTEM, user


def to_items(chunks: list[dict[str, Any]]) -> list[dict[str, str]]:
    """Split HLD chunks into small items (sentences, table rows, config lines): finer than chunks, so
    one verdict per item can make an answer as long as needed."""
    items: list[dict[str, str]] = []
    for c in chunks:
        if c["chunk_type"] == "prose":
            parts = re.split(r"(?<=[.;])\s+", c["content"])
        else:
            parts = c["content"].splitlines()
        for k, text in enumerate(p.strip() for p in parts):
            if len(text) > 20:
                items.append({"id": f"{c['id']}.{k}", "text": text})
    return items
