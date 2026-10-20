// APIM (Developer or StandardV2 only; Consumption does not support long-running connections).
// Two APIs in front of the Foundry GPT-6 Sol deployment (both authenticate with APIM's managed identity):
//   llm-default : path 2, NO forward-request policy (APIM defaults)
//   llm-stream  : path 3, forward-request timeout=600 buffer-response=false
// Deliberately no API/service-level `diagnostics` resource: no request/response body logging.
param name string
param location string
param publisherEmail string
param publisherName string

@allowed(['Developer', 'StandardV2'])
param sku string

param foundryName string
param foundryEndpoint string
param logAnalyticsId string

var cognitiveServicesOpenAIUser = '5e0bd9bd-7b93-4f28-af87-19fc36ad61bd'

resource apim 'Microsoft.ApiManagement/service@2024-05-01' = {
  name: name
  location: location
  sku: { name: sku, capacity: 1 }
  identity: { type: 'SystemAssigned' }
  properties: {
    publisherEmail: publisherEmail
    publisherName: publisherName
  }
}

resource foundry 'Microsoft.CognitiveServices/accounts@2025-06-01' existing = {
  name: foundryName
}

resource apimCallsFoundry 'Microsoft.Authorization/roleAssignments@2022-04-01' = {
  name: guid(foundry.id, apim.id, cognitiveServicesOpenAIUser)
  scope: foundry
  properties: {
    principalId: apim.identity.principalId
    principalType: 'ServicePrincipal'
    roleDefinitionId: subscriptionResourceId('Microsoft.Authorization/roleDefinitions', cognitiveServicesOpenAIUser)
  }
}

var llmVariants = [
  { key: 'default', path: 'llm-default', policy: loadTextContent('../apim/policy-default.xml') }
  { key: 'stream', path: 'llm-stream', policy: loadTextContent('../apim/policy-stream.xml') }
]
var llmOperations = [
  { name: 'chat-completions', template: '/chat/completions' }
  { name: 'responses', template: '/responses' }
]

resource llmApis 'Microsoft.ApiManagement/service/apis@2024-05-01' = [
  for v in llmVariants: {
    parent: apim
    name: 'llm-${v.key}'
    properties: {
      displayName: 'Foundry GPT-6 Sol (${v.key})'
      path: v.path
      protocols: ['https']
      serviceUrl: '${foundryEndpoint}/openai/v1'
      subscriptionRequired: true
      // OpenAI-style clients send the APIM key in `api-key`.
      subscriptionKeyParameterNames: { header: 'api-key', query: 'subscription-key' }
    }
  }
]

resource llmOps 'Microsoft.ApiManagement/service/apis/operations@2024-05-01' = [
  for i in range(0, length(llmVariants) * length(llmOperations)): {
    parent: llmApis[i / length(llmOperations)]
    name: llmOperations[i % length(llmOperations)].name
    properties: {
      displayName: llmOperations[i % length(llmOperations)].name
      method: 'POST'
      urlTemplate: llmOperations[i % length(llmOperations)].template
    }
  }
]

resource llmPolicies 'Microsoft.ApiManagement/service/apis/policies@2024-05-01' = [
  for (v, i) in llmVariants: {
    parent: llmApis[i]
    name: 'policy'
    properties: { format: 'rawxml', value: v.policy }
    dependsOn: [apimCallsFoundry]
  }
]

resource sub 'Microsoft.ApiManagement/service/subscriptions@2024-05-01' = {
  parent: apim
  name: 'lab-client'
  properties: {
    displayName: 'lab-client'
    scope: '${apim.id}/apis'
    allowTracing: false
  }
  dependsOn: [llmApis]
}

resource gatewayLogs 'Microsoft.Insights/diagnosticSettings@2021-05-01-preview' = {
  name: 'to-law'
  scope: apim
  properties: {
    workspaceId: logAnalyticsId
    logAnalyticsDestinationType: 'Dedicated'
    logs: [{ category: 'GatewayLogs', enabled: true }]
  }
}

output name string = apim.name
output gatewayUrl string = apim.properties.gatewayUrl
