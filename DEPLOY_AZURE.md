# Deployment Guide: Azure Cloud

Run the course notebooks using Azure OpenAI Service for enterprise-grade AI capabilities.

## Overview

Azure OpenAI Service provides:
- ✅ **Enterprise security** - SOC 2, HIPAA, ISO compliance
- ✅ **High performance** - Microsoft's global infrastructure
- ✅ **Latest models** - GPT-4, GPT-3.5-turbo, embeddings
- ✅ **Cost control** - Usage quotas and monitoring
- ✅ **Private networks** - VNet integration available

## Prerequisites

- Azure subscription ([Create free account](https://azure.microsoft.com/free/))
- Azure CLI installed ([Install guide](https://docs.microsoft.com/cli/azure/install-azure-cli))
- Contributor access to create resources
- Access to Azure OpenAI Service ([Request access](https://aka.ms/oai/access))

## Quick Start (Azure Portal)

### 1. Create Azure OpenAI Resource

```bash
# Login to Azure
az login

# Set subscription
az account set --subscription "Your-Subscription-Name"

# Create resource group
az group create \
  --name mba590-ai-rg \
  --location eastus

# Create Azure OpenAI resource
az cognitiveservices account create \
  --name mba590-openai \
  --resource-group mba590-ai-rg \
  --kind OpenAI \
  --sku S0 \
  --location eastus
```

### 2. Deploy Models

```bash
# Deploy GPT-4
az cognitiveservices account deployment create \
  --resource-group mba590-ai-rg \
  --name mba590-openai \
  --deployment-name gpt-4 \
  --model-name gpt-4 \
  --model-version "0613" \
  --model-format OpenAI \
  --sku-capacity 10 \
  --sku-name "Standard"

# Deploy GPT-3.5-turbo (for cost-effective testing)
az cognitiveservices account deployment create \
  --resource-group mba590-ai-rg \
  --name mba590-openai \
  --deployment-name gpt-35-turbo \
  --model-name gpt-35-turbo \
  --model-version "0613" \
  --model-format OpenAI \
  --sku-capacity 10 \
  --sku-name "Standard"

# Deploy embeddings model (for RAG exercises)
az cognitiveservices account deployment create \
  --resource-group mba590-ai-rg \
  --name mba590-openai \
  --deployment-name text-embedding-ada-002 \
  --model-name text-embedding-ada-002 \
  --model-version "2" \
  --model-format OpenAI \
  --sku-capacity 10 \
  --sku-name "Standard"
```

### 3. Get Credentials

```bash
# Get endpoint
az cognitiveservices account show \
  --name mba590-openai \
  --resource-group mba590-ai-rg \
  --query properties.endpoint \
  --output tsv

# Get API key
az cognitiveservices account keys list \
  --name mba590-openai \
  --resource-group mba590-ai-rg \
  --query key1 \
  --output tsv
```

### 4. Configure Environment

```bash
# Copy environment template
cp .env.example .env

# Edit .env and add:
LLM_PROVIDER=azure
AZURE_OPENAI_ENDPOINT=https://mba590-openai.openai.azure.com/
AZURE_OPENAI_KEY=your-api-key-here
AZURE_OPENAI_API_VERSION=2024-02-15-preview
AZURE_OPENAI_DEPLOYMENT_NAME=gpt-4
AZURE_OPENAI_EMBEDDING_DEPLOYMENT=text-embedding-ada-002
```

## One-Click Deployment

Use Azure Resource Manager (ARM) template for automated deployment:

```bash
# Deploy using provided template
az deployment group create \
  --resource-group mba590-ai-rg \
  --template-file azure/deploy-azure-openai.json \
  --parameters azure/parameters.json
```

See `azure/README.md` for template details.

## Using Azure OpenAI in Notebooks

### Basic Usage

```python
from utils.llm_helpers import call_azure_openai

response = call_azure_openai(
    prompt="Explain prompt engineering",
    deployment="gpt-4",
    temperature=0.7
)
print(response)
```

### Chat Completions

```python
from utils.llm_helpers import chat_azure_openai

messages = [
    {"role": "system", "content": "You are an AI strategy expert."},
    {"role": "user", "content": "What is agentic AI?"}
]

response = chat_azure_openai(
    messages=messages,
    deployment="gpt-4",
    temperature=0.7,
    max_tokens=500
)
print(response)
```

### Embeddings (for RAG)

```python
from utils.llm_helpers import get_azure_embeddings

texts = [
    "Document 1 content",
    "Document 2 content",
    "Document 3 content"
]

embeddings = get_azure_embeddings(
    texts=texts,
    deployment="text-embedding-ada-002"
)
```

### Streaming Responses

```python
from utils.llm_helpers import stream_azure_openai

for chunk in stream_azure_openai(
    prompt="Write a business plan",
    deployment="gpt-4"
):
    print(chunk, end='', flush=True)
```

## Cost Management

### Set Usage Quotas

```python
# In Azure Portal:
# 1. Go to your Azure OpenAI resource
# 2. Click "Quota"
# 3. Set limits per model deployment

# Example limits for course:
# - gpt-4: 100K tokens/minute
# - gpt-35-turbo: 200K tokens/minute
```

### Monitor Usage

```bash
# View usage metrics
az monitor metrics list \
  --resource "/subscriptions/{subscription-id}/resourceGroups/mba590-ai-rg/providers/Microsoft.CognitiveServices/accounts/mba590-openai" \
  --metric "Total Calls" \
  --start-time 2024-01-01T00:00:00Z \
  --end-time 2024-01-31T23:59:59Z
```

### Cost Estimation

```python
from utils.llm_helpers import estimate_azure_cost

# Estimate cost for assignment
cost = estimate_azure_cost(
    input_tokens=5000,
    output_tokens=2000,
    model="gpt-4",
    region="eastus"
)
print(f"Estimated cost: ${cost['total_cost']:.4f}")
```

## Security Best Practices

### 1. Use Managed Identity

```python
# In production, use managed identity instead of API keys
from azure.identity import DefaultAzureCredential
from openai import AzureOpenAI

credential = DefaultAzureCredential()
client = AzureOpenAI(
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    azure_ad_token_provider=credential.get_token,
    api_version="2024-02-15-preview"
)
```

### 2. Network Security

```bash
# Restrict to specific IPs or VNets
az cognitiveservices account network-rule add \
  --resource-group mba590-ai-rg \
  --name mba590-openai \
  --ip-address "YOUR_IP_ADDRESS"

# Or use Private Endpoint
az network private-endpoint create \
  --resource-group mba590-ai-rg \
  --name mba590-openai-pe \
  --vnet-name mba590-vnet \
  --subnet default \
  --private-connection-resource-id "/subscriptions/{sub-id}/resourceGroups/mba590-ai-rg/providers/Microsoft.CognitiveServices/accounts/mba590-openai" \
  --group-id account \
  --connection-name mba590-openai-connection
```

### 3. Key Rotation

```bash
# Regenerate keys periodically
az cognitiveservices account keys regenerate \
  --name mba590-openai \
  --resource-group mba590-ai-rg \
  --key-name key1
```

## Azure Container Apps Deployment

Deploy the entire course environment to Azure:

### 1. Build and Push Container

```bash
# Login to Azure Container Registry
az acr login --name mba590registry

# Build image
docker build -t mba590registry.azurecr.io/ai-course:latest .

# Push to registry
docker push mba590registry.azurecr.io/ai-course:latest
```

### 2. Deploy to Container Apps

```bash
# Create Container Apps environment
az containerapp env create \
  --name mba590-env \
  --resource-group mba590-ai-rg \
  --location eastus

# Deploy app
az containerapp create \
  --name mba590-jupyter \
  --resource-group mba590-ai-rg \
  --environment mba590-env \
  --image mba590registry.azurecr.io/ai-course:latest \
  --target-port 8888 \
  --ingress external \
  --env-vars \
    AZURE_OPENAI_ENDPOINT=https://mba590-openai.openai.azure.com/ \
    AZURE_OPENAI_KEY=secretref:openai-key
```

### 3. Access Jupyter

```bash
# Get URL
az containerapp show \
  --name mba590-jupyter \
  --resource-group mba590-ai-rg \
  --query properties.configuration.ingress.fqdn \
  --output tsv
```

## Multi-Region Deployment

For high availability:

```bash
# Deploy to multiple regions
regions=("eastus" "westeurope" "southeastasia")

for region in "${regions[@]}"; do
  az cognitiveservices account create \
    --name "mba590-openai-${region}" \
    --resource-group mba590-ai-rg \
    --kind OpenAI \
    --sku S0 \
    --location ${region}
done

# Use Azure Traffic Manager for load balancing
```

## Monitoring and Logging

### Enable Diagnostics

```bash
# Create Log Analytics workspace
az monitor log-analytics workspace create \
  --resource-group mba590-ai-rg \
  --workspace-name mba590-logs

# Enable diagnostic settings
az monitor diagnostic-settings create \
  --name mba590-diagnostics \
  --resource "/subscriptions/{sub-id}/resourceGroups/mba590-ai-rg/providers/Microsoft.CognitiveServices/accounts/mba590-openai" \
  --workspace "/subscriptions/{sub-id}/resourceGroups/mba590-ai-rg/providers/Microsoft.OperationalInsights/workspaces/mba590-logs" \
  --logs '[{"category": "Audit", "enabled": true}, {"category": "RequestResponse", "enabled": true}]' \
  --metrics '[{"category": "AllMetrics", "enabled": true}]'
```

### Query Logs

```kusto
// In Azure Portal > Log Analytics
AzureDiagnostics
| where ResourceProvider == "MICROSOFT.COGNITIVESERVICES"
| where TimeGenerated > ago(24h)
| summarize count() by OperationName, bin(TimeGenerated, 1h)
| render timechart
```

## Troubleshooting

### Rate Limit Errors

```python
# Implement retry logic with exponential backoff
from utils.llm_helpers import call_azure_openai_with_retry

response = call_azure_openai_with_retry(
    prompt="Your prompt",
    deployment="gpt-4",
    max_retries=3,
    backoff_factor=2
)
```

### Quota Issues

```bash
# Check current quota
az cognitiveservices account deployment show \
  --name mba590-openai \
  --resource-group mba590-ai-rg \
  --deployment-name gpt-4

# Request quota increase via Azure Portal
```

### Network Connectivity

```bash
# Test endpoint
curl https://mba590-openai.openai.azure.com/openai/deployments?api-version=2024-02-15-preview \
  -H "api-key: YOUR_API_KEY"
```

## Cost Optimization Tips

1. **Use GPT-3.5-turbo for development** - Switch to GPT-4 for production
2. **Set token limits** - Prevent runaway costs
3. **Cache responses** - Reuse identical queries
4. **Batch requests** - Reduce API calls
5. **Monitor daily** - Set up cost alerts

```bash
# Create budget alert
az consumption budget create \
  --amount 100 \
  --budget-name mba590-budget \
  --category Cost \
  --time-grain Monthly \
  --time-period start-date="2024-01-01" \
  --notifications actual_GreaterThan_80_Percent: \
    enabled=true \
    threshold=80 \
    operator=GreaterThan \
    contact-emails="admin@example.com"
```

## Comparison: Azure vs Other Options

| Feature | Azure OpenAI | OpenAI Direct | Local LLM |
|---------|-------------|---------------|-----------|
| Compliance | ✅ Enterprise | ⚠️ Standard | ✅ Full control |
| Data residency | ✅ Configurable | ❌ US only | ✅ On-prem |
| VNet integration | ✅ Yes | ❌ No | ✅ Yes |
| SLA | ✅ 99.9% | ⚠️ None | ⚠️ Self-managed |
| Model availability | ⚠️ Delayed | ✅ Latest | ⚠️ Limited |
| Cost | ⚠️ Similar to OpenAI | ⚠️ Per-token | ✅ Free |

## Resources

- [Azure OpenAI Documentation](https://learn.microsoft.com/azure/ai-services/openai/)
- [Pricing Calculator](https://azure.microsoft.com/pricing/calculator/)
- [Best Practices](https://learn.microsoft.com/azure/ai-services/openai/concepts/best-practices)
- [Enterprise Deployment](https://learn.microsoft.com/azure/ai-services/openai/how-to/enterprise)

## Support

For Azure-specific issues:
1. Check [Azure Status](https://status.azure.com/)
2. Review diagnostic logs
3. Contact Azure Support
4. See TROUBLESHOOTING.md

---

**Previous**: [Local Deployment Guide](DEPLOY_LOCAL.md) | **Next**: [README](README.md)
