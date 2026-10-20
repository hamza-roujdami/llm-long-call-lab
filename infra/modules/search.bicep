// Azure AI Search for the `ai_search` tool (keyword/BM25 over the synthetic design document).
// Entra (RBAC) auth is enabled for the apps; the API key stays enabled only so the index can be
// seeded from a workstation with `az search admin-key show` (see data/upload_index.py).
param name string
param location string

@allowed(['free', 'basic'])
param sku string = 'basic'

resource search 'Microsoft.Search/searchServices@2024-06-01-preview' = {
  name: name
  location: location
  sku: { name: sku }
  properties: {
    replicaCount: 1
    partitionCount: 1
    hostingMode: 'default'
    authOptions: { aadOrApiKey: { aadAuthFailureMode: 'http401WithBearerChallenge' } }
  }
}

output name string = search.name
output endpoint string = 'https://${search.name}.search.windows.net'
