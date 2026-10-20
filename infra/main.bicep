// apim-timeout-lab: resource-group-scoped deployment.
//
// Phase 1 (deployApps=false): Log Analytics, ACR + identity, AI Search, Foundry (GPT-6 Sol),
//   APIM (two Foundry APIs: no policy / streaming policy), ACA environment, data-plane roles.
//   Then build images with `az acr build` (see README).
// Phase 2 (deployApps=true): the app tier (web, api, worker Job).
targetScope = 'resourceGroup'

param location string = resourceGroup().location

@minLength(3)
@maxLength(12)
param namePrefix string = 'apimtlab'

@allowed(['Developer', 'StandardV2'])
param apimSku string = 'Developer'

param apimPublisherEmail string
param apimPublisherName string = 'apim-timeout-lab'
param deployApps bool = false
param imageTag string = 'latest'

param modelName string = 'gpt-6-sol'
param modelVersion string = '2026-09-22'

@allowed(['GlobalStandard', 'DataZoneStandard'])
param modelSku string = 'GlobalStandard'

@description('Model capacity in units of 1K tokens per minute.')
param modelCapacity int = 100

@allowed(['free', 'basic'])
param searchSku string = 'basic'

@description('AI Search can live in another region when Sweden Central has no capacity.')
param searchLocation string = location

// Retry policy of the worker's LLM client. Placeholder (single attempt) until the customer's settings are known.
param llmMaxAttempts int = 1
param llmRetryBackoffSeconds int = 5

@secure()
param labPassword string

@secure()
param internalToken string

var suffix = take(uniqueString(resourceGroup().id), 5)
var apimName = '${namePrefix}-apim-${suffix}'
var foundryName = '${namePrefix}-fdy-${suffix}'

var acrPullRole = '7f951dda-4ed3-4680-a7ca-43fe172d538d'

// ---- Observability: ACA console logs (results) and APIM gateway logs (metadata only)
resource law 'Microsoft.OperationalInsights/workspaces@2023-09-01' = {
  name: '${namePrefix}-law-${suffix}'
  location: location
  properties: {
    sku: { name: 'PerGB2018' }
    retentionInDays: 30
  }
}

// ---- Registry + one user-assigned identity shared by web, api and worker (lab simplification).
// Needs permission to create role assignments (Owner or User Access Administrator) on the resource group.
resource acr 'Microsoft.ContainerRegistry/registries@2023-07-01' = {
  name: replace('${namePrefix}acr${suffix}', '-', '')
  location: location
  sku: { name: 'Basic' }
  properties: { adminUserEnabled: false }
}

resource identity 'Microsoft.ManagedIdentity/userAssignedIdentities@2023-01-31' = {
  name: '${namePrefix}-id-${suffix}'
  location: location
}

resource acrPull 'Microsoft.Authorization/roleAssignments@2022-04-01' = {
  name: guid(acr.id, identity.id, acrPullRole)
  scope: acr
  properties: {
    principalId: identity.properties.principalId
    principalType: 'ServicePrincipal'
    roleDefinitionId: subscriptionResourceId('Microsoft.Authorization/roleDefinitions', acrPullRole)
  }
}

// ---- AI Search for the ai_search tool (Entra auth for the apps; the admin key only seeds the index)
resource search 'Microsoft.Search/searchServices@2024-06-01-preview' = {
  name: '${namePrefix}-search-${suffix}'
  location: searchLocation
  sku: { name: searchSku }
  properties: {
    replicaCount: 1
    partitionCount: 1
    hostingMode: 'default'
    authOptions: { aadOrApiKey: { aadAuthFailureMode: 'http401WithBearerChallenge' } }
  }
}

// ---- Microsoft Foundry (AIServices) with the GPT-6 Sol deployment. Key auth is off: callers use Entra
// tokens (the worker directly, APIM through its own identity).
resource foundry 'Microsoft.CognitiveServices/accounts@2025-06-01' = {
  name: foundryName
  location: location
  kind: 'AIServices'
  sku: { name: 'S0' }
  identity: { type: 'SystemAssigned' }
  properties: {
    customSubDomainName: foundryName
    publicNetworkAccess: 'Enabled'
    disableLocalAuth: true
  }
}

resource model 'Microsoft.CognitiveServices/accounts/deployments@2025-06-01' = {
  parent: foundry
  name: modelName
  sku: { name: modelSku, capacity: modelCapacity }
  properties: {
    model: { format: 'OpenAI', name: modelName, version: modelVersion }
  }
}

// ---- Container Apps environment (Consumption)
resource env 'Microsoft.App/managedEnvironments@2024-03-01' = {
  name: '${namePrefix}-env-${suffix}'
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

// ---- APIM with the two Foundry APIs (paths 2 and 3)
module apim 'apim.bicep' = {
  name: 'apim'
  params: {
    name: apimName
    location: location
    publisherEmail: apimPublisherEmail
    publisherName: apimPublisherName
    sku: apimSku
    foundryName: foundry.name
    foundryEndpoint: 'https://${foundry.name}.openai.azure.com'
    logAnalyticsId: law.id
  }
}

// ---- App tier (phase 2)
module apps 'apps.bicep' = if (deployApps) {
  name: 'apps'
  params: {
    location: location
    envId: env.id
    registryServer: acr.properties.loginServer
    identityId: identity.id
    identityClientId: identity.properties.clientId
    identityPrincipalId: identity.properties.principalId
    namePrefix: namePrefix
    suffix: suffix
    imageTag: imageTag
    searchName: search.name
    foundryName: foundry.name
    modelName: model.name
    apimName: apim.outputs.name
    apimUrl: apim.outputs.gatewayUrl
    llmMaxAttempts: llmMaxAttempts
    llmRetryBackoffSeconds: llmRetryBackoffSeconds
    labPassword: labPassword
    internalToken: internalToken
    envDefaultDomain: env.properties.defaultDomain
  }
  dependsOn: [acrPull]
}

output acrName string = acr.name
output apimName string = apim.outputs.name
output apimGatewayUrl string = apim.outputs.gatewayUrl
output logAnalyticsName string = law.name
output searchName string = search.name
output searchEndpoint string = 'https://${search.name}.search.windows.net'
output foundryName string = foundry.name
output foundryEndpoint string = 'https://${foundry.name}.openai.azure.com'
output webUrl string = deployApps ? apps!.outputs.webUrl : ''
output workerJobName string = deployApps ? apps!.outputs.workerJobName : ''
