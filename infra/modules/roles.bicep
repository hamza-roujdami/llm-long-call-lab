// Data-plane roles for the shared app identity on Search and Foundry.
param identityPrincipalId string
param searchName string
param foundryName string

var searchIndexDataReader = '1407120a-92aa-4202-b7e9-c0e197c71c8f'
var openAIUser = '5e0bd9bd-7b93-4f28-af87-19fc36ad61bd'

resource search 'Microsoft.Search/searchServices@2024-06-01-preview' existing = { name: searchName }
resource foundry 'Microsoft.CognitiveServices/accounts@2025-06-01' existing = { name: foundryName }

resource searchRead 'Microsoft.Authorization/roleAssignments@2022-04-01' = {
  name: guid(search.id, identityPrincipalId, searchIndexDataReader)
  scope: search
  properties: {
    principalId: identityPrincipalId
    principalType: 'ServicePrincipal'
    roleDefinitionId: subscriptionResourceId('Microsoft.Authorization/roleDefinitions', searchIndexDataReader)
  }
}

resource model 'Microsoft.Authorization/roleAssignments@2022-04-01' = {
  name: guid(foundry.id, identityPrincipalId, openAIUser)
  scope: foundry
  properties: {
    principalId: identityPrincipalId
    principalType: 'ServicePrincipal'
    roleDefinitionId: subscriptionResourceId('Microsoft.Authorization/roleDefinitions', openAIUser)
  }
}
