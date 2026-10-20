// APIM (Developer or StandardV2 only; Consumption does not support long-running connections),
// two APIs in front of the mock (streaming vs buffering policy), a subscription, and gateway logs.
// Deliberately no API/service-level `diagnostics` resource: no request/response body logging.
param name string
param location string
param publisherEmail string
param publisherName string

@allowed(['Developer', 'StandardV2'])
param sku string

param backendUrl string
param logAnalyticsId string

@secure()
param mockApiKey string

resource apim 'Microsoft.ApiManagement/service@2024-05-01' = {
  name: name
  location: location
  sku: { name: sku, capacity: 1 }
  properties: {
    publisherEmail: publisherEmail
    publisherName: publisherName
  }
}

resource mockKey 'Microsoft.ApiManagement/service/namedValues@2024-05-01' = {
  parent: apim
  name: 'mock-key'
  properties: {
    displayName: 'mock-key'
    secret: true
    value: mockApiKey
  }
}

var variants = [
  { key: 'stream', path: 'lab', policy: loadTextContent('../../apim/streaming.xml') }
  { key: 'buffered', path: 'lab-buffered', policy: loadTextContent('../../apim/buffered.xml') }
]
var operations = ['silent', 'stream', 'gap']

resource apis 'Microsoft.ApiManagement/service/apis@2024-05-01' = [
  for v in variants: {
    parent: apim
    name: 'mock-${v.key}'
    properties: {
      displayName: 'Mock model (${v.key})'
      path: v.path
      protocols: ['https']
      serviceUrl: backendUrl
      subscriptionRequired: true
    }
  }
]

resource ops 'Microsoft.ApiManagement/service/apis/operations@2024-05-01' = [
  for i in range(0, length(variants) * length(operations)): {
    parent: apis[i / length(operations)]
    name: operations[i % length(operations)]
    properties: {
      displayName: operations[i % length(operations)]
      method: 'GET'
      urlTemplate: '/${operations[i % length(operations)]}'
    }
  }
]

resource policies 'Microsoft.ApiManagement/service/apis/policies@2024-05-01' = [
  for (v, i) in variants: {
    parent: apis[i]
    name: 'policy'
    properties: { format: 'rawxml', value: v.policy }
    dependsOn: [mockKey]
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
  dependsOn: [apis]
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
