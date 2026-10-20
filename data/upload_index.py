"""Create the `design-pages` index in Azure AI Search and upload the (generated) synthetic pages.

  python data/upload_index.py --search-name <name> --resource-group <rg> [--subscription <id>]

Uses the service admin key fetched with the Azure CLI (never stored). The apps themselves read
the index with managed identity (Search Index Data Reader).
"""

import argparse
import subprocess

import httpx
from generate_synthetic_docs import generate

API = "2024-07-01"
INDEX = "design-pages"

INDEX_DEF = {
    "name": INDEX,
    "fields": [
        {"name": "id", "type": "Edm.String", "key": True, "filterable": True},
        {
            "name": "page",
            "type": "Edm.Int32",
            "filterable": True,
            "sortable": True,
            "retrievable": True,
        },
        {
            "name": "topic",
            "type": "Edm.String",
            "filterable": True,
            "facetable": True,
            "retrievable": True,
        },
        {"name": "title", "type": "Edm.String", "searchable": True, "retrievable": True},
        {"name": "content", "type": "Edm.String", "searchable": True, "retrievable": True},
    ],
}


def admin_key(name: str, rg: str, subscription: str | None) -> str:
    cmd = [
        "az",
        "search",
        "admin-key",
        "show",
        "--service-name",
        name,
        "-g",
        rg,
        "--query",
        "primaryKey",
        "-o",
        "tsv",
    ]
    if subscription:
        cmd += ["--subscription", subscription]
    return subprocess.run(cmd, check=True, capture_output=True, text=True).stdout.strip()


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--search-name", required=True)
    ap.add_argument("--resource-group", required=True)
    ap.add_argument("--subscription")
    args = ap.parse_args()

    base = f"https://{args.search_name}.search.windows.net"
    headers = {"api-key": admin_key(args.search_name, args.resource_group, args.subscription)}
    _, docs, _ = generate(pages=180, seed=42)  # same synthetic document the worker image generates
    with httpx.Client(headers=headers, timeout=60) as http:
        r = http.put(f"{base}/indexes/{INDEX}?api-version={API}", json=INDEX_DEF)
        r.raise_for_status()
        for i in range(0, len(docs), 100):
            batch = [{"@search.action": "mergeOrUpload", **d} for d in docs[i : i + 100]]
            r = http.post(
                f"{base}/indexes/{INDEX}/docs/index?api-version={API}", json={"value": batch}
            )
            r.raise_for_status()
        r = http.post(
            f"{base}/indexes/{INDEX}/docs/search?api-version={API}",
            json={"search": "BGP max-prefix", "top": 1, "select": "page,title"},
        )
        r.raise_for_status()
        print(
            f"uploaded {len(docs)} pages to {args.search_name}/{INDEX}; sample query -> {r.json()['value']}"
        )


if __name__ == "__main__":
    main()
