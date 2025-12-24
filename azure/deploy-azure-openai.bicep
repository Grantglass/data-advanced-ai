// Azure OpenAI Deployment for MBA 590 Course
// This template creates all necessary Azure resources

@description('Base name for all resources')
param baseName string = 'mba590'

@description('Location for all resources')
param location string = resourceGroup().location

@description('Azure OpenAI SKU')
@allowed([
  'S0'
])
param openAiSku string = 'S0'

@description('GPT-4 deployment capacity (TPM in thousands)')
param gpt4Capacity int = 10

@description('GPT-3.5-turbo deployment capacity (TPM in thousands)')
param gpt35Capacity int = 20

@description('Text embedding deployment capacity (TPM in thousands)')
param embeddingCapacity int = 10

@description('Tags to apply to all resources')
param tags object = {
  Environment: 'Education'
  Course: 'MBA 590'
  Purpose: 'AI Strategy'
}

// Azure OpenAI Service
resource openAiAccount 'Microsoft.CognitiveServices/accounts@2023-05-01' = {
  name: '${baseName}-openai'
  location: location
  kind: 'OpenAI'
  sku: {
    name: openAiSku
  }
  properties: {
    customSubDomainName: '${baseName}-openai'
    publicNetworkAccess: 'Enabled'
    networkAcls: {
      defaultAction: 'Allow'
    }
  }
  tags: tags
}

// GPT-4 Deployment
resource gpt4Deployment 'Microsoft.CognitiveServices/accounts/deployments@2023-05-01' = {
  parent: openAiAccount
  name: 'gpt-4'
  properties: {
    model: {
      format: 'OpenAI'
      name: 'gpt-4'
      version: '0613'
    }
  }
  sku: {
    name: 'Standard'
    capacity: gpt4Capacity
  }
}

// GPT-3.5-turbo Deployment
resource gpt35Deployment 'Microsoft.CognitiveServices/accounts/deployments@2023-05-01' = {
  parent: openAiAccount
  name: 'gpt-35-turbo'
  properties: {
    model: {
      format: 'OpenAI'
      name: 'gpt-35-turbo'
      version: '0613'
    }
  }
  sku: {
    name: 'Standard'
    capacity: gpt35Capacity
  }
  dependsOn: [
    gpt4Deployment
  ]
}

// Text Embedding Deployment
resource embeddingDeployment 'Microsoft.CognitiveServices/accounts/deployments@2023-05-01' = {
  parent: openAiAccount
  name: 'text-embedding-ada-002'
  properties: {
    model: {
      format: 'OpenAI'
      name: 'text-embedding-ada-002'
      version: '2'
    }
  }
  sku: {
    name: 'Standard'
    capacity: embeddingCapacity
  }
  dependsOn: [
    gpt35Deployment
  ]
}

// Log Analytics Workspace for monitoring
resource logWorkspace 'Microsoft.OperationalInsights/workspaces@2022-10-01' = {
  name: '${baseName}-logs'
  location: location
  properties: {
    sku: {
      name: 'PerGB2018'
    }
    retentionInDays: 30
  }
  tags: tags
}

// Diagnostic settings for Azure OpenAI
resource diagnosticSettings 'Microsoft.Insights/diagnosticSettings@2021-05-01-preview' = {
  scope: openAiAccount
  name: '${baseName}-diagnostics'
  properties: {
    workspaceId: logWorkspace.id
    logs: [
      {
        category: 'Audit'
        enabled: true
        retentionPolicy: {
          enabled: true
          days: 30
        }
      }
      {
        category: 'RequestResponse'
        enabled: true
        retentionPolicy: {
          enabled: true
          days: 30
        }
      }
    ]
    metrics: [
      {
        category: 'AllMetrics'
        enabled: true
        retentionPolicy: {
          enabled: true
          days: 30
        }
      }
    ]
  }
}

// Container Registry for Jupyter images (optional)
resource containerRegistry 'Microsoft.ContainerRegistry/registries@2023-01-01-preview' = {
  name: '${baseName}registry'
  location: location
  sku: {
    name: 'Basic'
  }
  properties: {
    adminUserEnabled: true
  }
  tags: tags
}

// Storage Account for notebooks and data
resource storageAccount 'Microsoft.Storage/storageAccounts@2023-01-01' = {
  name: '${baseName}storage'
  location: location
  sku: {
    name: 'Standard_LRS'
  }
  kind: 'StorageV2'
  properties: {
    accessTier: 'Hot'
    supportsHttpsTrafficOnly: true
    minimumTlsVersion: 'TLS1_2'
  }
  tags: tags
}

// Blob container for course materials
resource blobService 'Microsoft.Storage/storageAccounts/blobServices@2023-01-01' = {
  parent: storageAccount
  name: 'default'
}

resource notebooksContainer 'Microsoft.Storage/storageAccounts/blobServices/containers@2023-01-01' = {
  parent: blobService
  name: 'notebooks'
  properties: {
    publicAccess: 'None'
  }
}

resource dataContainer 'Microsoft.Storage/storageAccounts/blobServices/containers@2023-01-01' = {
  parent: blobService
  name: 'data'
  properties: {
    publicAccess: 'None'
  }
}

// Outputs
output openAiEndpoint string = openAiAccount.properties.endpoint
output openAiKey string = openAiAccount.listKeys().key1
output openAiResourceId string = openAiAccount.id
output logWorkspaceId string = logWorkspace.id
output containerRegistryLoginServer string = containerRegistry.properties.loginServer
output storageAccountName string = storageAccount.name
output storageAccountKey string = storageAccount.listKeys().keys[0].value
