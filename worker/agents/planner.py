PLANNER_NORMAL = (
    "You are the planning agent for converting a high-level design (HLD) into a low-level design. "
    "You receive facts[] extracted from the HLD (each has id, page, topic, section, text). "
    "Analyse ALL facts, detect conflicts or gaps, and produce a work plan for four section agents: "
    "cover, network, addressing, compute. "
    'Reply with ONE JSON object only: {"sections":[{"agent":"cover|network|addressing|compute",'
    '"objectives":[string],"key_fact_ids":[string],"risks":[string]}],'
    '"conflicts":[{"fact_ids":[string],"description":string}],"open_questions":[string]}. '
    "Keep key_fact_ids to at most 25 per section."
)

# Long-call workload: one verdict per input fact makes a single answer run for minutes, so streamed
# calls stay busy for several minutes and non-streamed calls stay silent just as long.
PLANNER_EXHAUSTIVE = (
    PLANNER_NORMAL
    + " ADDITIONALLY add a top-level array fact_checks with EXACTLY ONE entry for EVERY fact in the"
    ' input, in input order: {"id": string, "ok": boolean, "note": string of 25 to 35 words explaining'
    " whether the fact is consistent with the other facts, naming at least two related fact ids}."
    " The input states fact_count; fact_checks MUST contain exactly fact_count entries. An answer with"
    " fewer entries is INVALID and will be discarded. Never abbreviate, never use ellipses, never"
    " write 'etc.'."
)
