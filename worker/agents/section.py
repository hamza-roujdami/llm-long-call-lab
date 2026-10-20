from worker.agents.base import Agent

_SCHEMA = (
    'Reply with ONE JSON object only: {"section": string, "summary": string, '
    '"tables":[{"title":string,"columns":[string],"rows":[[string]]}], '
    '"findings":[{"fact_ids":[string],"text":string}], "issues":[string]}. '
    "Use the ai_search tool to verify at least one detail before answering, and cite page numbers."
)

_FOCUS = {
    "cover": "document control, scope, requirements and assumptions",
    "network": "VLANs, routing and BGP peering, firewall policy and load balancing",
    "addressing": "IPv4 supernets, subnets, DHCP scopes and NAT pools",
    "compute": "clusters, workload placement, datastores and backup tiers",
}


def _make(topic: str) -> Agent:
    return Agent(
        name=topic,
        use_search=True,
        system=(
            f"You are the {topic} section agent writing the low-level design section on {_FOCUS[topic]}. "
            "You receive the planner's instructions for your section and the relevant facts[]. "
            "Produce concise tables and findings; flag inconsistencies as issues. " + _SCHEMA
        ),
    )


SECTION_AGENTS = {t: _make(t) for t in _FOCUS}
