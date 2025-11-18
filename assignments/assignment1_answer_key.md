# Assignment 1: Answer Key & Sample Solutions

## MBA 590 - Advanced AI Strategy
**Instructor Reference Only - Do Not Distribute to Students**

---

## Part 1: Business Scenario Selection (10 points)

### Exemplary Response Example

**Scenario: Customer Service Automation**

```python
chosen_scenario = """
Scenario Name: AI-Powered Customer Support Ticket Classification

Description:
Our e-commerce company receives 5,000+ customer support tickets daily. Currently,
human agents manually categorize each ticket (Refund, Technical, Billing, Product
Question, Complaint), causing 2-4 hour delays before tickets reach the right
specialist. We need an AI system to instantly classify tickets and route them
appropriately, reducing response time to under 30 minutes.

Business Context:
- Current cost: 15 agents × $40K/year = $600K for classification alone
- Average ticket value: $85
- Customer churn from delays: estimated 8% of dissatisfied customers
- NPS impact: -12 points from slow response times

Success Criteria:
- 95%+ classification accuracy
- <5 second classification time per ticket
- Reduce routing errors from current 12% to <3%
- ROI positive within 6 months
- Maintain audit trail for compliance
"""
```

### Grading Criteria:
- ✅ Clear business problem statement (2 pts)
- ✅ Specific quantitative context (3 pts)
- ✅ Measurable success criteria (3 pts)
- ✅ Realistic scope appropriate for assignment (2 pts)

---

## Part 2: Implement Five Prompting Techniques (40 points)

### Technique 1: Zero-Shot (8 points)

**Exemplary Response:**

```python
zero_shot_prompt = """
You are a customer service ticket classifier. Analyze the following customer
message and classify it into exactly one category:
- REFUND: Customer wants money back
- TECHNICAL: Product not working, bug, or technical issue
- BILLING: Payment, invoice, or charge questions
- PRODUCT: Questions about features, specifications, or usage
- COMPLAINT: General dissatisfaction or negative feedback

Ticket: "I was charged twice for my order #12345. I only received one package
but my credit card shows two charges of $49.99 each. Please fix this ASAP."

Category:
"""

zero_shot_output = """
Category: BILLING

(Note: This correctly identifies the duplicate charge issue as a billing matter)
"""
```

**Grading Criteria:**
- Clear task definition (2 pts)
- Appropriate category definitions (2 pts)
- Realistic test case (2 pts)
- Reasonable expected output (2 pts)

---

### Technique 2: Few-Shot Learning (8 points)

**Exemplary Response:**

```python
few_shot_prompt = """
Classify customer service tickets into categories. Format: Category | Confidence | Reasoning

Examples:

Ticket: "This product is amazing! Just wanted to say thank you."
Category: PRODUCT | High | Positive feedback about product quality, no action needed

Ticket: "I haven't received my refund yet. It's been 10 business days."
Category: REFUND | High | Customer following up on refund status

Ticket: "The app crashes every time I try to log in."
Category: TECHNICAL | High | Software malfunction preventing product use

Ticket: "My invoice shows the wrong billing address."
Category: BILLING | High | Invoice/billing information error

Now classify:
Ticket: "I want to return this item. It doesn't fit and I'd like my money back."
"""

few_shot_output = """
Category: REFUND | High | Customer explicitly requesting return and monetary refund
"""
```

**Grading Criteria:**
- 2-3 diverse examples provided (2 pts)
- Consistent format across examples (2 pts)
- Examples cover different categories (2 pts)
- Test case different from examples (2 pts)

---

### Technique 3: Chain-of-Thought (CoT) (8 points)

**Exemplary Response:**

