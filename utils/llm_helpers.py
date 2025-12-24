"""
LLM Helper Functions

Utilities for working with Large Language Models in notebooks.
"""

import tiktoken
from typing import Dict, List, Optional, Union
import time


def count_tokens(text: str, model: str = "gpt-4") -> int:
    """
    Count the number of tokens in a text string.

    Args:
        text: The text to tokenize
        model: The model name (for tokenizer selection)

    Returns:
        int: Number of tokens

    Example:
        >>> count_tokens("Hello, how are you?")
        5
    """
    try:
        encoding = tiktoken.encoding_for_model(model)
    except KeyError:
        encoding = tiktoken.get_encoding("cl100k_base")

    return len(encoding.encode(text))


def estimate_cost(
    input_tokens: int,
    output_tokens: int,
    model: str = "gpt-4"
) -> Dict[str, float]:
    """
    Estimate the cost of an LLM API call.

    Args:
        input_tokens: Number of input tokens
        output_tokens: Number of output tokens
        model: Model name

    Returns:
        Dict with cost breakdown

    Example:
        >>> estimate_cost(1000, 500, "gpt-4")
        {'input_cost': 0.03, 'output_cost': 0.03, 'total_cost': 0.06}
    """
    # Pricing per 1K tokens (as of 2024 - update as needed)
    pricing = {
        "gpt-4": {"input": 0.03, "output": 0.06},
        "gpt-4-turbo": {"input": 0.01, "output": 0.03},
        "gpt-3.5-turbo": {"input": 0.0005, "output": 0.0015},
        "claude-3-opus": {"input": 0.015, "output": 0.075},
        "claude-3-sonnet": {"input": 0.003, "output": 0.015},
        "claude-3-haiku": {"input": 0.00025, "output": 0.00125},
    }

    if model not in pricing:
        model = "gpt-4"  # default

    input_cost = (input_tokens / 1000) * pricing[model]["input"]
    output_cost = (output_tokens / 1000) * pricing[model]["output"]

    return {
        "input_cost": round(input_cost, 4),
        "output_cost": round(output_cost, 4),
        "total_cost": round(input_cost + output_cost, 4),
        "model": model
    }


def create_mock_llm_response(
    prompt: str,
    response_type: str = "generic",
    delay: float = 0.5
) -> Dict:
    """
    Create a mock LLM response for testing without API calls.

    Args:
        prompt: The input prompt
        response_type: Type of response ("generic", "analysis", "code", "creative")
        delay: Simulated response delay in seconds

    Returns:
        Dict containing mock response data

    Example:
        >>> response = create_mock_llm_response("Explain AI", "analysis")
        >>> print(response['content'])
    """
    time.sleep(delay)

    responses = {
        "generic": "This is a mock response to your prompt. In a real implementation, this would be the LLM's actual output.",
        "analysis": """Based on the provided information, here is my analysis:

1. **Key Finding**: The data shows significant trends
2. **Insight**: There are several important patterns to consider
3. **Recommendation**: Consider implementing the suggested approach

This mock response demonstrates the structure of an analytical output.""",
        "code": """```python
def example_function(param):
    \"\"\"
    This is a mock code example.
    \"\"\"
    result = param * 2
    return result

# Usage
output = example_function(5)
print(output)  # Returns: 10
```""",
        "creative": """# Title: Creative Mock Response

This is a creative response demonstrating:
- Engaging narrative style
- Structured information delivery
- Professional tone with personality

The actual LLM would provide much more detailed and contextually relevant content."""
    }

    content = responses.get(response_type, responses["generic"])

    return {
        "content": content,
        "model": "mock-model",
        "tokens": {
            "input": count_tokens(prompt),
            "output": count_tokens(content),
            "total": count_tokens(prompt) + count_tokens(content)
        },
        "cost": estimate_cost(
            count_tokens(prompt),
            count_tokens(content)
        )
    }


def format_chat_message(
    role: str,
    content: str,
    name: Optional[str] = None
) -> Dict:
    """
    Format a message for chat-based LLM APIs.

    Args:
        role: Message role ("system", "user", "assistant")
        content: Message content
        name: Optional name for the message

    Returns:
        Dict formatted for API

    Example:
        >>> msg = format_chat_message("user", "Hello!")
        >>> print(msg)
        {'role': 'user', 'content': 'Hello!'}
    """
    message = {
        "role": role,
        "content": content
    }

    if name:
        message["name"] = name

    return message


