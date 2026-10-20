// ACR (Basic) + one user-assigned identity with AcrPull, shared by the ACI mock and the ACA job.
// Needs permission to create role assignments (Owner or User Access Administrator) on the RG.
param acrName string
param identityName string
param location string

var acrPullRoleId = '7f951dda-4ed3-4680-a7ca-43fe172d538d'

resource acr 'Microsoft.ContainerRegistry/registries@2023-07-01' = {
  name: acrName
  location: location
  sku: { name: 'Basic' }
  properties: { adminUserEnabled: false }
}

resource id 'Microsoft.ManagedIdentity/userAssignedIdentities@2023-01-31' = {
  name: identityName
  location: location
}

resource pull 'Microsoft.Authorization/roleAssignments@2022-04-01' = {
  name: guid(acr.id, id.id, acrPullRoleId)
  scope: acr
  properties: {
    principalId: id.properties.principalId
    principalType: 'ServicePrincipal'
    roleDefinitionId: subscriptionResourceId('Microsoft.Authorization/roleDefinitions', acrPullRoleId)
  }
}

output acrName string = acr.name
output loginServer string = acr.properties.loginServer
output identityId string = id.id
output identityPrincipalId string = id.properties.principalId
output identityClientId string = id.properties.clientId
