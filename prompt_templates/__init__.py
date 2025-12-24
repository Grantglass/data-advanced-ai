"""
Prompt Templates Library for MBA 590 - Advanced AI Strategy

This module provides reusable prompt templates for various business use cases.
"""

from typing import Dict, List, Optional
import json


class PromptTemplate:
    """
    A reusable prompt template with variable substitution.

    Attributes:
        name (str): Template name
        category (str): Template category (e.g., "business_analysis")
        technique (str): Prompting technique (e.g., "zero-shot", "few-shot", "chain-of-thought")
        template (str): The prompt template with {placeholders}
        variables (List[str]): List of variable names in the template
        description (str): Description of what the template does
        examples (List[Dict]): Example usages
    """

    def __init__(
        self,
        name: str,
        category: str,
        technique: str,
        template: str,
        variables: List[str],
        description: str = "",
        examples: Optional[List[Dict]] = None,
    ):
        self.name = name
        self.category = category
        self.technique = technique
        self.template = template
        self.variables = variables
        self.description = description
        self.examples = examples or []

    def fill(self, **kwargs) -> str:
        """
        Fill the template with provided variable values.

        Args:
            **kwargs: Variable values to substitute

        Returns:
            str: Filled prompt ready to use

        Raises:
            ValueError: If required variables are missing
        """
        missing = set(self.variables) - set(kwargs.keys())
        if missing:
            raise ValueError(f"Missing required variables: {missing}")

        return self.template.format(**kwargs)

    def to_dict(self) -> Dict:
        """Convert template to dictionary format."""
        return {
            "name": self.name,
            "category": self.category,
            "technique": self.technique,
            "template": self.template,
            "variables": self.variables,
            "description": self.description,
            "examples": self.examples,
        }

    def to_json(self) -> str:
        """Convert template to JSON string."""
        return json.dumps(self.to_dict(), indent=2)

    @classmethod
    def from_dict(cls, data: Dict) -> "PromptTemplate":
        """Create template from dictionary."""
        return cls(**data)

    @classmethod
    def from_json(cls, json_str: str) -> "PromptTemplate":
        """Create template from JSON string."""
        return cls.from_dict(json.loads(json_str))

    def __repr__(self) -> str:
        return f"PromptTemplate(name='{self.name}', category='{self.category}', technique='{self.technique}')"

    def __str__(self) -> str:
        return f"{self.name} ({self.technique}): {self.description}"


class PromptLibrary:
    """
    Manages a collection of prompt templates.
    """

    def __init__(self):
        self.templates: Dict[str, PromptTemplate] = {}

    def add(self, template: PromptTemplate):
        """Add a template to the library."""
        self.templates[template.name] = template

    def get(self, name: str) -> Optional[PromptTemplate]:
        """Get a template by name."""
        return self.templates.get(name)

    def list_by_category(self, category: str) -> List[PromptTemplate]:
        """List all templates in a category."""
        return [t for t in self.templates.values() if t.category == category]

    def list_by_technique(self, technique: str) -> List[PromptTemplate]:
        """List all templates using a specific technique."""
        return [t for t in self.templates.values() if t.technique == technique]

    def search(self, keyword: str) -> List[PromptTemplate]:
        """Search templates by keyword in name or description."""
        keyword = keyword.lower()
        return [
            t
            for t in self.templates.values()
            if keyword in t.name.lower() or keyword in t.description.lower()
        ]

    def __len__(self) -> int:
        return len(self.templates)

    def __repr__(self) -> str:
        return f"PromptLibrary(templates={len(self.templates)})"


# Create global library instance
library = PromptLibrary()


# Export main classes
__all__ = ["PromptTemplate", "PromptLibrary", "library"]