def create_chat_conversation(
    system_prompt: str,
    user_messages: List[str],
    assistant_responses: Optional[List[str]] = None
) -> List[Dict]:
    """
    Create a conversation history for chat models.

    Args:
        system_prompt: System instruction
        user_messages: List of user messages
        assistant_responses: Optional list of assistant responses

    Returns:
        List of formatted messages

    Example:
        >>> conversation = create_chat_conversation(
        ...     "You are a helpful assistant",
        ...     ["Hello", "How are you?"],
        ...     ["Hi there!", "I'm doing well!"]
        ... )
    """
    messages = [format_chat_message("system", system_prompt)]

    if assistant_responses is None:
        assistant_responses = []

    for i, user_msg in enumerate(user_messages):
        messages.append(format_chat_message("user", user_msg))
        if i < len(assistant_responses):
            messages.append(format_chat_message("assistant", assistant_responses[i]))

    return messages


def calculate_cost_comparison(
    prompt: str,
    expected_output_tokens: int,
    models: List[str]
) -> Dict:
    """
    Compare costs across different models.

    Args:
        prompt: The prompt text
        expected_output_tokens: Estimated output length
        models: List of model names to compare

    Returns:
        Dict with cost comparison data
    """
    input_tokens = count_tokens(prompt)
    comparison = {}

    for model in models:
        cost = estimate_cost(input_tokens, expected_output_tokens, model)
        comparison[model] = cost

    return comparison


# ==================== Local LLM (Ollama) Support ====================

def call_local_llm(
    prompt: str,
    model: str = "llama2:7b",
    temperature: float = 0.7,
    max_tokens: int = 500,
    options: Optional[Dict] = None
) -> str:
    """
    Call local LLM via Ollama.

    Args:
        prompt: The prompt text
        model: Ollama model name
        temperature: Sampling temperature
        max_tokens: Maximum tokens to generate
        options: Additional Ollama options

    Returns:
        str: Generated text

    Example:
        >>> response = call_local_llm("Explain AI", model="llama2:7b")
    """
    import requests
    import os

    base_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")

    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False,
        "options": options or {}
    }

    if temperature:
        payload["options"]["temperature"] = temperature
    if max_tokens:
        payload["options"]["num_predict"] = max_tokens

    try:
        response = requests.post(
            f"{base_url}/api/generate",
            json=payload,
            timeout=120
        )
        response.raise_for_status()
        return response.json().get("response", "")
    except Exception as e:
        return f"Error calling local LLM: {str(e)}"


def chat_local_llm(
    messages: List[Dict],
    model: str = "llama2:7b",
    temperature: float = 0.7,
    max_tokens: int = 500
) -> str:
    """
    Chat with local LLM using message format.

    Args:
        messages: List of message dicts with 'role' and 'content'
        model: Ollama model name
        temperature: Sampling temperature
        max_tokens: Maximum tokens to generate

    Returns:
        str: Assistant response

    Example:
        >>> messages = [
        ...     {"role": "user", "content": "Hello!"}
        ... ]
        >>> response = chat_local_llm(messages)
    """
    import requests
    import os

    base_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")

    payload = {
        "model": model,
        "messages": messages,
        "stream": False,
        "options": {
            "temperature": temperature,
            "num_predict": max_tokens
        }
    }

    try:
        response = requests.post(
            f"{base_url}/api/chat",
            json=payload,
            timeout=120
        )
        response.raise_for_status()
        return response.json().get("message", {}).get("content", "")
    except Exception as e:
        return f"Error calling local LLM: {str(e)}"


def stream_local_llm(prompt: str, model: str = "llama2:7b"):
    """
    Stream responses from local LLM.

    Args:
        prompt: The prompt text
        model: Ollama model name

    Yields:
        str: Text chunks

    Example:
        >>> for chunk in stream_local_llm("Write a story"):
        ...     print(chunk, end='')
    """
    import requests
    import os
    import json

    base_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")

    payload = {
        "model": model,
        "prompt": prompt,
        "stream": True
    }

    try:
        response = requests.post(
            f"{base_url}/api/generate",
            json=payload,
            stream=True,
            timeout=120
        )
        response.raise_for_status()

        for line in response.iter_lines():
            if line:
                chunk = json.loads(line)
                if "response" in chunk:
                    yield chunk["response"]
    except Exception as e:
        yield f"Error: {str(e)}"


# ==================== Azure OpenAI Support ====================

def call_azure_openai(
    prompt: str,
    deployment: str = "gpt-4",
    temperature: float = 0.7,
    max_tokens: int = 500
) -> str:
    """
    Call Azure OpenAI Service.

    Args:
        prompt: The prompt text
        deployment: Azure deployment name
        temperature: Sampling temperature
        max_tokens: Maximum tokens to generate

    Returns:
        str: Generated text

    Example:
        >>> response = call_azure_openai("Explain AI", deployment="gpt-4")
    """
    try:
        from openai import AzureOpenAI
        import os

        client = AzureOpenAI(
            api_key=os.getenv("AZURE_OPENAI_KEY"),
            api_version=os.getenv("AZURE_OPENAI_API_VERSION", "2024-02-15-preview"),
            azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
        )

        response = client.chat.completions.create(
            model=deployment,
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature,
            max_tokens=max_tokens
        )

        return response.choices[0].message.content
    except Exception as e:
        return f"Error calling Azure OpenAI: {str(e)}"


