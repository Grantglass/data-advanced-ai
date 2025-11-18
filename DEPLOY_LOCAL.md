# Deployment Guide: Local LLM (On-Premises)

Run the course notebooks completely locally using open-source LLMs - no cloud API required!

## Overview

This setup allows you to run Large Language Models on your own hardware using [Ollama](https://ollama.ai/), providing:
- ✅ **Complete privacy** - Data never leaves your machine
- ✅ **No API costs** - Free to use
- ✅ **Offline capability** - Works without internet
- ✅ **Full control** - Choose your models and parameters

## Prerequisites

### Hardware Requirements

**Minimum**:
- CPU: 8-core processor
- RAM: 16GB
- Storage: 50GB free space
- GPU: Optional but recommended

**Recommended**:
- CPU: 16-core processor
- RAM: 32GB+
- Storage: 100GB+ SSD
- GPU: NVIDIA GPU with 8GB+ VRAM (RTX 3060 or better)

### Software Requirements

- Docker and Docker Compose
- NVIDIA drivers (if using GPU)
- NVIDIA Container Toolkit (for GPU support)

## Quick Start

### 1. Install Ollama

**On Linux/WSL**:
```bash
curl -fsSL https://ollama.ai/install.sh | sh
```

**On macOS**:
```bash
brew install ollama
```

**On Windows**:
Download from https://ollama.ai/download

### 2. Start Ollama Service

```bash
# Start Ollama server
ollama serve
```

### 3. Pull Models

```bash
# Recommended models for this course

# Fast, efficient model (good for testing)
ollama pull llama2:7b

# Better quality (requires more resources)
ollama pull llama2:13b

# Best quality (requires powerful GPU)
ollama pull llama2:70b

# Alternative: Mistral (excellent performance)
ollama pull mistral:7b

# For code tasks
ollama pull codellama:7b
```

### 4. Configure Environment

```bash
# Copy environment template
cp .env.example .env

# Edit .env and set:
LLM_PROVIDER=ollama
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=llama2:7b
```

### 5. Start with Docker Compose

```bash
# Use the local LLM configuration
docker-compose -f docker-compose.local-llm.yml up
```

Access Jupyter at http://localhost:8888

## Model Selection Guide

### For Course Exercises

| Task | Recommended Model | RAM Needed |
|------|------------------|------------|
| Prompt engineering basics | llama2:7b | 8GB |
| Advanced prompting | mistral:7b | 8GB |
| Agentic systems | llama2:13b | 16GB |
| Complex reasoning | llama2:70b | 64GB |
| Code generation | codellama:7b | 8GB |

### Model Comparison

```bash
# List available models
ollama list

# Get model info
ollama show llama2:7b
```

## Using Local LLMs in Notebooks

### Basic Usage

```python
from utils.llm_helpers import call_local_llm

# Simple completion
response = call_local_llm(
    prompt="Explain prompt engineering",
    model="llama2:7b",
    temperature=0.7
)
print(response)
```

### Chat Format

```python
from utils.llm_helpers import chat_local_llm

messages = [
    {"role": "system", "content": "You are a helpful AI assistant."},
    {"role": "user", "content": "What is RAG?"}
]

response = chat_local_llm(messages, model="llama2:7b")
print(response)
```

### Streaming Responses

```python
from utils.llm_helpers import stream_local_llm

for chunk in stream_local_llm("Write a business plan", model="llama2:7b"):
    print(chunk, end='', flush=True)
```

## Performance Optimization

### GPU Acceleration

**Check GPU availability**:
```bash
nvidia-smi
```

**Configure GPU usage**:
```bash
# Use specific GPU
CUDA_VISIBLE_DEVICES=0 ollama serve

# Use multiple GPUs
CUDA_VISIBLE_DEVICES=0,1 ollama serve
```

### Model Quantization

Use quantized models for better performance:

```bash
# 4-bit quantization (faster, less memory)
ollama pull llama2:7b-q4

# 8-bit quantization (balanced)
ollama pull llama2:7b-q8
```

### Context Window Management

```python
# Adjust context window size
response = call_local_llm(
    prompt="Your prompt",
    model="llama2:7b",
    options={
        "num_ctx": 4096,  # Context window size
        "num_predict": 512  # Max tokens to generate
    }
)
```

## Troubleshooting

### Ollama Not Starting

```bash
# Check if Ollama is running
curl http://localhost:11434/api/tags

# Restart Ollama
pkill ollama
ollama serve
```

### Out of Memory Errors

**Solutions**:
1. Use smaller model (7b instead of 13b)
2. Reduce context window
3. Enable quantization
4. Close other applications

```python
# Reduce memory usage
response = call_local_llm(
    prompt="Your prompt",
    model="llama2:7b-q4",  # Quantized model
    options={
        "num_ctx": 2048,  # Smaller context
        "num_batch": 128  # Smaller batch size
    }
)
```

### Slow Performance

**Optimizations**:
1. Use GPU if available
2. Use quantized models
3. Reduce max tokens
4. Use smaller context window

```bash
# Monitor performance
ollama run llama2:7b --verbose
```

## Model Management

### Update Models

```bash
# Update to latest version
ollama pull llama2:7b

# Remove old models
ollama rm llama2:7b-old
```

### Custom Models

```bash
# Create custom model from Modelfile
ollama create mymodel -f Modelfile

# Example Modelfile
cat > Modelfile <<EOF
FROM llama2:7b
SYSTEM You are an AI strategy expert specializing in business applications.
PARAMETER temperature 0.7
PARAMETER top_p 0.9
EOF

ollama create ai-strategy-expert -f Modelfile
```

## Alternative: LM Studio

If you prefer a GUI, use [LM Studio](https://lmstudio.ai/):

1. Download and install LM Studio
2. Download models through the GUI
3. Start local server (default: http://localhost:1234)
4. Update `.env`:
   ```
   LLM_PROVIDER=lmstudio
   LMSTUDIO_BASE_URL=http://localhost:1234
   ```

## Comparison: Local vs Cloud

| Aspect | Local LLM | Cloud API |
|--------|-----------|-----------|
| Privacy | ✅ Complete | ⚠️ Data sent to cloud |
| Cost | ✅ Free (hardware only) | ❌ Per-token pricing |
| Speed | ⚠️ Depends on hardware | ✅ Usually faster |
| Quality | ⚠️ Good (varies by model) | ✅ Excellent |
| Offline | ✅ Yes | ❌ No |
| Setup | ⚠️ More complex | ✅ Simple |

## Best Practices

1. **Start small**: Begin with 7b models, upgrade if needed
2. **Monitor resources**: Watch RAM/GPU usage
3. **Use quantization**: 4-bit models are usually sufficient
4. **Cache effectively**: Reuse model outputs when possible
5. **Batch requests**: Process multiple prompts together

## Resources

- [Ollama Documentation](https://github.com/ollama/ollama)
- [Model Library](https://ollama.ai/library)
- [LM Studio](https://lmstudio.ai/)
- [LocalAI](https://localai.io/)

## Support

For issues:
1. Check Ollama logs: `ollama logs`
2. Verify model: `ollama list`
3. Test API: `curl http://localhost:11434/api/tags`
4. See TROUBLESHOOTING.md

---

**Next**: See [Azure Deployment Guide](DEPLOY_AZURE.md) for cloud option
