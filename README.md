# apim-timeout-lab

Lab to reproduce long-call behaviour on **ACA Job → APIM → model**, so we can advise a customer.
Lab only; no customer data. Private repo, no LICENSE.

**Status: scaffold only.** Nothing has been deployed and no live run has been made, so there are no
"observed" results yet (see [results/README.md](results/README.md)). Azure deployment needs explicit approval, preceded by a
resource plan and cost estimate.

## Hypotheses (to test, not facts)

| | Hypothesis |
|--|-----------|
| H1 | APIM cuts calls that are silent for ~230–240 s (`forward-request` waits for response headers). |
| H2 | Streaming with `buffer-response="false"` avoids that. |
| H3 | Even when streaming, a gap of 4+ min between chunks can be dropped by the load balancer inside APIM, which matters for reasoning models. |
| H4 | Egress from an ACA Job to a backend is not the limiting hop. |

What Learn says (**expected**, not yet confirmed by us):
- `forward-request` `timeout` = wait for response *headers*; values > 240 s may not be honoured; `buffer-response="false"` relays each chunk immediately ([forward-request policy](https://learn.microsoft.com/azure/api-management/forward-request-policy)).
- Long-running connections are supported in classic and v2 tiers but not Consumption; connections idle ≥ 4 min need a keep-alive because of the Azure Load Balancer idle timeout; avoid `validate-content`, caching and body logging on streaming APIs ([SSE guidance](https://learn.microsoft.com/azure/api-management/how-to-server-sent-events)).

## Layout

| Path | Purpose |
|------|---------|
| [mock/](mock) | FastAPI fake model + Dockerfile, for **ACI** (not Container Apps/App Service: they add their own timeouts) |
| [client/](client) | Measurement client for a Container Apps Job (no ingress); optional real-model mode via the OpenAI SDK |
| [apim/](apim) | Policy variants: [streaming.xml](apim/streaming.xml) (buffering off), [buffered.xml](apim/buffered.xml) (buffering on) |
| [infra/](infra) | Bicep: Log Analytics, ACR, ACA env + Job, APIM (Developer or StandardV2), ACI mock |
| [results/](results) | CSVs + [README table](results/README.md) (expected vs observed) |
| [tests/](tests) | Offline tests (no Azure) |

## Mock endpoints

All end with a completion marker (`data: [DONE]`, or `"done":true` for `/silent`) so a clean finish is
distinguishable from a dropped connection. `x-mock-key` is required when `MOCK_API_KEY` is set. TCP keepalive is not enabled on purpose.

| Endpoint | Behaviour |
|----------|-----------|
| `/silent?delay=N` | Nothing (not even headers) for N s, then JSON. |
| `/stream?total=N&interval=M` | A chunk immediately, then one every M s for N s. |
| `/gap?first=10&gap=300&then=30[&interval=1]` | Chunks for `first` s, total silence for `gap` s, then chunks for `then` s. |

## Run matrix

Scenario names are accepted by `python -m client.run --scenario <name>` (list: `--list`).

| # | Scenario | Path | Client | Tests |
|---|----------|------|--------|-------|
| 1 | `direct-silent-300` | Job → mock | silent 300 s | H4 |
| 2 | `direct-silent-450` | Job → mock | silent 450 s | H4 |
| 3 | `apim-silent-300` | Job → APIM → mock | silent 300 s | H1 |
| 4 | `apim-stream-450` | streaming policy | `/stream` total 450, every 10 s | H2 |
| 5 | `apim-gap-300` | streaming policy | `/gap` first 10, gap 300, then 30 | H3 |
| 6 | `apim-stream-buffered-450` | buffering policy | `/stream` total 450 | H2 |
| 7 | `apim-stream-parallel3-450` | streaming policy | 3 parallel `/stream` 450 | H2 |

Optional controls: `direct-stream-450`, `apim-silent-200`, `apim-gap-200`. Custom runs:
`python -m client.run --target apim --endpoint gap --param gap=240 --apim-variant stream`.
Real model: `python -m client.run --openai --target apim [--no-stream]` (set `OPENAI_*` in `.env`).
Retries are off; the client read timeout (900 s) is longer than every scenario so the client is never the limiter.

## Local use (no Azure)

```bash
python3.13 -m venv .venv && .venv/bin/pip install pytest ruff fastapi uvicorn httpx pydantic-settings openai
.venv/bin/python -m pytest -q && .venv/bin/ruff check .
MOCK_API_KEY=k .venv/bin/uvicorn mock.app:app --port 8000 &
MOCK_BASE_URL=http://127.0.0.1:8000 MOCK_API_KEY=k .venv/bin/python -m client.run \
  --target direct --endpoint gap --param first=2 --param gap=3 --param then=2 --param interval=1
```

Verified locally: tests, lint, Bicep compile (`az bicep build`), and a client↔mock run covering silent, stream, gap
(longest gap measured as configured) and a connection killed mid-stream (classified `truncated`).
**Not verified:** Docker image builds (no daemon was available), any deployment, APIM/ACA behaviour.

## Deployment plan (requires approval; nothing has been run)

Copy `.env.example` to `.env` and fill it in. Planned resources, one resource group in the chosen region:
Log Analytics, ACR Basic, user-assigned identity (AcrPull), ACA environment (Consumption) + manual Job,
APIM (Developer or StandardV2), ACI container group (1 vCPU / 1 GB, public IP + DNS label, port 8000).
APIM Developer provisioning is slow and APIM is the main cost driver; produce a regional cost estimate
(Azure pricing calculator) and a `what-if` before approval. The mock is publicly reachable on plain HTTP
and guarded only by the shared `x-mock-key`: acceptable for a lab with synthetic data, delete it afterwards.

```bash
set -a; source .env; set +a
az group create -n "rg-$NAME_PREFIX" -l "$AZURE_LOCATION"
az deployment group what-if -g "rg-$NAME_PREFIX" -p infra/main.bicepparam      # review
az deployment group create  -g "rg-$NAME_PREFIX" -p infra/main.bicepparam      # phase 1
az acr build -r <acr> -t mock:latest   -f mock/Dockerfile .
az acr build -r <acr> -t client:latest -f client/Dockerfile .
DEPLOY_COMPUTE=true az deployment group create -g "rg-$NAME_PREFIX" -p infra/main.bicepparam   # phase 2
az containerapp job start -n <job> -g "rg-$NAME_PREFIX" --container-name client \
  --args "--scenario" "apim-stream-450"
```

(`<acr>`, `<job>` come from the deployment outputs.)

## Getting results out of the Job

Job file systems are ephemeral, so the client also prints one `RESULT {json}` line per call to stdout (Log Analytics).
Rebuild the CSV with `python -m client.logs_to_csv results/<name>.csv < logs.txt`, or query
`ContainerAppConsoleLogs_CL` for lines starting with `RESULT` (column names unverified; adjust to the workspace schema).
APIM gateway logs (metadata only, no bodies) go to the same workspace; correlate with `client_request_id`.
Record each run in [results/README.md](results/README.md).

## Cleanup

`az group delete -n "rg-$NAME_PREFIX"` removes everything (APIM soft-delete may retain the name; purge if needed).
