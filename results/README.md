# Results

**Status: no live runs yet.** Every "Observed" cell is empty until a run is executed against deployed
resources. Raw data lives next to this file as `<scenario>-<utc>.csv` (schema: [template.csv](template.csv)).

Labels: **expected** = stated in Microsoft Learn (cited); **observed** = measured in our runs (run id +
CSV). Do not put an Azure-behaviour claim in either column without its source.

| # | Scenario | Hyp. | Expected (source) | Observed (run id / CSV) | Verdict |
|---|----------|------|-------------------|-------------------------|---------|
| 1 | `direct-silent-300` | H4 | No documented limit for ACA Job → ACI that we have verified; this run establishes the baseline. | _not run_ | |
| 2 | `direct-silent-450` | H4 | As above. | _not run_ | |
| 3 | `apim-silent-300` | H1 | `forward-request` `timeout` is the wait for response headers; values > 240 s "may not be honoured" because the network infrastructure can drop idle connections ([forward-request](https://learn.microsoft.com/azure/api-management/forward-request-policy)). | _not run_ | |
| 4 | `apim-stream-450` | H2 | With `buffer-response="false"` each chunk is returned to the caller immediately; chunks every 10 s stay well inside the 4-minute idle window ([forward-request](https://learn.microsoft.com/azure/api-management/forward-request-policy), [SSE guidance](https://learn.microsoft.com/azure/api-management/how-to-server-sent-events)). | _not run_ | |
| 5 | `apim-gap-300` | H3 | Connections idle ≥ 4 min need a keep-alive; the Azure Load Balancer used in the APIM infrastructure enforces a 4-minute idle timeout ([SSE guidance](https://learn.microsoft.com/azure/api-management/how-to-server-sent-events)). A 300 s gap may therefore be dropped. | _not run_ | |
| 6 | `apim-stream-buffered-450` | H2 | With `buffer-response="true"` (default) chunks are buffered (8 KB, unless end of stream is detected) before being returned ([forward-request](https://learn.microsoft.com/azure/api-management/forward-request-policy)); our chunks are tiny, so expect coalesced delivery. | _not run_ | |
| 7 | `apim-stream-parallel3-450` | H2 | No documented per-connection limit relevant here; control for concurrency. | _not run_ | |
| C1 | `direct-stream-450` (control) | H4 | As row 1. | _not run_ | |
| C2 | `apim-silent-200` (control) | H1 | Below the documented 240 s threshold, expect success. | _not run_ | |
| C3 | `apim-gap-200` (control) | H3 | Below the 4-minute idle window, expect success. | _not run_ | |

Verdict vocabulary: `supported`, `refuted`, `inconclusive` (and why).

## Reading a CSV

- `outcome`: `completed` (2xx + completion marker), `truncated` (2xx, then the connection ended/failed
  without the marker), `http_error` (non-2xx; `error_detail` has the body head), `error` (no response).
- `ttfh_s` time to response headers; `ttfb_s` first body byte; `longest_gap_s` largest gap between body
  chunks; `last_chunk_s` vs `total_s` shows how long the connection was silent before it ended.
- `client_request_id` is sent as `x-client-request-id`; `server_request_ids` lists correlation headers
  returned (APIM and the mock). Use them to find the matching APIM gateway log row.

## Run log

| Run id | Scenario | Date (UTC) | APIM SKU / region | CSV | Notes |
|--------|----------|------------|-------------------|-----|-------|
| | | | | | |