```python
cot_prompt = """
Classify this customer ticket using step-by-step reasoning:

Ticket: "I ordered the Premium subscription but I'm still seeing ads. Also,
I was charged $29.99 instead of the $19.99 promotional price advertised."

Let's analyze step by step:

Step 1: Identify all issues mentioned
Step 2: Determine which issue is primary vs. secondary
Step 3: Check if issues are related or separate
Step 4: Assign primary category
Step 5: Flag if multiple categories apply
Step 6: Provide routing recommendation
"""

cot_output = """
Step 1: Issues mentioned:
  - Premium subscription not working (seeing ads)
  - Incorrect pricing ($29.99 charged vs $19.99 advertised)

Step 2: Primary vs. secondary:
  - Primary: Billing issue (incorrect charge amount)
  - Secondary: Technical issue (ads still showing)

Step 3: Relationship analysis:
  - Issues ARE related - wrong charge + wrong service level
  - Likely cause: Customer charged for wrong subscription tier

Step 4: Primary category: BILLING
  - The pricing discrepancy is the root cause

Step 5: Multiple categories: YES
  - Primary: BILLING
  - Secondary: TECHNICAL

Step 6: Routing recommendation:
  - Route to Billing specialist first
  - Billing should verify subscription tier, correct charge
  - May need escalation to Technical if subscription not applied correctly
  - Priority: HIGH (customer paying for service not received)
"""
```

**Grading Criteria:**
- Explicit step-by-step structure (2 pts)
- Logical reasoning progression (2 pts)
- Complex scenario requiring multi-step analysis (2 pts)
- Actionable conclusion (2 pts)

---

### Technique 4: Self-Ask / Least-to-Most (8 points)

**Exemplary Response:**

```python
decomposition_prompt = """
Complex ticket classification using Self-Ask method:

Ticket: "I'm extremely frustrated. I've called 3 times about my refund. The
product arrived damaged, I sent photos as requested, was promised a refund in
5-7 days, and it's now been 3 weeks. This is unacceptable customer service.
I'm disputing the charge with my credit card company if not resolved today."

Let's break this down with sub-questions:

Sub-question 1: What is the customer's primary request?
Sub-question 2: What is the history of this issue?
Sub-question 3: What is the urgency level?
Sub-question 4: Are there escalation triggers present?
Sub-question 5: What category best serves the customer's need?
Sub-question 6: What immediate actions are required?
"""

decomposition_output = """
Answer 1: Primary request is a refund for damaged product

Answer 2: History:
- Product arrived damaged (original issue)
- Customer provided photo evidence
- Refund promised (5-7 days)
- 3 weeks have passed
- Customer called 3 times previously
- Promise not fulfilled

Answer 3: Urgency level: CRITICAL
- Customer threatening credit card dispute
- Multiple contact attempts
- Time-sensitive demand ("today")

Answer 4: Escalation triggers: YES
- Threat of chargeback
- Multiple failed contact attempts
- Tone indicates high dissatisfaction
- Potential public complaint/review risk

Answer 5: Category: REFUND + ESCALATION
- Primary: REFUND (core issue)
- Flag: URGENT_ESCALATION

Answer 6: Immediate actions:
- Route to senior refund specialist
- Process refund immediately (same day)
- Customer communication within 1 hour
- Add note preventing automatic responses
- Follow-up protocol to prevent chargeback
- Document for service recovery analysis
"""
```

**Grading Criteria:**
- Systematic decomposition into sub-questions (2 pts)
- Each sub-question answered thoroughly (2 pts)
- Complex, multi-faceted scenario (2 pts)
- Synthesis of answers into actionable recommendation (2 pts)

---

### Technique 5: RAG / Prompt Chaining (8 points)

**Exemplary Response:**

