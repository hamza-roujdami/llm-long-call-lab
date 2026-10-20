// apim-timeout-lab: resource-group-scoped deployment. NOT deployed without explicit approval.
//
// Phase 1 (deployCompute=false): Log Analytics, ACR + identity, ACA environment, APIM.
// Build/push images with `az acr build` (see README).
// Phase 2 (deployCompute=true): ACI mock + ACA Job.
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

@secure()
param mockApiKey string

var suffix = take(uniqueString(resourceGroup().id), 5)
var acrName = replace('${namePrefix}acr${suffix}', '-', '')
var apimName = '${namePrefix}-apim-${suffix}'
var mockDnsLabel = '${namePrefix}-mock-${suffix}'
var mockUrl = 'http://${mockDnsLabel}.${location}.azurecontainer.io:8000'

module monitoring 'modules/monitoring.bicep' = {
  name: 'monitoring'
  params: { name: '${namePrefix}-law-${suffix}', location: location }
}

module registry 'modules/registry.bicep' = {
  name: 'registry'
  params: { acrName: acrName, identityName: '${namePrefix}-id-${suffix}', location: location }
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
    logAnalyticsId: monitoring.outputs.id
    mockApiKey: mockApiKey
  }
}

resource apimService 'Microsoft.ApiManagement/service@2024-05-01' existing = {
  name: apimName
}

resource clientSub 'Microsoft.ApiManagement/service/subscriptions@2024-05-01' existing = {
  parent: apimService
  name: 'lab-client'
}

module aca 'modules/aca.bicep' = {
  name: 'aca'
  params: {
    envName: '${namePrefix}-env-${suffix}'
    jobName: '${namePrefix}-client-${suffix}'
    location: location
    logAnalyticsName: '${namePrefix}-law-${suffix}'
    deployJob: deployCompute
    image: '${registry.outputs.loginServer}/client:${imageTag}'
    registryServer: registry.outputs.loginServer
    identityId: registry.outputs.identityId
    mockBaseUrl: mockUrl
    apimBaseUrl: apim.outputs.gatewayUrl
    mockApiKey: mockApiKey
    apimSubscriptionKey: clientSub.listSecrets().primaryKey
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

output acrName string = registry.outputs.acrName
output apimName string = apim.outputs.name
output apimGatewayUrl string = apim.outputs.gatewayUrl
output mockUrl string = mockUrl
output jobName string = '${namePrefix}-client-${suffix}'
output logAnalyticsName string = '${namePrefix}-law-${suffix}'