def chat_azure_openai(
    messages: List[Dict],
    deployment: str = "gpt-4",
    temperature: float = 0.7,
    max_tokens: int = 500
) -> str:
    """
    Chat with Azure OpenAI using message format.

    Args:
        messages: List of message dicts
        deployment: Azure deployment name
        temperature: Sampling temperature
        max_tokens: Maximum tokens

    Returns:
        str: Assistant response
    """
    try:
        from openai import AzureOpenAI
        import os

        client = AzureOpenAI(
            api_key=os.getenv("AZURE_OPENAI_KEY"),
            api_version=os.getenv("AZURE_OPENAI_API_VERSION", "2024-02-15-preview"),
            azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
        )

        response = client.chat.completions.create(
            model=deployment,
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens
        )

        return response.choices[0].message.content
    except Exception as e:
        return f"Error calling Azure OpenAI: {str(e)}"


def get_azure_embeddings(texts: List[str], deployment: str = "text-embedding-ada-002") -> List[List[float]]:
    """
    Get embeddings from Azure OpenAI.

    Args:
        texts: List of texts to embed
        deployment: Azure embedding deployment name

    Returns:
        List of embedding vectors
    """
    try:
        from openai import AzureOpenAI
        import os

        client = AzureOpenAI(
            api_key=os.getenv("AZURE_OPENAI_KEY"),
            api_version=os.getenv("AZURE_OPENAI_API_VERSION", "2024-02-15-preview"),
            azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
        )

        response = client.embeddings.create(
            model=deployment,
            input=texts
        )

        return [item.embedding for item in response.data]
    except Exception as e:
        print(f"Error getting embeddings: {str(e)}")
        return []


def stream_azure_openai(prompt: str, deployment: str = "gpt-4"):
    """
    Stream responses from Azure OpenAI.

    Args:
        prompt: The prompt text
        deployment: Azure deployment name

    Yields:
        str: Text chunks
    """
    try:
        from openai import AzureOpenAI
        import os

        client = AzureOpenAI(
            api_key=os.getenv("AZURE_OPENAI_KEY"),
            api_version=os.getenv("AZURE_OPENAI_API_VERSION", "2024-02-15-preview"),
            azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
        )

        stream = client.chat.completions.create(
            model=deployment,
            messages=[{"role": "user", "content": prompt}],
            stream=True
        )

        for chunk in stream:
            if chunk.choices[0].delta.content:
                yield chunk.choices[0].delta.content
    except Exception as e:
        yield f"Error: {str(e)}"


# ==================== Unified LLM Interface ====================

def call_llm(
    prompt: str,
    provider: Optional[str] = None,
    model: Optional[str] = None,
    **kwargs
) -> str:
    """
    Unified interface to call any LLM provider.

    Args:
        prompt: The prompt text
        provider: LLM provider ('openai', 'azure', 'ollama', 'anthropic')
                 If None, reads from LLM_PROVIDER env var
        model: Model/deployment name (provider-specific)
        **kwargs: Additional arguments for the provider

    Returns:
        str: Generated text

    Example:
        >>> # Use default provider from .env
        >>> response = call_llm("Explain AI")
        >>>
        >>> # Specify provider
        >>> response = call_llm("Explain AI", provider="ollama", model="llama2:7b")
    """
    import os

    if provider is None:
        provider = os.getenv("LLM_PROVIDER", "openai").lower()

    if provider == "ollama":
        model = model or os.getenv("OLLAMA_MODEL", "llama2:7b")
        return call_local_llm(prompt, model=model, **kwargs)

    elif provider == "azure":
        model = model or os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME", "gpt-4")
        return call_azure_openai(prompt, deployment=model, **kwargs)

    elif provider == "openai":
        # Use standard OpenAI client
        try:
            from openai import OpenAI
            client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
            model = model or os.getenv("OPENAI_MODEL", "gpt-4")

            response = client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": prompt}],
                **kwargs
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error calling OpenAI: {str(e)}"

    elif provider == "anthropic":
        # Use Anthropic client
        try:
            from anthropic import Anthropic
            client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
            model = model or os.getenv("ANTHROPIC_MODEL", "claude-3-opus-20240229")

            response = client.messages.create(
                model=model,
                max_tokens=kwargs.get("max_tokens", 1024),
                messages=[{"role": "user", "content": prompt}]
            )
            return response.content[0].text
        except Exception as e:
            return f"Error calling Anthropic: {str(e)}"

    else:
        return f"Unknown provider: {provider}"
