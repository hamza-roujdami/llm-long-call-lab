// Container Apps environment (Consumption) wired to Log Analytics. The apps and the worker Job live in apps.bicep.
param envName string
param location string
param logAnalyticsName string

resource law 'Microsoft.OperationalInsights/workspaces@2023-09-01' existing = {
  name: logAnalyticsName
}

resource env 'Microsoft.App/managedEnvironments@2024-03-01' = {
  name: envName
  location: location
  properties: {
    appLogsConfiguration: {
      destination: 'log-analytics'
      logAnalyticsConfiguration: {
        customerId: law.properties.customerId
        sharedKey: law.listKeys().primarySharedKey
      }
    }
  }
}

output envId string = env.id
output defaultDomain string = env.properties.defaultDomain