```python
# Chain 1: Extract key information
advanced_prompt_chain1 = """
Extract the following structured information from this support ticket:

Ticket: "Order #45821 - I received the wrong color. I ordered black headphones
but got white ones. Can I exchange them? Also, do I need to pay return shipping?"

Extract:
- Order number:
- Issue type:
- Product details:
- Customer request:
- Additional questions:
"""

# Chain 2: Check knowledge base (RAG simulation)
advanced_prompt_chain2 = """
Based on extracted info:
- Order: #45821
- Issue: Wrong color received (ordered black, got white)
- Request: Exchange
- Question: Return shipping cost?

Retrieve relevant policies:
[KNOWLEDGE BASE RESULTS]
- Return Policy: 30-day free returns/exchanges
- Wrong Item Policy: Company covers return shipping for shipping errors
- Exchange Process: Initiate online, receive prepaid label
"""

# Chain 3: Generate response using context
advanced_prompt_chain3 = """
Using the ticket analysis and policy information, classify and draft response:

Classification: REFUND/EXCHANGE
Priority: STANDARD
Sentiment: NEUTRAL

Draft response:
'I sincerely apologize for sending you the wrong color headphones. Since this
was our error, we'll make it right at no cost to you.

Here's what happens next:
1. We're sending you a prepaid return label via email (no shipping cost)
2. Once we receive the white headphones, we'll immediately ship black ones
3. You'll receive tracking info within 24 hours of our warehouse receiving the return

Alternative: If you'd prefer a refund instead, we can process that immediately.

Your order #45821 is flagged as priority for processing. Expected resolution: 3-5 business days.

Is there anything else I can help with?'
"""
```

**Grading Criteria:**
- Clear chaining structure with multiple prompts (2 pts)
- Each chain builds on previous output (2 pts)
- Demonstrates RAG concept (knowledge retrieval) (2 pts)
- Final output incorporates all context (2 pts)

---

## Part 3: Comparative Analysis (30 points)

### Exemplary Ratings & Justification

```python
comparison_data = {
    'Technique': ['Zero-Shot', 'Few-Shot', 'CoT', 'Decomposition', 'Advanced'],
    'Output Quality': [3, 4, 5, 5, 4],
    'Consistency': [2, 4, 4, 3, 5],
    'Ease of Implementation': [5, 4, 3, 3, 2],
    'Token Efficiency': [5, 3, 2, 2, 1],
    'Business Value': [3, 4, 5, 4, 5]
}
```

**Grading Criteria:**
- Ratings supported by evidence (10 pts)
- Visualization created and labeled (5 pts)
- Written analysis addresses all questions (15 pts)

---

### 3.1 Which technique performed best? (Sample Answer)

**Exemplary Response:**

"Chain-of-Thought (CoT) performed best for customer service ticket classification because
our scenario involves complex, multi-issue tickets that require nuanced decision-making.

CoT excelled in three critical areas:

First, **accuracy on complex cases**: When tickets contained multiple issues (billing +
technical), CoT correctly identified primary vs. secondary concerns, achieving 94% accuracy
vs. 78% for Zero-Shot on our test set of 50 complex tickets.

Second, **transparency for audit requirements**: The step-by-step reasoning creates an
audit trail showing why each classification decision was made. This is crucial for
compliance in financial services and for training new agents on edge cases.

Third, **actionable routing**: CoT didn't just classify—it provided context for proper
routing (e.g., 'Route to Billing first, then escalate to Technical if needed'). This
reduced misroutes by 45% compared to simple classification.

However, CoT uses 3-4x more tokens than Zero-Shot ($0.08 vs $0.02 per classification
with GPT-4). For our 5,000 daily tickets, this is $400/day vs $100/day—an additional
$109K annually. Given the $600K we save in staffing costs, this 18% premium is justified
by the quality improvement."

**Grading (5 pts):**
- Clear thesis statement (1 pt)
- Multiple supporting reasons with evidence (2 pts)
- Quantitative justification (1 pt)
- Addresses trade-offs (1 pt)

---

### 3.2 Key trade-offs between techniques (Sample Answer)

**Exemplary Response:**

"The fundamental trade-off is between **cost/speed** and **quality/explainability**.

**Zero-Shot vs. Few-Shot:**
Zero-Shot is 65% faster (0.3s vs. 0.9s response time) and uses 50% fewer tokens, but
Few-Shot improved consistency by 28% on our benchmark. For high-volume, straightforward
classification, Zero-Shot suffices. For customer-facing applications where consistency
matters, Few-Shot's premium is worthwhile.

**Few-Shot vs. CoT:**
CoT provided superior reasoning transparency but increased token costs by 250%. The
key trade-off is explainability vs. scale. For 100,000+ daily classifications, Few-Shot
is more economical. For high-stakes decisions (executive escalations, legal issues),
CoT's transparency justifies the cost.

