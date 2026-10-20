// Log Analytics workspace: ACA console logs (client results) and APIM gateway logs (metadata only).
param name string
param location string

resource law 'Microsoft.OperationalInsights/workspaces@2023-09-01' = {
  name: name
  location: location
  properties: {
    sku: { name: 'PerGB2018' }
    retentionInDays: 30
  }
}

output name string = law.name
output id string = law.id
