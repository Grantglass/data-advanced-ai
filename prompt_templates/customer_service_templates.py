"""
Customer Service Prompt Templates

Templates for handling customer inquiries, complaints, and support scenarios.
"""

from . import PromptTemplate, library


# Complaint Response Template
complaint_response = PromptTemplate(
    name="complaint_response",
    category="customer_service",
    technique="role-playing",
    description="Generate empathetic, solution-oriented responses to customer complaints",
    template="""You are a senior customer service representative at {company_name}, known for exceptional empathy, professionalism, and problem-solving skills. {company_values}

Customer Situation:
- Customer Name: {customer_name}
- Issue: {issue_description}
- Customer Sentiment: {sentiment}
- Previous Interactions: {previous_context}

Craft a response that:
1. Acknowledges the customer's frustration and validates their feelings
2. Apologizes sincerely for the inconvenience
3. Explains what happened (if appropriate)
4. Offers a clear solution or next steps
5. Provides direct contact information for follow-up
6. Thanks them for their patience and continued business

Tone: Professional, warm, empathetic, and solution-focused
Length: 150-250 words

Write the email response:""",
    variables=["company_name", "company_values", "customer_name", "issue_description", "sentiment", "previous_context"],
    examples=[
        {
            "company_name": "TechGear Pro",
            "company_values": "We pride ourselves on quality products and exceptional customer care.",
            "customer_name": "Sarah Johnson",
            "issue_description": "Received a laptop with a cracked screen",
            "sentiment": "Frustrated but polite",
            "previous_context": "First-time customer, ordered 5 days ago"
        }
    ]
)

library.add(complaint_response)


# Product Inquiry Response Template
product_inquiry = PromptTemplate(
    name="product_inquiry",
    category="customer_service",
    technique="few-shot",
    description="Answer product questions with helpful, detailed information",
    template="""Answer customer product inquiries following this style:

Example 1:
Q: What's the battery life of the UltraBook Pro?
A: Great question! The UltraBook Pro offers up to 12 hours of battery life with typical use (web browsing, document editing, video streaming). For more intensive tasks like video editing, you can expect 8-10 hours. The battery also supports fast charging - you'll get 50% charge in just 30 minutes.

Example 2:
Q: Is the CloudSync service compatible with my existing tools?
A: Absolutely! CloudSync integrates seamlessly with all major productivity tools including Microsoft Office 365, Google Workspace, Slack, and Salesforce. We also offer a REST API for custom integrations. Would you like me to send you our integration guide?

Now answer this customer inquiry:

Product: {product_name}
Customer Question: {customer_question}
Key Product Details: {product_details}

Provide a helpful, informative response that:
- Directly answers the question
- Includes relevant technical details
- Suggests additional helpful information
- Offers to provide more resources if needed
- Uses a friendly, conversational tone""",
    variables=["product_name", "customer_question", "product_details"],
    examples=[
        {
            "product_name": "SmartHome Hub Max",
            "customer_question": "Can I control my existing smart devices with this hub?",
            "product_details": "Supports Zigbee, Z-Wave, Wi-Fi, Bluetooth. Compatible with 5000+ devices. Works with Alexa, Google Home, Apple HomeKit."
        }
    ]
)

library.add(product_inquiry)


# Escalation Handling Template
escalation_handler = PromptTemplate(
    name="escalation_handler",
    category="customer_service",
    technique="chain-of-thought",
    description="Handle escalated customer issues with systematic problem-solving",
    template="""Handle this escalated customer issue using a systematic approach:

Escalation Details:
- Customer: {customer_name} ({customer_tier})
- Issue: {issue}
- Previous Attempts to Resolve: {previous_attempts}
- Business Impact: {impact}
- Customer Emotion Level: {emotion_level}

Think through this step-by-step:

Step 1: Assess the Situation
- What is the root cause?
- What has already been tried?
- What is the customer's primary concern?
- What are the stakes for the customer?

Step 2: Identify Options
- What solutions are available?
- What are the trade-offs of each option?
- What can we offer that goes beyond standard protocol?
- What resources do we need?

Step 3: Determine Best Approach
- Which solution best addresses the root cause?
- How can we exceed expectations given the escalation?
- What can we do to rebuild trust?

Step 4: Craft Response
Write a response that:
- Takes full ownership of the situation
- Presents the solution clearly
- Explains the special accommodations being made
- Provides a direct escalation contact
- Sets clear expectations and timeline
- Includes a gesture of goodwill (if appropriate)

Provide your analysis for each step, then the final response.""",
    variables=["customer_name", "customer_tier", "issue", "previous_attempts", "impact", "emotion_level"],
    examples=[
        {
            "customer_name": "David Chen",
            "customer_tier": "Enterprise (3-year customer)",
            "issue": "Critical service outage during product launch - 3 hours downtime",
            "previous_attempts": "Standard troubleshooting, tier 1 and tier 2 support",
            "impact": "Lost revenue, damaged reputation with their customers",
            "emotion_level": "Very frustrated, considering alternatives"
        }
    ]
)

library.add(escalation_handler)


# Export all templates
__all__ = [
    "complaint_response",
    "product_inquiry",
    "escalation_handler"
]