**Decomposition vs. Chain:**
Self-Ask decomposition excelled at identifying escalation needs (95% accuracy vs. 82%
for Few-Shot) but required 4x processing time. Prompt chaining offered the best of all
approaches but needed infrastructure investment (vector database, knowledge base).

**Strategic recommendation:** Use a tiered approach:
- Tier 1 (70% of tickets): Few-Shot classification
- Tier 2 (25% of tickets): CoT for complex cases
- Tier 3 (5% of tickets): Full decomposition for escalations

This optimizes cost while maintaining quality where it matters most."

**Grading (5 pts):**
- Identifies multiple specific trade-offs (2 pts)
- Provides quantitative comparisons (1 pt)
- Business context for trade-offs (1 pt)
- Strategic synthesis (1 pt)

---

### 3.3 Cost considerations impact (Sample Answer)

**Exemplary Response:**

"Cost analysis fundamentally changes the recommendation from 'best performance' to
'best value.'

**Current State Costs:**
- 15 agents × $40K = $600K/year
- Average 12-minute handling time per ticket

**Proposed AI Costs (5,000 tickets/day, 1.8M/year):**
- Zero-Shot: $0.02/ticket = $36K/year + $50K implementation = $86K total
- CoT: $0.08/ticket = $144K/year + $50K implementation = $194K total
- Chaining: $0.15/ticket = $270K/year + $150K implementation = $420K total

**All options show strong ROI** (86-600K savings), but the cost spread is 5x.

**The critical insight:** We don't need uniform quality across all 5,000 daily tickets.
**Recommendation:**
- 80% standard tickets → Few-Shot ($64K/year)
- 15% complex tickets → CoT ($22K/year)
- 5% escalations → Chaining ($14K/year)
- **Total: $100K vs. $600K = 83% cost reduction**

This tiered approach delivers CoT-level outcomes for complex cases while maintaining
cost efficiency overall. The $500K savings funds the AI implementation in 2 months."

**Grading (5 pts):**
- Specific cost calculations (2 pts)
- Comparison across techniques (1 pt)
- ROI analysis (1 pt)
- Cost-optimized recommendation (1 pt)

---

## Part 4: Strategic Recommendations (20 points)

### 4.1 Implementation Roadmap (Sample Answer)

**Exemplary Response:**

"**Phase 1: Pilot & Validate (Months 1-2)**

Begin with Few-Shot classification on 10% of ticket volume (500/day) for non-critical
categories (PRODUCT questions only). This low-risk start builds confidence and provides
baseline metrics.

Success metrics: 90%+ accuracy, <5% misrouting rate, agent satisfaction survey >4/5

Infrastructure: Single API integration, simple classification script, human review queue

**Phase 2: Scale & Optimize (Months 3-4)**

Expand to 50% of volume (2,500/day) and all categories except escalations. Introduce
CoT for complex multi-issue tickets (identified by keyword triggers).

Add: Confidence scoring (auto-route >95% confidence, human review 80-95%)

Success metrics: 93%+ accuracy, 30% reduction in routing time, <2% escalation rate

**Phase 3: Advanced Features (Months 5-6)**

Implement full prompt chaining with RAG for 100% of tickets. Build knowledge base of
past resolutions, policies, and FAQs. Add automated response drafting for high-confidence
classifications.

Final state: AI classifies and drafts responses, humans review and send. Expected 60%
full automation rate, 40% human-in-loop.

Success metrics: 95%+ accuracy, <30min response time, $500K annual savings achieved"

**Grading (7 pts):**
- Phased approach with timelines (2 pts)
- Increasing complexity per phase (2 pts)
- Specific success metrics per phase (2 pts)
- Realistic scope and progression (1 pt)

---

### 4.2 Risk Assessment (Sample Answer)

**Exemplary Response:**

"**Risk 1: Classification Errors Leading to Customer Dissatisfaction**

Impact: Misrouted tickets delay resolution, frustrate customers, potentially cause churn

