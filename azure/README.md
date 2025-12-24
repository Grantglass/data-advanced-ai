# Azure Deployment Templates

This directory contains Infrastructure-as-Code templates for deploying the MBA 590 course infrastructure to Azure.

## Files

- `deploy-azure-openai.bicep` - Main Bicep template for Azure OpenAI and supporting resources
- `deploy.sh` - Quick deployment script
- `parameters.json` - Parameter file for customization

## Quick Deploy

```bash
# Login to Azure
az login

# Create resource group
az group create --name mba590-rg --location eastus

# Deploy using Bicep
az deployment group create \
  --resource-group mba590-rg \
  --template-file deploy-azure-openai.bicep \
  --parameters baseName=mba590

# Get outputs
az deployment group show \
  --resource-group mba590-rg \
  --name deploy-azure-openai \
  --query properties.outputs
```

## What Gets Deployed

1. **Azure OpenAI Account**
   - GPT-4 deployment
   - GPT-3.5-turbo deployment
   - Text-embedding-ada-002 deployment

2. **Log Analytics Workspace**
   - 30-day retention
   - Diagnostic logging enabled

3. **Container Registry** (optional)
   - For custom Jupyter images

4. **Storage Account**
   - Blob containers for notebooks and data

## Customization

Create a `parameters.json` file:

```json
{
  "$schema": "https://schema.management.azure.com/schemas/2019-04-01/deploymentParameters.json#",
  "contentVersion": "1.0.0.0",
  "parameters": {
    "baseName": {
      "value": "mba590"
    },
    "location": {
      "value": "eastus"
    },
    "gpt4Capacity": {
      "value": 10
    },
    "gpt35Capacity": {
      "value": 20
    }
  }
}
```

Then deploy:

```bash
az deployment group create \
  --resource-group mba590-rg \
  --template-file deploy-azure-openai.bicep \
  --parameters @parameters.json
```

## Post-Deployment

1. **Get credentials**:
   ```bash
   # Get endpoint
   az cognitiveservices account show \
     --name mba590-openai \
     --resource-group mba590-rg \
     --query properties.endpoint -o tsv

   # Get API key
   az cognitiveservices account keys list \
     --name mba590-openai \
     --resource-group mba590-rg \
     --query key1 -o tsv
   ```

2. **Update `.env` file**:
   ```bash
   LLM_PROVIDER=azure
   AZURE_OPENAI_ENDPOINT=<endpoint from above>
   AZURE_OPENAI_KEY=<key from above>
   AZURE_OPENAI_API_VERSION=2024-02-15-preview
   AZURE_OPENAI_DEPLOYMENT_NAME=gpt-4
   ```

3. **Test connection**:
   ```bash
   curl <endpoint>/openai/deployments?api-version=2024-02-15-preview \
     -H "api-key: <your-key>"
   ```

## Clean Up

To delete all resources:

```bash
az group delete --name mba590-rg --yes --no-wait
```

## Cost Estimate

Typical monthly costs for classroom use (20 students):

- Azure OpenAI: $200-500 (depends on usage)
- Log Analytics: $5-10
- Storage: $1-2
- Container Registry: $5

**Total: ~$210-520/month**

Use Azure Cost Management to monitor actual spend.

## Security Best Practices

1. **Enable Private Endpoints** (production):
   ```bash
   # Add to bicep template
   networkAcls: {
     defaultAction: 'Deny'
   }
   ```

2. **Use Managed Identity** instead of API keys

3. **Enable Azure Policy** for compliance

4. **Set up budget alerts**:
   ```bash
   az consumption budget create \
     --amount 500 \
     --budget-name mba590-budget \
     --category Cost \
     --time-grain Monthly
   ```

## Troubleshooting

See [DEPLOY_AZURE.md](../DEPLOY_AZURE.md) for detailed troubleshooting guide.

## Support

For Azure-specific issues:
- Check [Azure Status](https://status.azure.com/)
- Review deployment logs: `az deployment group show`
- Contact Azure Support
