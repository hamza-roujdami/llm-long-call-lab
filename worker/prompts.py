"""Calibrated long-call prompts.

S and L are the same task at two sizes: review N synthetic facts and write one verdict per fact, which
makes the answer (and therefore the call) long. N is calibrated against the real model so S takes about
300 s and L about 450 s on the direct path; the result is saved to results/calibration.json by run_matrix.py.
"""

import json
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
