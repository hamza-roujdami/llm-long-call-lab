"""Generate a SYNTHETIC high-level design (HLD) as search chunks. Everything is fictional (seeded RNG).

The shape mirrors a typical RAG corpus: chunks of ~2,000 characters, each with a filename, page number,
section path and type (prose | table | iac). Two groups:
  in_slice=true   the "starting slice" the orchestrator puts in the planner's facts[] (~100K tokens)
  in_slice=false  only reachable through the ai_search tool: the segment (VLAN) table, the cluster
                  role table with host counts, the subscription table, and extra pages

Output: data/synthetic_docs/hld.jsonl (git-ignored, generated at image build)

  python data/generate_synthetic_docs.py [--slice 200] [--extra 120] [--seed 42]
"""

import argparse
import json
import random
from pathlib import Path

OUT = Path(__file__).parent / "synthetic_docs"
CHUNK_CHARS = 2000
DOMAIN_SHARE = {
    "cover": 0.07,
    "network": 0.33,
    "addressing": 0.27,
    "compute": 0.25,
    "security": 0.08,
}
TYPE_SHARE = {"prose": 0.6, "table": 0.3, "iac": 0.1}
FILES = {
    "cover": "HLD-00-Overview.docx",
    "network": "HLD-10-Network.docx",
    "addressing": "HLD-20-Addressing.docx",
    "compute": "HLD-30-Compute.docx",
    "security": "HLD-40-Security.docx",
}
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


def security_fact(r: random.Random) -> str:
    return (
        f"Certificate for {r.choice(APPS)}.{r.choice(SITES).lower()}.example is issued by the internal CA "
        f"with key size {r.choice([2048, 3072, 4096])}, valid {r.choice([12, 24, 36])} months and renewed "
        f"{r.choice([30, 45, 60])} days before expiry; owner {r.choice(OWNERS)}."
    )


MAKERS = {
    "network": network_fact,
    "addressing": addressing_fact,
    "compute": compute_fact,
    "cover": cover_fact,
    "security": security_fact,
}


def _table(header: list[str], rows: list[list[str]]) -> str:
    lines = ["| " + " | ".join(header) + " |", "|" + "---|" * len(header)]
    lines += ["| " + " | ".join(str(c) for c in row) + " |" for row in rows]
    return "\n".join(lines)


def _prose(r: random.Random, domain: str) -> str:
    out, size = [], 0
    while size < CHUNK_CHARS:
        t = MAKERS[domain](r)
        out.append(t)
        size += len(t) + 1
    return " ".join(out)


def _table_chunk(r: random.Random, domain: str) -> str:
    rows: list[list[str]] = []
    if domain == "network":
        header = ["Rule", "Action", "Protocol/Port", "Source", "Destination", "Logging"]
        while len(_table(header, rows)) < CHUNK_CHARS:
            rows.append([f"FW-{r.randint(1000, 9999)}", r.choice(["permit", "deny"]),
                         f"{r.choice(['tcp', 'udp'])}/{r.choice([443, 8443, 5432, 1433, 9092, 6379])}",
                         _cidr(r, 24), _cidr(r, 26), r.choice(["full", "drop-only", "sampled"])])  # fmt: skip
    elif domain == "compute":
        header = ["Cluster", "Hosts", "Cores/host", "RAM GB/host", "Overcommit", "Storage policy"]
        while len(_table(header, rows)) < CHUNK_CHARS:
            rows.append([f"{r.choice(SITES)[:3].upper()}-{r.choice(ENVS).upper()}-{r.randint(1, 9)}",
                         r.randint(4, 32), r.choice([64, 96, 128]), r.choice([512, 1024, 2048]),
                         f"{r.choice([2, 3, 4])}:1", r.choice(["gold", "silver", "bronze"])])  # fmt: skip
    elif domain == "security":
        header = [
            "Certificate",
            "Issuer",
            "Key size",
            "Validity (months)",
            "Renew before (days)",
            "Owner",
        ]
        while len(_table(header, rows)) < CHUNK_CHARS:
            rows.append([f"{r.choice(APPS)}.{r.choice(SITES).lower()}.example", "Internal CA",
                         r.choice([2048, 3072, 4096]), r.choice([12, 24, 36]), r.choice([30, 45, 60]),
                         r.choice(OWNERS)])  # fmt: skip
    else:
        header = ["Subnet", "CIDR", "Gateway", "DHCP", "Purpose", "Site"]
        while len(_table(header, rows)) < CHUNK_CHARS:
            rows.append([f"snet-{r.choice(TIERS)}-{r.randint(1, 40):02d}", _cidr(r, r.choice([24, 26])),
                         ".1", r.choice(["off", "8h lease", "relay"]), r.choice(TIERS), r.choice(SITES)])  # fmt: skip
    return _table(header, rows)


