#!/usr/bin/env bash
# Start the long-call matrix as an execution of the worker Job.
#   infra/run-matrix.sh <image-tag> max-output-tokens=N [confirm-spend] [repeat=2] [paths=direct,apim-stream] ...
# Without `confirm-spend` it is a DRY RUN: the job only prints the plan (no model calls, no cost).
# A start with overrides replaces the job's environment, so the full environment is passed here.
set -euo pipefail
cd "$(dirname "$0")/.."
set -a && . ./.env && set +a
TAG=${1:?image tag, e.g. the TAG printed by the deploy step}; shift
RG=rg-$NAME_PREFIX
SUB=$AZURE_SUBSCRIPTION_ID

OUT=$(az deployment group list -g "$RG" --subscription "$SUB" \
  --query "[?properties.outputs.workerJobName.value!=null && properties.outputs.acrName.value!=null]|[0].properties.outputs" -o json)
val() { echo "$OUT" | python3 -c "import sys,json; print(json.load(sys.stdin)['$1']['value'])"; }
JOB=$(val workerJobName); ACR=$(val acrName)
IDENTITY_CLIENT_ID=$(az identity list -g "$RG" --subscription "$SUB" --query "[0].clientId" -o tsv)

az containerapp job start -n "$JOB" -g "$RG" --subscription "$SUB" --container-name worker \
  --image "$ACR.azurecr.io/worker:$TAG" --args matrix "$@" \
  --env-vars "FOUNDRY_ENDPOINT=$(val foundryEndpoint)" "APIM_URL=$(val apimGatewayUrl)" \
  "APIM_KEY=secretref:apim-key" "MODEL=gpt-6-sol" "AZURE_CLIENT_ID=$IDENTITY_CLIENT_ID" \
  "LLM_READ_TIMEOUT_S=3600" --query name -o tsv