Mitigation:
- Implement confidence thresholds (auto-route only >95% confidence)
- Human review queue for 80-95% confidence classifications
- Weekly accuracy audits with random sampling (200 tickets/week)
- Rapid feedback loop: agents can flag errors, which retrain the model
- Escalation path: customers can request human assistance at any time

**Risk 2: Prompt Injection / Adversarial Inputs**

Impact: Malicious customers could craft tickets to manipulate classification, potentially
routing high-priority issues to wrong queues or extracting sensitive information

Mitigation:
- Input sanitization (strip unusual characters, limit ticket length)
- Prompt design: System role clearly separated from user input
- Monitoring: Flag tickets with unusual patterns for review
- Rate limiting: Prevent bulk manipulation attempts
- Security testing: Red team exercises to identify vulnerabilities

**Risk 3: Over-reliance on AI Reducing Human Expertise**

Impact: Agents lose classification skills, creating dependency risk if AI fails

Mitigation:
- Maintain human-in-loop for 20% of tickets (random sampling)
- Quarterly training: agents practice classification without AI assist
- Disaster recovery: Documented fallback to manual process
- Knowledge retention: CoT explanations serve as training material
- Career paths: Upskill agents to AI quality reviewers (higher-value role)"

**Grading (7 pts):**
- Three distinct, relevant risks identified (3 pts)
- Specific mitigation strategies for each (3 pts)
- Business impact assessment included (1 pt)

---

### 4.3 Success Metrics (Sample Answer)

**Exemplary Response:**

"Success will be measured across four dimensions:

**1. Operational Efficiency (Primary)**
- Ticket routing time: Target <30 seconds (baseline: 2-4 hours)
- Classification accuracy: Target 95%+ (measured via weekly random audits)
- Misrouting rate: Target <3% (baseline: 12%)
- Agent time savings: Target 60% reduction in classification effort

**2. Customer Experience**
- NPS impact: Target +15 points improvement (measure via post-resolution survey)
- First response time: Target <30 minutes (baseline: 2-4 hours)
- Resolution time: Target 20% improvement overall
- Customer escalation rate: Target <2% of tickets

**3. Financial Performance**
- Cost reduction: Target $500K annual savings
- ROI: Target >500% in Year 1
- Cost per ticket: Target <$0.05 (vs. $0.33 current state)
- Payback period: Target <6 months

**4. System Reliability**
- Uptime: Target 99.9% availability
- Processing speed: Target <5 seconds per classification
- Error rate: Target <1% system failures
- Scalability: Handle 10,000 tickets/day without performance degradation

**Measurement cadence:**
- Daily: Accuracy, processing time, error rate
- Weekly: Audit sample, cost tracking
- Monthly: NPS, customer satisfaction, ROI calculation
- Quarterly: Strategic review, roadmap adjustment"

**Grading (6 pts):**
- Multiple metric categories (operational, customer, financial) (2 pts)
- Specific, measurable targets with baselines (2 pts)
- Measurement methodology described (1 pt)
- Regular review cadence specified (1 pt)

---

## Overall Grading Summary

**Point Distribution:**
- Part 1 (Scenario Selection): 10 points
- Part 2 (Five Techniques): 40 points (8 points each)
- Part 3 (Comparative Analysis): 30 points
  - Comparison table/viz: 15 points
  - Written analysis: 15 points (3 questions × 5 points)
- Part 4 (Strategic Recommendations): 20 points
  - Roadmap: 7 points
  - Risk assessment: 7 points
  - Success metrics: 6 points

**Total: 100 points (20% of final grade)**

---

## Common Student Mistakes to Watch For

1. **Vague scenarios** without quantitative business context
2. **Identical prompts** with minor wording changes (not demonstrating technique differences)
3. **No actual code** - only written descriptions
4. **Unrealistic ratings** - all techniques rated 5/5 or all rated identically
5. **Generic recommendations** not tailored to chosen scenario
6. **Missing cost analysis** in comparative section
7. **No numerical metrics** in success criteria
8. **Copy-paste answers** from lecture notes without application to scenario

---

*End of Answer Key*
