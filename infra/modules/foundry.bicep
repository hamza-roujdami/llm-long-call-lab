// Microsoft Foundry resource (AIServices) with a GPT-6 Sol deployment (no project needed).
// Local (key) auth is disabled: callers use Entra tokens (workers directly, APIM via its identity).
param name string
param location string
param modelName string = 'gpt-6-sol'
param modelVersion string = '2026-09-22'

@allowed(['GlobalStandard', 'DataZoneStandard'])
param deploymentSku string = 'GlobalStandard'

@description('Capacity in units of 1K tokens per minute.')
param capacity int = 100

resource foundry 'Microsoft.CognitiveServices/accounts@2025-06-01' = {
  name: name
  location: location
  kind: 'AIServices'
  sku: { name: 'S0' }
  identity: { type: 'SystemAssigned' }
  properties: {
    customSubDomainName: name
    publicNetworkAccess: 'Enabled'
    disableLocalAuth: true
  }
}

resource model 'Microsoft.CognitiveServices/accounts/deployments@2025-06-01' = {
  parent: foundry
  name: modelName
  sku: { name: deploymentSku, capacity: capacity }
  properties: {
    model: { format: 'OpenAI', name: modelName, version: modelVersion }
  }
}

output name string = foundry.name
output endpoint string = 'https://${foundry.name}.openai.azure.com'
output deployment string = model.name
