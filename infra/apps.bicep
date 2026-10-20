// The app tier on the shared ACA environment:
//   web    : Next.js UI, external ingress, basic-auth guard
//   api    : FastAPI, internal ingress; POST /runs starts a worker Job execution
//   worker : manual-trigger Job: the agent pipeline (started by the api) and the long-call matrix
//            (`python -m worker.run_matrix`, started with az). 4 h replica timeout
// One user-assigned identity is shared by all three (lab simplification; see README).
param location string
param envId string
param registryServer string
param identityId string
param identityClientId string
param identityPrincipalId string
param namePrefix string
param suffix string
param imageTag string
param searchName string
param foundryName string
param modelName string
param apimName string
param apimUrl string
param llmMaxAttempts int = 1
param llmRetryBackoffSeconds int = 5

param envDefaultDomain string

@secure()
param labPassword string

@secure()
param internalToken string

var searchEndpoint = 'https://${searchName}.search.windows.net'
var foundryEndpoint = 'https://${foundryName}.openai.azure.com'
var searchIndexDataReaderRole = '1407120a-92aa-4202-b7e9-c0e197c71c8f'
var openAIUserRole = '5e0bd9bd-7b93-4f28-af87-19fc36ad61bd'

// Data-plane access for the shared identity: read the search index, call the model directly (path 1).
resource search 'Microsoft.Search/searchServices@2024-06-01-preview' existing = { name: searchName }
resource foundry 'Microsoft.CognitiveServices/accounts@2025-06-01' existing = { name: foundryName }

resource searchReader 'Microsoft.Authorization/roleAssignments@2022-04-01' = {
  name: guid(search.id, identityPrincipalId, searchIndexDataReaderRole)
  scope: search
  properties: {
    principalId: identityPrincipalId
    principalType: 'ServicePrincipal'
    roleDefinitionId: subscriptionResourceId('Microsoft.Authorization/roleDefinitions', searchIndexDataReaderRole)
  }
}

resource workerCallsFoundry 'Microsoft.Authorization/roleAssignments@2022-04-01' = {
  name: guid(foundry.id, identityPrincipalId, openAIUserRole)
  scope: foundry
  properties: {
    principalId: identityPrincipalId
    principalType: 'ServicePrincipal'
    roleDefinitionId: subscriptionResourceId('Microsoft.Authorization/roleDefinitions', openAIUserRole)
  }
}

resource apim 'Microsoft.ApiManagement/service@2024-05-01' existing = {
  name: apimName
}

resource clientSub 'Microsoft.ApiManagement/service/subscriptions@2024-05-01' existing = {
  parent: apim
  name: 'lab-client'
}

var apimKey = clientSub.listSecrets().primaryKey
var workerImage = '${registryServer}/worker:${imageTag}'

var workerEnv = [
  { name: 'AZURE_CLIENT_ID', value: identityClientId }
  { name: 'API_URL', value: 'https://${namePrefix}-api-${suffix}.internal.${envDefaultDomain}' }
  { name: 'INTERNAL_TOKEN', secretRef: 'internal-token' }
  { name: 'FOUNDRY_ENDPOINT', value: foundryEndpoint }
  { name: 'APIM_URL', value: apimUrl }
  { name: 'APIM_KEY', secretRef: 'apim-key' }
  { name: 'SEARCH_ENDPOINT', value: searchEndpoint }
  { name: 'MODEL', value: modelName }
  { name: 'LLM_MAX_ATTEMPTS', value: string(llmMaxAttempts) }
  { name: 'LLM_RETRY_BACKOFF_S', value: string(llmRetryBackoffSeconds) }
]

var registries = [{ server: registryServer, identity: identityId }]
var identity = {
  type: 'UserAssigned'
  userAssignedIdentities: { '${identityId}': {} }
}

resource worker 'Microsoft.App/jobs@2024-03-01' = {
  name: '${namePrefix}-worker-${suffix}'
  location: location
  identity: identity
  properties: {
    environmentId: envId
    configuration: {
      triggerType: 'Manual'
      replicaTimeout: 14400
      replicaRetryLimit: 0
      manualTriggerConfig: { parallelism: 1, replicaCompletionCount: 1 }
      registries: registries
      secrets: [
        { name: 'apim-key', value: apimKey }
        { name: 'internal-token', value: internalToken }
      ]
    }
    template: {
      containers: [
        {
          name: 'worker'
          image: workerImage
          resources: { cpu: json('1.0'), memory: '2Gi' }
          env: workerEnv
        }
      ]
    }
  }
}

// The api starts executions of the worker job, so it needs write access on that job only.
var contributor = 'b24988ac-6180-42a0-ab88-20f7382dd24c'
resource apiStartsWorker 'Microsoft.Authorization/roleAssignments@2022-04-01' = {
  name: guid(worker.id, identityPrincipalId, contributor)
  scope: worker
  properties: {
    principalId: identityPrincipalId
    principalType: 'ServicePrincipal'
    roleDefinitionId: subscriptionResourceId('Microsoft.Authorization/roleDefinitions', contributor)
  }
}

resource api 'Microsoft.App/containerApps@2024-03-01' = {
  name: '${namePrefix}-api-${suffix}'
  location: location
  identity: identity
  properties: {
    environmentId: envId
    configuration: {
      activeRevisionsMode: 'Single'
      ingress: { external: false, targetPort: 8080, transport: 'auto' }
      registries: registries
      secrets: [{ name: 'internal-token', value: internalToken }]
    }
    template: {
      containers: [
        {
          name: 'api'
          image: '${registryServer}/api:${imageTag}'
          resources: { cpu: json('0.5'), memory: '1Gi' }
          env: [
            { name: 'AZURE_CLIENT_ID', value: identityClientId }
            { name: 'INTERNAL_TOKEN', secretRef: 'internal-token' }
            { name: 'JOB_RESOURCE_ID', value: worker.id }
            { name: 'WORKER_IMAGE', value: workerImage }
            { name: 'WORKER_ENV_JSON', value: string(workerEnv) }
          ]
        }
      ]
      scale: { minReplicas: 1, maxReplicas: 1 }
    }
  }
  dependsOn: [apiStartsWorker, searchReader, workerCallsFoundry]
}

resource web 'Microsoft.App/containerApps@2024-03-01' = {
  name: '${namePrefix}-web-${suffix}'
  location: location
  identity: identity
  properties: {
    environmentId: envId
    configuration: {
      activeRevisionsMode: 'Single'
      ingress: { external: true, targetPort: 3000, transport: 'auto' }
      registries: registries
      secrets: [{ name: 'lab-password', value: labPassword }]
    }
    template: {
      containers: [
        {
          name: 'web'
          image: '${registryServer}/web:${imageTag}'
          resources: { cpu: json('0.5'), memory: '1Gi' }
          env: [
            { name: 'API_URL', value: 'https://${api.properties.configuration.ingress.fqdn}' }
            { name: 'LAB_PASSWORD', secretRef: 'lab-password' }
          ]
        }
      ]
      scale: { minReplicas: 1, maxReplicas: 1 }
    }
  }
}

output webUrl string = 'https://${web.properties.configuration.ingress.fqdn}'
output apiFqdn string = api.properties.configuration.ingress.fqdn
output workerJobName string = worker.name
