# Results

One CSV per run (schema = the columns in `worker/results.py`), plus the table in the top-level
[README](../README.md#run-matrix-and-results-table). Matrix runs append to `runs.csv`.

| File | What it is |
|---|---|
| `runs.csv` | Real-model matrix (calibration + 12 cells). **Not run yet** (cost guard). |
| `smoke-pipeline-*.csv` | Observed: tiny capped pipeline runs on GPT-6 Sol (reasoning low), to verify the agents and telemetry. Not timeout evidence. |
| `mock-probe-*.csv` | Observed on a **mock backend** (silent on purpose), harness since removed (commit `00e7732`). Older schema. Not GPT-6 Sol evidence. |

Labels: **expected** = stated in Microsoft Learn (cited in the README); **observed** = measured in our runs.
Never record an Azure-behaviour claim without one of the two.

## Run log

| Run id | Cell (path / stream / prompt) | Date (UTC) | APIM SKU / region | CSV | Verdict (supported / refuted / inconclusive) |
|---|---|---|---|---|---|
| | | | | | |
