"""Calibrated long-call prompts.

S and L are the same task at two sizes: review N synthetic facts and write one verdict per fact, which
makes the answer (and therefore the call) long. S calibrates N (words per note fixed); L keeps S's N and
calibrates the words per note (observed: beyond ~500 items the model stops listing every item). Targets:
S about 300 s, L about 450 s on the direct path; the result is saved to results/calibration.json by run_matrix.py.
"""

import json
import re
from typing import Any

BASE_WORDS = 30
DEFAULT_ITEMS = 485  # items for which one verdict per item is still reliable (observed: more makes the model answer short)


def system_prompt(words: int = BASE_WORDS) -> str:
    return (
        "You are a meticulous design reviewer. You receive facts[] extracted from a synthetic "
        "high-level design document. Reply with ONE JSON object only: "
        '{"verdicts":[{"id": string, "ok": boolean, "note": string}]}. '
        "verdicts MUST contain EXACTLY ONE entry for EVERY input fact, in input order. "
        f"Each note is {words - 5} to {words + 5} words, says whether the fact is consistent with the other "
        "facts and names at least two related fact ids. Never abbreviate, never use ellipses, never write "
        "'etc.'; an answer with fewer entries than fact_count is invalid."
    )


TARGETS_S = {"S": 300, "L": 450}
# L cannot be reached by output length alone (observed: the model stops at ~35-40K tokens, ~230-290 s), so L adds
# silent reasoning time with xhigh effort. S uses the --reasoning default (high).
PROMPT_REASONING = {"S": None, "L": "xhigh"}


def build_prompt(
    n_facts: int, facts: list[dict[str, Any]], words: int = BASE_WORDS
) -> tuple[str, str]:
    """(system, user) for the first n_facts facts, each verdict note about `words` words."""
    picked = facts[:n_facts]
    user = json.dumps({"fact_count": len(picked), "facts": picked})
    return system_prompt(words), user


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
