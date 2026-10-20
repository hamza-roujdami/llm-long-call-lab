// apim-timeout-lab: resource-group-scoped deployment.
//
// Phase 1 (deployCompute=false): Log Analytics, ACR + identity, AI Search, Foundry (GPT-6 Sol),
//   APIM (mock + Foundry APIs), ACA environment, data-plane roles.
//   Then build images with `az acr build` (see README).
// Phase 2 (deployCompute=true): ACI fake model, probe Job, and the app tier (web, api, worker Job).
targetScope = 'resourceGroup'

param location string = resourceGroup().location

@minLength(3)
@maxLength(12)
param namePrefix string = 'apimtlab'

@allowed(['Developer', 'StandardV2'])
param apimSku string = 'Developer'

param apimPublisherEmail string
param apimPublisherName string = 'apim-timeout-lab'
param deployCompute bool = false
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
param mockApiKey string

@secure()
param labPassword string

@secure()
param internalToken string

var suffix = take(uniqueString(resourceGroup().id), 5)
var acrName = replace('${namePrefix}acr${suffix}', '-', '')
var apimName = '${namePrefix}-apim-${suffix}'
var lawName = '${namePrefix}-law-${suffix}'
var searchName = '${namePrefix}-search-${suffix}'
var foundryName = '${namePrefix}-fdy-${suffix}'
var mockDnsLabel = '${namePrefix}-mock-${suffix}'
var mockUrl = 'http://${mockDnsLabel}.${location}.azurecontainer.io:8000'

module monitoring 'modules/monitoring.bicep' = {
  name: 'monitoring'
  params: { name: lawName, location: location }
}

module registry 'modules/registry.bicep' = {
  name: 'registry'
  params: { acrName: acrName, identityName: '${namePrefix}-id-${suffix}', location: location }
}

module search 'modules/search.bicep' = {
  name: 'search'
  params: { name: searchName, location: searchLocation, sku: searchSku }
}

module foundry 'modules/foundry.bicep' = {
  name: 'foundry'
  params: {
    name: foundryName
    location: location
    modelName: modelName
    modelVersion: modelVersion
    deploymentSku: modelSku
    capacity: modelCapacity
  }
}

module apim 'modules/apim.bicep' = {
  name: 'apim'
  params: {
    name: apimName
    location: location
    publisherEmail: apimPublisherEmail
    publisherName: apimPublisherName
    sku: apimSku
    backendUrl: mockUrl
    foundryName: foundry.outputs.name
    foundryEndpoint: foundry.outputs.endpoint
    logAnalyticsId: monitoring.outputs.id
    mockApiKey: mockApiKey
  }
}

module roles 'modules/roles.bicep' = {
  name: 'roles'
  params: {
    identityPrincipalId: registry.outputs.identityPrincipalId
    searchName: search.outputs.name
    foundryName: foundry.outputs.name
  }
}

module aca 'modules/aca.bicep' = {
  name: 'aca'
  params: {
    envName: '${namePrefix}-env-${suffix}'
    jobName: '${namePrefix}-probe-${suffix}'
    location: location
    logAnalyticsName: monitoring.outputs.name
    deployJob: deployCompute
    image: '${registry.outputs.loginServer}/probe:${imageTag}'
    registryServer: registry.outputs.loginServer
    identityId: registry.outputs.identityId
    mockBaseUrl: mockUrl
    apimBaseUrl: apim.outputs.gatewayUrl
    mockApiKey: mockApiKey
    apimName: apim.outputs.name
  }
}

module mock 'modules/mock-aci.bicep' = if (deployCompute) {
  name: 'mock'
  params: {
    name: '${namePrefix}-mock-${suffix}'
    location: location
    image: '${registry.outputs.loginServer}/mock:${imageTag}'
    registryServer: registry.outputs.loginServer
    identityId: registry.outputs.identityId
    dnsLabel: mockDnsLabel
    mockApiKey: mockApiKey
  }
}

module apps 'modules/apps.bicep' = if (deployCompute) {
  name: 'apps'
  params: {
    location: location
    envId: aca.outputs.envId
    registryServer: registry.outputs.loginServer
    identityId: registry.outputs.identityId
    identityClientId: registry.outputs.identityClientId
    identityPrincipalId: registry.outputs.identityPrincipalId
    namePrefix: namePrefix
    suffix: suffix
    imageTag: imageTag
    searchEndpoint: search.outputs.endpoint
    foundryEndpoint: foundry.outputs.endpoint
    modelName: foundry.outputs.deployment
    apimName: apim.outputs.name
    apimUrl: apim.outputs.gatewayUrl
    llmMaxAttempts: llmMaxAttempts
    llmRetryBackoffSeconds: llmRetryBackoffSeconds
    labPassword: labPassword
    internalToken: internalToken
    envDefaultDomain: aca.outputs.defaultDomain
  }
  dependsOn: [roles]
}

output acrName string = registry.outputs.acrName
output apimName string = apim.outputs.name
output apimGatewayUrl string = apim.outputs.gatewayUrl
output mockUrl string = mockUrl
output probeJobName string = '${namePrefix}-probe-${suffix}'
output logAnalyticsName string = lawName
output searchName string = search.outputs.name
output searchEndpoint string = search.outputs.endpoint
output foundryName string = foundry.outputs.name
output foundryEndpoint string = foundry.outputs.endpoint
output webUrl string = deployCompute ? apps!.outputs.webUrl : ''
output workerJobName string = deployCompute ? apps!.outputs.workerJobName : ''
