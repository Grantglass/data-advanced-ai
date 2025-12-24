"""
Utilities for MBA 590 - Advanced AI Strategy Course

Common helper functions for working with LLMs, data, and prompts in Jupyter notebooks.
"""

from .llm_helpers import (
    count_tokens,
    estimate_cost,
    create_mock_llm_response,
    format_chat_message
)

from .data_helpers import (
    load_sample_data,
    save_results,
    display_dataframe,
    create_comparison_chart
)

from .prompt_helpers import (
    validate_prompt,
    measure_prompt_quality,
    compare_prompts
)

from .evaluation_helpers import (
    calculate_bleu,
    calculate_rouge,
    calculate_similarity,
    create_evaluation_report
)

__version__ = "1.0.0"

__all__ = [
    # LLM Helpers
    "count_tokens",
    "estimate_cost",
    "create_mock_llm_response",
    "format_chat_message",
    # Data Helpers
    "load_sample_data",
    "save_results",
    "display_dataframe",
    "create_comparison_chart",
    # Prompt Helpers
    "validate_prompt",
    "measure_prompt_quality",
    "compare_prompts",
    # Evaluation Helpers
    "calculate_bleu",
    "calculate_rouge",
    "calculate_similarity",
    "create_evaluation_report",
]
