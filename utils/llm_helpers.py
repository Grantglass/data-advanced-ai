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
