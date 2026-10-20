// ACA environment (Consumption) + manual-trigger Job (no ingress). The job is created only when
// deployJob is true, i.e. after the client image exists in ACR.
param envName string
param jobName string
param location string
param logAnalyticsName string
param deployJob bool
param image string
param registryServer string
param identityId string
param mockBaseUrl string
param apimBaseUrl string

@secure()
param mockApiKey string

@secure()
param apimSubscriptionKey string

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

resource job 'Microsoft.App/jobs@2024-03-01' = if (deployJob) {
  name: jobName
  location: location
  identity: {
    type: 'UserAssigned'
    userAssignedIdentities: { '${identityId}': {} }
  }
  properties: {
    environmentId: env.id
    configuration: {
      triggerType: 'Manual'
      replicaTimeout: 3600
      replicaRetryLimit: 0
      manualTriggerConfig: { parallelism: 1, replicaCompletionCount: 1 }
      registries: [{ server: registryServer, identity: identityId }]
      secrets: [
        { name: 'mock-key', value: mockApiKey }
        { name: 'apim-key', value: apimSubscriptionKey }
      ]
    }
    template: {
      containers: [
        {
          name: 'client'
          image: image
          resources: { cpu: json('0.25'), memory: '0.5Gi' }
          env: [
            { name: 'MOCK_BASE_URL', value: mockBaseUrl }
            { name: 'APIM_BASE_URL', value: apimBaseUrl }
            { name: 'MOCK_API_KEY', secretRef: 'mock-key' }
            { name: 'APIM_SUBSCRIPTION_KEY', secretRef: 'apim-key' }
          ]
        }
      ]
    }
  }
}

output envName string = env.name
