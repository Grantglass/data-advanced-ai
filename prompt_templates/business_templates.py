"""
Business Analysis Prompt Templates

Ready-to-use templates for common business analysis tasks.
"""

from . import PromptTemplate, library


# SWOT Analysis Template
swot_analysis = PromptTemplate(
    name="swot_analysis",
    category="business_analysis",
    technique="structured-output",
    description="Generate a comprehensive SWOT analysis for a business scenario",
    template="""Conduct a detailed SWOT analysis for the following business scenario:

Context: {context}
Company/Product: {subject}
Market: {market}

Provide your analysis in the following format:

## Strengths
- [List 4-6 internal positive attributes]

## Weaknesses
- [List 4-6 internal challenges or limitations]

## Opportunities
- [List 4-6 external favorable conditions or trends]

## Threats
- [List 4-6 external risks or challenges]

For each item, provide a brief explanation of why it matters and its potential impact.""",
    variables=["context", "subject", "market"],
    examples=[
        {
            "context": "A company planning to launch an AI-powered customer service platform",
            "subject": "SmartSupport AI Platform",
            "market": "Mid-market B2B SaaS companies"
        }
    ]
)

library.add(swot_analysis)


# Competitive Analysis Template
competitive_analysis = PromptTemplate(
    name="competitive_analysis",
    category="business_analysis",
    technique="chain-of-thought",
    description="Analyze competitors systematically with structured reasoning",
    template="""Analyze our competitive position using the following approach:

Our Company: {our_company}
Competitors: {competitors}
Market Segment: {market_segment}

Step 1: For each competitor, identify:
- Core strengths and differentiators
- Weaknesses or gaps
- Market positioning

Step 2: Compare across these dimensions:
- Product/Service features
- Pricing strategy
- Customer base
- Technology stack
- Market share

Step 3: Identify:
- Our competitive advantages
- Areas where we're behind
- White space opportunities
- Strategic threats

Step 4: Recommend:
- Top 3 strategic priorities to strengthen our position
- Specific actions to differentiate from competitors

Provide detailed reasoning for each step.""",
    variables=["our_company", "competitors", "market_segment"],
    examples=[
        {
            "our_company": "AI Automation startup focusing on SMBs",
            "competitors": "Zapier, Make.com, UiPath",
            "market_segment": "SMB workflow automation"
        }
    ]
)

library.add(competitive_analysis)


# Market Opportunity Assessment Template
market_opportunity = PromptTemplate(
    name="market_opportunity",
    category="business_analysis",
    technique="structured-output",
    description="Assess and prioritize market opportunities",
    template="""Evaluate the following market opportunity:

Opportunity: {opportunity_description}
Target Market: {target_market}
Current Market Size: {market_size}
Growth Rate: {growth_rate}

Analyze across these dimensions:

1. **Market Attractiveness** (Score 1-10)
   - Market size and growth potential
   - Competitive intensity
   - Profit margins
   - Market maturity

2. **Strategic Fit** (Score 1-10)
   - Alignment with core competencies
   - Resource requirements
   - Risk profile
   - Time to market

3. **Competitive Position** (Score 1-10)
   - Differentiation potential
   - Barriers to entry
   - Existing advantages
   - Threat of substitutes

4. **Financial Potential**
   - Revenue opportunity (3-year projection)
   - Required investment
   - Expected ROI
   - Break-even timeline

5. **Overall Recommendation**
   - Go/No-Go decision with rationale
   - Key success factors
   - Critical risks to mitigate
   - Recommended next steps""",
    variables=["opportunity_description", "target_market", "market_size", "growth_rate"],
    examples=[
        {
            "opportunity_description": "AI-powered contract analysis for legal teams",
            "target_market": "Mid-size law firms (50-200 lawyers)",
            "market_size": "$2.5B annually",
            "growth_rate": "18% CAGR"
        }
    ]
)

library.add(market_opportunity)


# Business Case Development Template
business_case = PromptTemplate(
    name="business_case",
    category="business_analysis",
    technique="structured-output",
    description="Develop a comprehensive business case for an initiative",
    template="""Create a comprehensive business case for the following initiative:

Initiative: {initiative_name}
Objective: {objective}
Proposed Investment: {investment}

Develop the business case with these sections:

## Executive Summary
- Brief overview of the initiative (2-3 sentences)
- Key benefits and expected ROI
- Recommendation

## Problem Statement
- Current state and challenges
- Impact on the organization
- Why this initiative is needed now

## Proposed Solution
- Description of the initiative
- How it addresses the problem
- Key features or components

## Strategic Alignment
- How this supports organizational objectives
- Strategic importance
- Stakeholders impacted

## Financial Analysis
- Total investment required
- Expected benefits (quantified)
- ROI calculation
- Payback period

## Implementation Approach
- High-level timeline
- Resource requirements
- Key milestones
- Dependencies

## Risk Assessment
- Top 3-5 risks
- Mitigation strategies
- Contingency plans

## Success Criteria
- Measurable outcomes
- KPIs to track
- Timeline for achieving benefits

## Recommendation
- Clear go/no-go recommendation
- Critical success factors
- Next steps""",
    variables=["initiative_name", "objective", "investment"],
    examples=[
        {
            "initiative_name": "Enterprise-wide AI Training Program",
            "objective": "Build AI literacy across 500 employees",
            "investment": "$250,000"
        }
    ]
)

library.add(business_case)


# Export all templates
__all__ = [
    "swot_analysis",
    "competitive_analysis",
    "market_opportunity",
    "business_case"
]
