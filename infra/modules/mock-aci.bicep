// Mock model on Azure Container Instances (public IP + DNS label, plain HTTP on 8000).
// ACI is used on purpose: Container Apps / App Service add their own ingress timeouts.
// Exposure: lab only, no customer data; protected by a shared x-mock-key header.
param name string
param location string
param image string
param registryServer string
param identityId string
param dnsLabel string

@secure()
param mockApiKey string

resource mock 'Microsoft.ContainerInstance/containerGroups@2023-05-01' = {
  name: name
  location: location
  identity: {
    type: 'UserAssigned'
    userAssignedIdentities: { '${identityId}': {} }
  }
  properties: {
    osType: 'Linux'
    restartPolicy: 'Always'
    imageRegistryCredentials: [{ server: registryServer, identity: identityId }]
    ipAddress: {
      type: 'Public'
      dnsNameLabel: dnsLabel
      ports: [{ port: 8000, protocol: 'TCP' }]
    }
    containers: [
      {
        name: 'mock'
        properties: {
          image: image
          ports: [{ port: 8000, protocol: 'TCP' }]
          resources: { requests: { cpu: 1, memoryInGB: 1 } }
          environmentVariables: [{ name: 'MOCK_API_KEY', secureValue: mockApiKey }]
        }
      }
    ]
  }
}

output fqdn string = mock.properties.ipAddress.fqdn
output ip string = mock.properties.ipAddress.ip
