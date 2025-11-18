# Prompt Templates Library

This directory contains reusable prompt templates organized by use case and prompting technique.

## Organization

- `business_analysis/` - Templates for market research, competitive analysis, SWOT, etc.
- `customer_service/` - Templates for support responses, escalation handling, etc.
- `content_creation/` - Templates for marketing copy, product descriptions, etc.
- `data_analysis/` - Templates for data interpretation, trend analysis, etc.
- `technical/` - Templates for code review, documentation, debugging, etc.
- `strategic/` - Templates for planning, decision-making, risk assessment, etc.

## Usage

Each template file includes:
- **Purpose**: What the template is for
- **Technique**: Prompting approach used (zero-shot, few-shot, CoT, etc.)
- **Template**: The actual prompt with placeholders
- **Example**: Sample usage
- **Best Practices**: Tips for optimal results

## Template Format

```python
from prompt_templates import PromptTemplate

template = PromptTemplate(
    name="Template Name",
    category="Category",
    technique="Technique",
    template="Your prompt with {placeholders}",
    variables=["placeholder1", "placeholder2"]
)

# Use the template
filled_prompt = template.fill(
    placeholder1="value1",
    placeholder2="value2"
)
```

## Available Templates

### Business Analysis
- `competitive_analysis.py` - Analyze competitors
- `market_opportunity.py` - Identify market opportunities
- `swot_analysis.py` - Generate SWOT analysis

### Customer Service
- `complaint_response.py` - Handle customer complaints
- `product_inquiry.py` - Answer product questions
- `escalation_handler.py` - Manage escalations

### Content Creation
- `product_description.py` - Write product descriptions
- `email_campaign.py` - Create marketing emails
- `social_media.py` - Generate social posts

### Data Analysis
- `trend_analysis.py` - Analyze trends
- `summary_statistics.py` - Summarize data insights
- `anomaly_detection.py` - Identify anomalies

### Technical
- `code_review.py` - Review code
- `bug_diagnosis.py` - Diagnose bugs
- `api_documentation.py` - Document APIs

### Strategic
- `decision_framework.py` - Structure decisions
- `risk_assessment.py` - Assess risks
- `roadmap_planning.py` - Plan roadmaps

## Contributing

To add a new template:
1. Create a new Python file in the appropriate category folder
2. Follow the template structure shown above
3. Include comprehensive documentation and examples
4. Test with various inputs

## License

These templates are provided for educational purposes as part of the MBA 590 course.
