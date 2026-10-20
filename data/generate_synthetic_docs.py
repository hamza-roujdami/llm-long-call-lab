"""Generate a SYNTHETIC high-level design document and its facts[] list.

Everything is fictional and produced from a seeded RNG (no real customer data). Output:
  data/synthetic_docs/design_document.md   readable document, one section per page
  data/synthetic_docs/facts.jsonl          one fact per line (the planner payload source)
  data/synthetic_docs/pages.jsonl          one search document per page (indexed in AI Search)

  python data/generate_synthetic_docs.py [--pages 180] [--seed 42]
"""

import argparse
import json
import random
from pathlib import Path

OUT = Path(__file__).parent / "synthetic_docs"
FACTS_PER_PAGE = 9
TOPIC_SHARE = {"cover": 0.07, "network": 0.35, "addressing": 0.30, "compute": 0.28}
TOPIC_TITLES = {
    "cover": [
        "Document control",
        "Scope and objectives",
        "Stakeholders",
        "Requirements",
        "Assumptions",
    ],
    "network": [
        "Core routing",
        "Switching fabric",
        "Perimeter firewalls",
        "Load balancing",
        "WAN links",
    ],
    "addressing": [
        "IPv4 supernets",
        "Site allocations",
        "DHCP scopes",
        "Management ranges",
        "NAT pools",
    ],
    "compute": [
        "Hypervisor clusters",
        "Workload placement",
        "Storage policies",
        "Backup tiers",
        "Capacity",
    ],
}
SITES = ["Aldermere", "Brightholm", "Cresswick", "Dunmoor", "Eastvale", "Fernhollow"]
ENVS = ["prod", "preprod", "test", "dr", "mgmt"]
TIERS = ["web", "app", "data", "cache", "queue", "batch", "bastion", "monitoring"]
APPS = ["ledger", "catalogue", "scheduler", "gateway", "telemetry", "mailer", "reports", "identity"]
OWNERS = [
    "Platform Engineering",
    "Network Operations",
    "Infrastructure Architecture",
    "Service Delivery",
]


def _cidr(r: random.Random, bits: int) -> str:
    return f"10.{r.randint(0, 255)}.{r.randint(0, 255) & (255 << (24 - bits) if bits < 24 else 255)}.0/{bits}"


def network_fact(r: random.Random) -> str:
    kind = r.randrange(4)
    sw1, sw2 = (f"{r.choice(SITES)[:3].lower()}-sw{r.randint(1, 24):02d}" for _ in range(2))
    if kind == 0:
        return (
            f"VLAN {r.randint(100, 3999)} ({r.choice(TIERS)}-{r.choice(ENVS)}) is trunked between {sw1} and {sw2} "
            f"on port-channel {r.randint(1, 48)}, uses MTU {r.choice([1500, 9000, 9216])}, maps to VRF "
            f"{r.choice(ENVS).upper()}-{r.randint(1, 9)} and runs {r.choice(['RSTP', 'MSTP'])} with bridge priority "
            f"{r.choice([4096, 8192, 24576, 32768])}; changes require CAB approval {r.randint(2, 10)} days ahead."
        )
    if kind == 1:
        return (
            f"Firewall rule {r.randint(1000, 9999)} permits {r.choice(['tcp', 'udp'])}/{r.choice([443, 8443, 5432, 1433, 9092, 6379])} "
            f"from {_cidr(r, 24)} to {_cidr(r, 26)} with {r.choice(['full', 'drop-only', 'sampled'])} logging; "
            f"the rule is reviewed every {r.choice([30, 60, 90, 180])} days by {r.choice(OWNERS)} and expires on "
            f"202{r.randint(7, 9)}-{r.randint(1, 12):02d}-{r.randint(1, 28):02d}."
        )
    if kind == 2:
        return (
            f"BGP peering between core-{r.randint(1, 8)} (AS {r.randint(64512, 65534)}) and edge-{r.randint(1, 8)} "
            f"(AS {r.randint(64512, 65534)}) at {r.choice(SITES)} uses timers {r.choice([3, 10, 30])}/"
            f"{r.choice([9, 30, 90])}s, max-prefix {r.choice([500, 1000, 5000])} and BFD interval "
            f"{r.choice([100, 300, 500])} ms; ingress route-map RM-{r.choice(TIERS).upper()}-{r.randint(1, 30)} applies."
        )
    return (
        f"Load balancer pool {r.choice(APPS)}-{r.choice(ENVS)} fronts {r.randint(2, 12)} members with "
        f"{r.choice(['least-connections', 'round-robin', 'weighted'])} balancing, health probe "
        f"{r.choice(['tcp', 'http', 'https'])}/{r.choice([80, 443, 8080])} every {r.choice([5, 10, 30])}s and "
        f"idle timeout {r.choice([60, 240, 300, 900])}s; persistence {r.choice(['none', 'source-ip', 'cookie'])}."
    )


def addressing_fact(r: random.Random) -> str:
    kind = r.randrange(3)
    site, env = r.choice(SITES), r.choice(ENVS)
    if kind == 0:
        return (
            f"Subnet {_cidr(r, r.choice([22, 24, 26]))} is allocated to {r.choice(TIERS)} workloads in {site}/{env}; "
            f"gateway .1, {r.randint(2, 20)} addresses reserved, DHCP "
            f"{r.choice(['disabled', 'enabled with 8h lease', 'relay to dhcp-' + str(r.randint(1, 4))])}, "
            f"growth headroom {r.choice([15, 20, 25, 30])}% and utilisation {r.randint(12, 88)}% at last audit."
        )
    if kind == 1:
        return (
            f"Supernet {_cidr(r, r.choice([16, 18, 20]))} is delegated to {site} ({env}) and summarised at "
            f"border-{r.randint(1, 6)}; the overlap check against {r.choice(SITES)} passed in review "
            f"{r.randint(100, 999)}, and {r.randint(0, 6)} exceptions are documented in IPAM ticket "
            f"IPAM-{r.randint(1000, 9999)}."
        )
    return (
        f"NAT pool {_cidr(r, 28)} serves outbound traffic for {r.choice(APPS)} in {site}, supports "
        f"{r.randint(500, 60000)} concurrent translations, timeout {r.choice([60, 300, 3600])}s, and is monitored "
        f"with an alert at {r.choice([70, 80, 90])}% port exhaustion."
    )


