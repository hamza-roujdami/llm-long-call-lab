using './main.bicep'

// Secrets come from the environment (see .env.example); nothing sensitive is stored here.
param namePrefix = readEnvironmentVariable('NAME_PREFIX', 'apimtlab')
param apimSku = readEnvironmentVariable('APIM_SKU', 'Developer')
param apimPublisherEmail = readEnvironmentVariable('APIM_PUBLISHER_EMAIL')
param mockApiKey = readEnvironmentVariable('MOCK_API_KEY')
// Phase 1 leaves this false; set DEPLOY_COMPUTE=true once images are in ACR.
param deployCompute = readEnvironmentVariable('DEPLOY_COMPUTE', 'false') == 'true'