def _iac_chunk(r: random.Random, domain: str) -> str:
    lines: list[str] = []
    if domain == "compute":
        lines.append("vms:")
        while sum(map(len, lines)) < CHUNK_CHARS:
            lines += [f"  - name: {r.choice(APPS)}-{r.choice(TIERS)}-{r.randint(1, 40):02d}",
                      f"    size: {r.choice(['4vCPU-16GB', '8vCPU-32GB', '16vCPU-64GB'])}",
                      f"    cluster: {r.choice(SITES)[:3].upper()}-{r.choice(ENVS).upper()}-{r.randint(1, 9)}",
                      f"    backup: {r.choice(['T1-hourly', 'T2-daily', 'T3-weekly'])}"]  # fmt: skip
    elif domain == "network":
        lines.append("firewall_rules:")
        while sum(map(len, lines)) < CHUNK_CHARS:
            lines += [f"  - id: FW-{r.randint(1000, 9999)}", f"    action: {r.choice(['permit', 'deny'])}",
                      f"    port: {r.choice([443, 8443, 5432, 1433, 9092])}", f"    src: {_cidr(r, 24)}",
                      f"    dst: {_cidr(r, 26)}"]  # fmt: skip
    else:
        lines.append("subnets:")
        while sum(map(len, lines)) < CHUNK_CHARS:
            lines += [f"  - name: snet-{r.choice(TIERS)}-{r.randint(1, 40):02d}",
                      f"    cidr: {_cidr(r, r.choice([24, 26]))}", f"    site: {r.choice(SITES)}"]  # fmt: skip
    return "\n".join(lines)


def _chunk(r: random.Random, n: int, domain: str, kind: str, page: int, in_slice: bool) -> dict:
    content = {"prose": _prose, "table": _table_chunk, "iac": _iac_chunk}[kind]
    title = r.choice(TOPIC_TITLES.get(domain, ["Certificates"]))
    return {
        "id": f"c{n:04d}",
        "content": content(r, domain) if kind != "prose" else _prose(r, domain),
        "filename": FILES[domain],
        "page_number": page,
        "section_path": f"{domain.capitalize()} > {title}",
        "chunk_type": kind,
        "domain": domain,
        "in_slice": in_slice,
    }


def _key_chunks(r: random.Random, start: int) -> list[dict]:
    """Facts the planner can only find with ai_search: segments, cluster roles, subscriptions."""
    names = ["Core-Transit", "DMZ", "Web", "App", "Data", "Mgmt", "Backup", "Monitoring", "Identity",
             "Cache", "Queue", "Bastion", "Vendor", "Guest"]  # fmt: skip
    segs = [[100 + 10 * i, n, f"10.{20 + i}.0.0/24", "onprem" if i % 5 else "azure",
             r.choice(["servers", "network devices", "security tools", "infrastructure services"])]
            for i, n in enumerate(names)]  # fmt: skip
    seg_table = _table(["VLAN ID", "Segment name", "CIDR", "Platform", "Purpose"], segs)
    roles = [["Cluster-MGMT", "Hypervisor management", 100 + 50, r.randint(3, 5)],
             ["Cluster-VMOTION", "Live migration", 160, r.randint(3, 5)],
             ["Cluster-STORAGE", "Distributed storage", 170, r.randint(4, 8)],
             ["Cluster-WORKLOAD", "Production workloads", 120, r.randint(8, 16)]]  # fmt: skip
    role_table = _table(["Network", "Function", "VLAN ID", "Host count"], roles)
    subs = _table(["Subscription", "Hosts servers", "Purpose"],
                  [["Connectivity", "yes", "gateways, firewalls"], ["Identity", "yes", "directory services"],
                   ["Management", "yes", "monitoring, backup"], ["Data platform", "no", "PaaS only"]])  # fmt: skip
    items = [("addressing", "IP blocks", seg_table), ("compute", "Cluster roles", role_table),
             ("cover", "Subscriptions", subs)]  # fmt: skip
    return [
        {"id": f"c{start + i:04d}", "content": c, "filename": FILES[d], "page_number": 900 + i,
         "section_path": f"{d.capitalize()} > {t}", "chunk_type": "table", "domain": d, "in_slice": False}
        for i, (d, t, c) in enumerate(items)
    ]  # fmt: skip


def generate(slice_chunks: int = 200, extra_chunks: int = 120, seed: int = 42) -> list[dict]:
    r = random.Random(seed)
    chunks: list[dict] = []
    domains = [d for d, share in DOMAIN_SHARE.items() for _ in range(round(100 * share))]
    kinds = [k for k, share in TYPE_SHARE.items() for _ in range(round(100 * share))]
    page = {d: 0 for d in DOMAIN_SHARE}
    for i in range(slice_chunks + extra_chunks):
        domain = r.choice(domains)
        kind = r.choice(kinds)
        if kind == "iac" and domain in ("cover", "security"):
            kind = "prose"
        page[domain] += 1
        chunks.append(_chunk(r, len(chunks) + 1, domain, kind, page[domain], i < slice_chunks))
    chunks += _key_chunks(r, len(chunks) + 1)
    return chunks


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--slice", type=int, default=200, dest="slice_chunks")
    ap.add_argument("--extra", type=int, default=120)
    ap.add_argument("--seed", type=int, default=42)
    args = ap.parse_args()
    chunks = generate(args.slice_chunks, args.extra, args.seed)
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "hld.jsonl").write_text("".join(json.dumps(c) + "\n" for c in chunks))
    s = [c for c in chunks if c["in_slice"]]
    chars = sum(len(c["content"]) for c in s)
    print(
        f"{len(chunks)} chunks ({len(s)} in the facts slice, ~{chars:,} chars, ~{chars // 4:,} tokens est.)"
    )


if __name__ == "__main__":
    main()