def compute_fact(r: random.Random) -> str:
    kind = r.randrange(3)
    if kind == 0:
        return (
            f"Cluster {r.choice(SITES)[:3].upper()}-{r.choice(ENVS).upper()}-{r.randint(1, 9)} has {r.randint(4, 32)} hosts "
            f"of model {r.choice(['R760', 'DL380g11', 'SR650v3'])} with {r.choice([64, 96, 128])} cores and "
            f"{r.choice([512, 1024, 2048])} GB RAM each; HA admission control reserves {r.choice([10, 15, 25])}% and "
            f"CPU overcommit is capped at {r.choice([2, 3, 4])}:1."
        )
    if kind == 1:
        return (
            f"Workload {r.choice(APPS)}-{r.choice(TIERS)} runs {r.randint(2, 40)} VMs of size "
            f"{r.choice(['4vCPU/16GB', '8vCPU/32GB', '16vCPU/64GB'])} in anti-affinity group "
            f"AG-{r.randint(1, 60)}, storage policy {r.choice(['gold', 'silver', 'bronze'])} and backup tier "
            f"{r.choice(['T1-hourly', 'T2-daily', 'T3-weekly'])} with RPO {r.choice([1, 4, 24])}h."
        )
    return (
        f"Datastore {r.choice(SITES)[:3].lower()}-ds{r.randint(1, 60):02d} provides {r.randint(20, 400)} TB usable on "
        f"{r.choice(['NVMe', 'SAS SSD', 'hybrid'])} with {r.choice(['RAID-6', 'erasure coding 4+2', 'mirror'])}; "
        f"thin-provisioning ratio {r.choice([1.2, 1.5, 2.0])}:1 and an alert at {r.choice([75, 80, 85])}% used."
    )


def cover_fact(r: random.Random) -> str:
    kind = r.randrange(3)
    if kind == 0:
        return (
            f"Document HLD-{r.randint(100, 999)} version {r.randint(0, 3)}.{r.randint(0, 9)} is owned by "
            f"{r.choice(OWNERS)}, reviewed on 202{r.randint(6, 8)}-{r.randint(1, 12):02d}-{r.randint(1, 28):02d}, "
            f"classified {r.choice(['Internal', 'Confidential'])} and applies to {r.choice(SITES)} and {r.choice(SITES)}."
        )
    if kind == 1:
        return (
            f"Requirement R-{r.randint(1, 400):03d}: the {r.choice(TIERS)} tier must tolerate loss of "
            f"{r.choice(['one host', 'one rack', 'one site'])} with recovery inside {r.choice([5, 15, 60, 240])} minutes "
            f"and no more than {r.choice([0, 1, 5])} minutes of data loss."
        )
    return (
        f"Assumption A-{r.randint(1, 120):03d}: {r.choice(SITES)} provides {r.choice([2, 3, 4])} diverse carrier paths "
        f"and {r.choice([10, 25, 100])} Gbit/s of committed bandwidth; any change is raised with {r.choice(OWNERS)}."
    )


MAKERS = {
    "network": network_fact,
    "addressing": addressing_fact,
    "compute": compute_fact,
    "cover": cover_fact,
}


def generate(pages: int, seed: int) -> tuple[list[dict], list[dict], str]:
    r = random.Random(seed)
    plan: list[str] = []
    for topic, share in TOPIC_SHARE.items():
        plan += [topic] * round(pages * share)
    plan = (plan + ["network"] * pages)[:pages]
    facts: list[dict] = []
    docs: list[dict] = []
    md = ["# Meridian Private Cloud: High-Level Design (SYNTHETIC)\n"]
    fid = 0
    for n, topic in enumerate(plan, start=1):
        section = r.choice(TOPIC_TITLES[topic])
        page_facts = []
        for _ in range(FACTS_PER_PAGE):
            fid += 1
            f = {
                "id": f"F{fid:05d}",
                "page": n,
                "topic": topic,
                "section": section,
                "text": MAKERS[topic](r),
            }
            facts.append(f)
            page_facts.append(f)
        body = "\n\n".join(f"- ({f['id']}) {f['text']}" for f in page_facts)
        md.append(f"\n## Page {n}: {section} [{topic}]\n\n{body}\n")
        docs.append(
            {
                "id": f"p{n:04d}",
                "page": n,
                "topic": topic,
                "title": f"{section} (page {n})",
                "content": " ".join(f["text"] for f in page_facts),
            }
        )
    return facts, docs, "".join(md)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--pages", type=int, default=180)
    ap.add_argument("--seed", type=int, default=42)
    args = ap.parse_args()
    facts, docs, md = generate(args.pages, args.seed)
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "design_document.md").write_text(md)
    (OUT / "facts.jsonl").write_text("".join(json.dumps(f) + "\n" for f in facts))
    (OUT / "pages.jsonl").write_text("".join(json.dumps(d) + "\n" for d in docs))
    chars = sum(len(json.dumps(f)) for f in facts)
    print(f"{len(docs)} pages, {len(facts)} facts, ~{chars // 4:,} tokens (chars/4) of facts[]")


if __name__ == "__main__":
    main()
