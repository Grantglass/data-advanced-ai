"""
Prompt Helper Functions

Utilities for creating, validating, and analyzing prompts.
"""

from typing import Dict, List, Optional
import re


def validate_prompt(prompt: str) -> Dict[str, any]:
    """
    Validate a prompt and provide quality feedback.

    Args:
        prompt: The prompt text to validate

    Returns:
        Dict with validation results and suggestions
    """
    issues = []
    suggestions = []
    score = 100

    # Check length
    if len(prompt) < 20:
        issues.append("Prompt is very short")
        suggestions.append("Add more context and specific instructions")
        score -= 20

    # Check for vague language
    vague_words = ["some", "maybe", "might", "could", "things", "stuff"]
    found_vague = [word for word in vague_words if word in prompt.lower()]
    if found_vague:
        issues.append(f"Contains vague language: {', '.join(found_vague)}")
        suggestions.append("Use specific, concrete language")
        score -= 10

    # Check for clear instructions
    instruction_words = [
        "create",
        "generate",
        "analyze",
        "explain",
        "list",
        "summarize",
    ]
    has_instruction = any(word in prompt.lower() for word in instruction_words)
    if not has_instruction:
        issues.append("No clear action verb found")
        suggestions.append(
            "Start with a clear instruction (e.g., 'Analyze', 'Create', 'Explain')"
        )
        score -= 15

    # Check for structure
    has_structure = any(char in prompt for char in ["1.", "2.", "-", "*", "\n\n"])
    if not has_structure and len(prompt) > 200:
        suggestions.append(
            "Consider adding structure with bullet points or numbered lists"
        )
        score -= 5

    # Check for output format specification
    format_keywords = ["format", "structure", "template", "example", "json", "markdown"]
    has_format = any(keyword in prompt.lower() for keyword in format_keywords)
    if not has_format and len(prompt) > 100:
        suggestions.append("Consider specifying the desired output format")
        score -= 5

    return {
        "score": max(0, score),
        "issues": issues,
        "suggestions": suggestions,
        "is_valid": score >= 60,
        "word_count": len(prompt.split()),
        "char_count": len(prompt),
    }


def measure_prompt_quality(
    prompt: str, criteria: Optional[List[str]] = None
) -> Dict[str, float]:
    """
    Measure prompt quality across multiple criteria.

    Args:
        prompt: The prompt to measure
        criteria: List of criteria to evaluate

    Returns:
        Dict with scores for each criterion (0-10 scale)
    """
    if criteria is None:
        criteria = ["clarity", "specificity", "structure", "completeness"]

    scores = {}

    # Clarity (based on sentence structure and vocabulary)
    if "clarity" in criteria:
        avg_sent_length = len(prompt.split()) / max(1, prompt.count("."))
        clarity_score = (
            10 if avg_sent_length <= 20 else max(0, 10 - (avg_sent_length - 20) / 5)
        )
        scores["clarity"] = round(clarity_score, 1)

    # Specificity (based on concrete vs. abstract language)
    if "specificity" in criteria:
        specific_words = [
            "example",
            "specifically",
            "exactly",
            "precisely",
            "must",
            "should",
        ]
        spec_count = sum(1 for word in specific_words if word in prompt.lower())
        scores["specificity"] = min(10, spec_count * 2)

    # Structure (based on formatting elements)
    if "structure" in criteria:
        structure_elements = [
            "\n\n" in prompt,  # Paragraphs
            any(c in prompt for c in ["1.", "2.", "3."]),  # Numbered lists
            any(c in prompt for c in ["-", "*", "•"]),  # Bullet points
            "**" in prompt or "__" in prompt,  # Bold formatting
            len(prompt.split("\n")) > 3,  # Multiple lines
        ]
        scores["structure"] = sum(structure_elements) * 2

    # Completeness (based on key components)
    if "completeness" in criteria:
        components = [
            any(
                word in prompt.lower()
                for word in ["context:", "background:", "situation:"]
            ),  # Context
            any(
                word in prompt.lower() for word in ["task:", "objective:", "goal:"]
            ),  # Task
            any(
                word in prompt.lower() for word in ["output:", "format:", "structure:"]
            ),  # Output spec
            any(
                word in prompt.lower() for word in ["example:", "like:", "such as:"]
            ),  # Examples
        ]
        scores["completeness"] = sum(components) * 2.5

    return scores


def compare_prompts(
    prompts: Dict[str, str], comparison_criteria: Optional[List[str]] = None
) -> Dict:
    """
    Compare multiple prompts across quality criteria.

    Args:
        prompts: Dict of {name: prompt_text}
        comparison_criteria: List of criteria to compare

    Returns:
        Dict with comparison results
    """
    results = {}

    for name, prompt in prompts.items():
        validation = validate_prompt(prompt)
        quality = measure_prompt_quality(prompt, comparison_criteria)

        results[name] = {
            "validation_score": validation["score"],
            "word_count": validation["word_count"],
            "quality_scores": quality,
            "average_quality": sum(quality.values()) / len(quality) if quality else 0,
            "issues": validation["issues"],
            "suggestions": validation["suggestions"],
        }

    return results


def extract_variables(prompt: str, delimiter: str = "{}") -> List[str]:
    """
    Extract variable placeholders from a prompt template.

    Args:
        prompt: Prompt text with variables
        delimiter: Variable delimiter (default: {})

    Returns:
        List of variable names
    """
    if delimiter == "{}":
        pattern = r"\{([^}]+)\}"
    else:
        pattern = f"{delimiter}([^{delimiter}]+){delimiter}"

    variables = re.findall(pattern, prompt)
    return list(set(variables))  # Remove duplicates


def fill_template(prompt_template: str, **kwargs) -> str:
    """
    Fill a prompt template with provided values.

    Args:
        prompt_template: Template with {placeholders}
        **kwargs: Values for placeholders

    Returns:
        Filled prompt

    Example:
        >>> template = "Analyze {topic} for {audience}"
        >>> fill_template(template, topic="AI trends", audience="executives")
    """
    return prompt_template.format(**kwargs)
