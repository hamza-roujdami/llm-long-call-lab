using './main.bicep'

// Secrets come from the environment (see .env.example); nothing sensitive is stored here.
param namePrefix = readEnvironmentVariable('NAME_PREFIX', 'apimtlab')
param apimSku = readEnvironmentVariable('APIM_SKU', 'Developer')
param apimPublisherEmail = readEnvironmentVariable('APIM_PUBLISHER_EMAIL')
param mockApiKey = readEnvironmentVariable('MOCK_API_KEY')
param labPassword = readEnvironmentVariable('LAB_PASSWORD')
param internalToken = readEnvironmentVariable('INTERNAL_TOKEN')
param modelSku = readEnvironmentVariable('MODEL_SKU', 'GlobalStandard')
param modelCapacity = int(readEnvironmentVariable('MODEL_CAPACITY', '100'))
param searchSku = readEnvironmentVariable('SEARCH_SKU', 'basic')
param searchLocation = readEnvironmentVariable('SEARCH_LOCATION', readEnvironmentVariable('AZURE_LOCATION', 'swedencentral'))
param llmMaxAttempts = int(readEnvironmentVariable('LLM_MAX_ATTEMPTS', '1'))
param llmRetryBackoffSeconds = int(readEnvironmentVariable('LLM_RETRY_BACKOFF_S', '5'))
// Phase 1 leaves this false; set DEPLOY_COMPUTE=true once images are in ACR.
param deployCompute = readEnvironmentVariable('DEPLOY_COMPUTE', 'false') == 'true'
param imageTag = readEnvironmentVariable('IMAGE_TAG', 'latest')
