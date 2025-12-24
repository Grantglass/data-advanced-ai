# MBA 590: Final Project
## AI Transformation Strategic Plan

**Spring 2026**

---

## Project Overview

The final project is a capstone experience where you'll synthesize everything learned in MBA 590 to develop a comprehensive AI transformation strategy for a real or realistic organization. This project simulates the work you might do as a Chief AI Officer, VP of Digital Transformation, or strategic consultant advising C-suite executives on AI adoption.

**Weight:** This project replaces Assignment 4 and counts for **20% of your final grade**.

**Due Date:** Week 15 (final week of class)

**Format:**
1. **Written Strategic Plan** (15-20 pages)
2. **Executive Presentation** (12-15 slides, presented in final class)
3. **Supporting Materials** (Jupyter notebook with technical demonstrations)

---

## Learning Objectives

This project demonstrates your ability to:

1. **Analyze** an organization's AI readiness and identify high-value opportunities
2. **Design** advanced prompting and agentic solutions for business problems
3. **Evaluate** technical approaches using appropriate metrics and frameworks
4. **Build** governance and operating models for responsible AI deployment
5. **Calculate** ROI and financial impact of AI initiatives
6. **Communicate** complex AI strategy to executive audiences
7. **Lead** organizational transformation in the AI era

---

## Part 1: Organization Selection & Analysis (20 points)

### Select Your Organization

Choose **ONE** of the following:

**Option A: Your Current/Former Employer**
- Advantage: Deep knowledge of operations, politics, culture
- Requirement: Anonymize sensitive information
- Must obtain implicit permission or use publicly available information only

**Option B: Public Company You Analyze**
- Advantage: Public financial data, analyst reports available
- Requirement: Must be substantial enough for meaningful AI strategy (>$100M revenue or >500 employees)
- Examples: Regional bank, retail chain, healthcare system, manufacturing company

**Option C: Startup/Growth Company You're Founding**
- Advantage: Can design AI-first from inception
- Requirement: Must be realistic with actual market research
- Include competitive analysis of existing players

**Option D: Industry Vertical Analysis**
- Develop AI strategy for a representative company in an industry vertical
- Requirement: Synthesize insights from 3-5 companies in the same vertical
- Example: "AI Strategy for Mid-Market Law Firms"

### Organizational Analysis

Provide comprehensive analysis of:

#### 1.1 Business Context (5 points)
- Industry, size (revenue, employees, customers), geographic footprint
- Business model and value proposition
- Competitive landscape and positioning
- Current technology maturity and digital capabilities
- Key business metrics and KPIs

#### 1.2 AI Readiness Assessment (8 points)

Evaluate across six dimensions using a 1-5 maturity scale:

| Dimension | Level 1 (Nascent) | Level 3 (Developing) | Level 5 (Advanced) |
|-----------|-------------------|----------------------|--------------------|
| **Data** | Siloed, unstructured | Centralized, some quality issues | Clean, accessible, governed |
| **Infrastructure** | Legacy systems | Cloud migration underway | Modern, scalable cloud |
| **Talent** | No AI/ML staff | Few data scientists | Strong AI/ML team |
| **Culture** | Risk-averse, skeptical | Experimenting with pilots | Data-driven, innovative |
| **Governance** | No AI policies | Basic guidelines | Comprehensive framework |
| **Use Cases** | No AI in production | 1-2 pilot projects | Multiple AI solutions scaled |

**For each dimension:**
- Rate current state (1-5)
- Provide evidence for rating
- Identify specific gaps
- Estimate time/cost to advance one level

#### 1.3 Opportunity Identification (7 points)

Identify 8-10 potential AI use cases across the organization:

| Use Case | Business Function | Impact Potential (H/M/L) | Complexity (H/M/L) | Est. ROI | Priority |
|----------|-------------------|--------------------------|-------------------|----------|----------|
| Example: Customer service chatbot | Customer Support | H | M | 400% Year 1 | 1 |
| Example: Fraud detection | Risk/Compliance | H | H | 250% Year 1 | 2 |

**Prioritize top 3-5 use cases** using a framework like RICE or weighted scoring.

Justify priorities with:
- Business value (revenue, cost savings, strategic importance)
- Technical feasibility (data availability, complexity)
- Resource requirements (time, budget, talent)
- Risk level (operational, reputational, compliance)

---

## Part 2: Technical Solution Design (25 points)

For your **top 2 prioritized use cases**, design detailed technical solutions.

### 2.1 Use Case #1: Detailed Design (12.5 points)

#### Problem Statement (2 points)
- Current state and pain points
- Stakeholders and their needs
- Success criteria (specific, measurable)

#### Solution Architecture (4 points)

Choose appropriate approach:
- **Advanced Prompting** (Few-shot, CoT, RAG, chaining)
- **Agentic System** (single or multi-agent)
- **Hybrid** (combination of techniques)

Provide:
- Architecture diagram
- Data flow
- Key components and their interactions
- Integration points with existing systems

#### Technical Implementation (4 points)

**Demonstrate in Jupyter notebook:**
- Working prototype code (even if simplified/mocked)
- Prompt examples (for prompting solutions)
- Agent design (for agentic solutions)
- Evaluation methodology

**For Prompting Solutions:**
- Show multiple prompting techniques tested
- Comparative analysis
- Prompt optimization process

**For Agentic Solutions:**
- Agent roles and responsibilities
- Tool/function definitions
- Coordination/orchestration logic
- Error handling and fallbacks

#### Evaluation & Metrics (2.5 points)
- How will you measure success?
- Baseline metrics vs. targets
- Evaluation framework (automated + human)
- Quality assurance process

### 2.2 Use Case #2: Detailed Design (12.5 points)
[Same structure as 2.1]

---

## Part 3: Implementation Roadmap (15 points)

### 3.1 Phased Rollout Plan (6 points)

**Phase 1 (Months 1-3): Foundation**
- Scope and deliverables
- Team and resources required
- Infrastructure and tooling needs
- Success criteria and go/no-go decision

**Phase 2 (Months 4-8): Pilot & Validate**
- Pilot scope (users, volume, features)
- Success metrics and validation approach
- Iteration and optimization plan
- Scale decision criteria

**Phase 3 (Months 9-12): Scale & Optimize**
- Full deployment plan
- Change management and training
- Monitoring and continuous improvement
- Lessons learned and next use cases

**Phase 4 (Year 2+): Expand & Innovate**
- Additional use cases from backlog
- Platform and capability building
- Innovation initiatives

### 3.2 Resource Plan (4 points)

#### Team Structure
| Role | FTE | Internal/External | Timeline | Est. Cost |
|------|-----|-------------------|----------|-----------|
| AI Strategy Lead | 1.0 | Internal hire | Month 1 | $150K/year |
| ML Engineers | 2.0 | Contract → hire | Month 2 | $180K/year each |
| Product Manager | 0.5 | Internal | Month 3 | $60K allocated |

**Total headcount:** X FTEs, Y contractors

#### Technology Stack
- LLM providers (API costs)
- Infrastructure (cloud, vector DB)
- Tooling and platforms
- Security and monitoring

#### Budget Summary
| Category | Year 1 | Year 2 | Year 3 | Total |
|----------|--------|--------|--------|-------|
| Personnel | $XXX | $XXX | $XXX | $XXX |
| Technology | $XXX | $XXX | $XXX | $XXX |
| Training & Change Mgmt | $XXX | $XXX | $XXX | $XXX |
| Contingency (15%) | $XXX | $XXX | $XXX | $XXX |
| **Total Investment** | $XXX | $XXX | $XXX | $XXX |

### 3.3 Change Management (5 points)

#### Stakeholder Analysis
- Executive sponsors
- Impacted business units
- IT and data teams
- End users
- External partners

For each stakeholder group:
- Current state and concerns
- Engagement strategy
- Success indicators

#### Communication Plan
- Key messages by audience
- Communication channels and frequency
- Feedback mechanisms

#### Training & Adoption
- Training needs analysis
- Learning programs (by role)
- Adoption measurement
- Resistance mitigation

---

## Part 4: Governance & Risk Management (15 points)

### 4.1 AI Governance Framework (7 points)

#### Policies & Standards
- Acceptable use policy
- Data access and privacy standards
- Model development and approval process
- Monitoring and audit requirements

#### Organizational Structure
- AI governance committee (composition, charter)
- Roles and responsibilities (RACI matrix)
- Decision rights and escalation paths
- Reporting and accountability

#### Ethical Principles
- Fairness and non-discrimination
- Transparency and explainability
- Human oversight and control
- Privacy and data protection

**Operationalize ethics:**
- How will you test for bias?
- What documentation is required?
- When is human-in-the-loop mandatory?
- How do you handle incidents?

### 4.2 Risk Assessment (8 points)

Identify and analyze 5-7 key risks:

| Risk | Likelihood (H/M/L) | Impact (H/M/L) | Mitigation Strategy | Residual Risk | Owner |
|------|-------------------|----------------|---------------------|---------------|-------|
| Model performance degradation | M | H | Automated monitoring, weekly audits, quarterly retraining | M | ML Engineering Lead |
| Data privacy breach | L | H | Encryption, access controls, compliance audits, incident response plan | L | CISO |

**Risk Categories to Consider:**
- **Technical:** Model failures, data quality, system downtime
- **Operational:** Skill gaps, resistance to change, process disruptions
- **Compliance:** Regulatory violations, audit failures
- **Reputational:** Public AI failures, bias incidents, customer trust
- **Financial:** Cost overruns, ROI not achieved
- **Strategic:** Competitive response, technology obsolescence

**For each risk:**
- Description and trigger conditions
- Probability and impact assessment
- Mitigation and contingency plans
- Monitoring and early warning indicators
- Residual risk after mitigation

---

## Part 5: Financial Analysis (15 points)

### 5.1 Cost-Benefit Analysis (7 points)

**Detailed 3-Year Financial Model**

#### Costs
**Year 0 (Implementation):**
- Software/platform licenses
- Infrastructure setup
- Initial development
- Change management
- Training
- Contingency

**Years 1-3 (Ongoing):**
- Personnel (by role)
- API/compute costs
- Licenses and subscriptions
- Maintenance and support
- Continuous improvement

#### Benefits
**Quantified Benefits:**
- Labor cost savings (e.g., reduced headcount, productivity gains)
- Revenue improvements (e.g., increased sales, better retention)
- Cost reductions (e.g., fraud prevention, efficiency gains)
- Risk mitigation value (e.g., compliance, fewer errors)

**Qualitative Benefits:**
- Improved customer satisfaction
- Faster decision-making
- Competitive positioning
- Employee satisfaction
- Innovation capability

### 5.2 ROI Metrics (5 points)

Calculate:

**1. Net Present Value (NPV)**
- Use appropriate discount rate (WACC or 10-12%)
- Show calculations for each year
- Explain assumptions

**2. Payback Period**
- When does cumulative cash flow turn positive?
- Compare to organizational standards

**3. Internal Rate of Return (IRR)**
- What discount rate makes NPV = 0?
- Compare to hurdle rate

**4. ROI Percentage**
- (Total Benefits - Total Costs) / Total Costs
- By year and cumulative

**5. Sensitivity Analysis**
- Best case (+30% benefits, -20% costs)
- Base case (your projections)
- Worst case (-30% benefits, +20% costs)
- What assumptions matter most?

### 5.3 Success Metrics & KPIs (3 points)

Define metrics to track:

**Leading Indicators (predict future success):**
- User adoption rate
- Training completion
- Model accuracy trends
- Engagement metrics

**Lagging Indicators (measure results):**
- Cost savings realized
- Revenue impact
- Customer satisfaction (NPS)
- Process efficiency improvements

**Dashboarding Plan:**
- What gets measured weekly/monthly/quarterly?
- Who sees which metrics?
- What triggers executive review?

---

## Part 6: Executive Presentation (10 points)

Create a **12-15 slide deck** suitable for board/C-suite presentation.

### Required Slides:

**1. Title Slide** (0.5 pts)
- Project title
- Organization
- Your name and date

**2. Executive Summary** (1.5 pts)
- The opportunity (1-2 sentences)
- Recommended investment ($X over Y years)
- Expected return (NPV, payback, ROI%)
- Top 3 strategic initiatives
- Key risks and mitigations

**3. Business Context & Opportunity** (1 pt)
- Current state challenges
- Market/competitive pressures
- Why AI, why now?

**4. AI Readiness Assessment** (1 pt)
- Maturity across 6 dimensions (visual)
- Key gaps and investments needed
- Path to AI-ready organization

**5-6. Strategic Initiatives (2 slides)** (2 pts)
- Top 3-5 use cases with business impact
- Prioritization rationale
- Expected outcomes for each

**7-8. Technical Approach (2 slides)** (1 pt)
- High-level architecture for top initiatives
- Prompting vs. agentic approaches
- Integration with existing systems
- (Keep technical detail appropriate for executive audience)

**9. Implementation Roadmap** (1 pt)
- Phased plan over 12-18 months
- Key milestones and decision points
- Resource requirements by phase

**10. Financial Analysis** (1.5 pts)
- 3-year cost-benefit summary
- NPV, payback, ROI
- Sensitivity analysis
- Comparison to do-nothing scenario

**11. Governance & Risk** (1 pt)
- Governance structure
- Top 3-5 risks and mitigations
- Ethical AI principles

**12. Success Metrics** (0.5 pts)
- How we'll measure success
- Leading and lagging indicators
- Reporting cadence

**13. Recommendations & Next Steps** (0.5 pts)
- Clear ask (approval for $X investment)
- Immediate next steps
- Timeline for decision

**14. Appendix** (0 pts - optional)
- Additional details for Q&A
- Technical deep dives
- Detailed financials

### Presentation Delivery (Graded in Class)

**In-class presentation: 10 minutes + 5 minutes Q&A**

Grading criteria:
- Clarity and professionalism (2 pts)
- Business storytelling (2 pts)
- Handling of Q&A (1 pt)

---

## Deliverables Summary

### 1. Written Strategic Plan (15-20 pages)
**Format:** PDF, professional formatting
**Due:** Week 15, before class

**Suggested structure:**
1. Executive Summary (1 page)
2. Organization Analysis (3-4 pages)
3. Technical Solution Design (4-5 pages)
4. Implementation Roadmap (2-3 pages)
5. Governance & Risk (2-3 pages)
6. Financial Analysis (2-3 pages)
7. Conclusion & Recommendations (1 page)
8. Appendices (technical details, financial models)

### 2. Executive Presentation (12-15 slides)
**Format:** PowerPoint or Google Slides
**Due:** Week 15, before class
**Presented:** In-class during final session

### 3. Supporting Technical Materials
**Format:** Jupyter notebook (.ipynb)
**Due:** Week 15, with written plan

**Should include:**
- Working code demonstrations for top 2 use cases
- Prompt examples (if prompting-based solutions)
- Agent architecture (if agentic solutions)
- Evaluation framework and sample results
- Financial model calculations (can be Python or Excel embedded)

---

## Grading Rubric

| Component | Points | Criteria |
|-----------|--------|----------|
| **Part 1: Organization Analysis** | 20 | Business context (5), AI readiness (8), opportunities (7) |
| **Part 2: Technical Design** | 25 | Use case 1 (12.5), Use case 2 (12.5) |
| **Part 3: Implementation Roadmap** | 15 | Phased plan (6), resources (4), change mgmt (5) |
| **Part 4: Governance & Risk** | 15 | Governance framework (7), risk assessment (8) |
| **Part 5: Financial Analysis** | 15 | Cost-benefit (7), ROI metrics (5), KPIs (3) |
| **Part 6: Executive Presentation** | 10 | Slide content (7.5), delivery (2.5) |
| **Total** | 100 | |

### Detailed Grading Criteria

#### Exemplary (90-100%): A/A-
- Comprehensive, sophisticated analysis demonstrating mastery
- Innovative technical solutions with strong justification
- Realistic, detailed implementation plan with contingencies
- Rigorous financial analysis with sensitivity testing
- Executive-ready presentation, publication-quality writing
- Demonstrates synthesis across all course concepts

#### Proficient (80-89%): B+/B
- Thorough analysis covering all required elements
- Sound technical solutions appropriate for use cases
- Solid implementation plan with most details covered
- Competent financial analysis with reasonable assumptions
- Good presentation and clear writing
- Shows understanding of course concepts

#### Developing (70-79%): B-
- Basic analysis meeting minimum requirements
- Technical solutions present but lacking depth
- Implementation plan missing key details
- Financial analysis incomplete or unrealistic assumptions
- Presentation adequate but not polished
- Limited synthesis of course concepts

#### Unsatisfactory (<70%): C+ or below
- Incomplete analysis with significant gaps
- Weak or inappropriate technical solutions
- Vague implementation plan
- Missing or flawed financial analysis
- Poor presentation quality
- Does not demonstrate course learning objectives

---

## Submission Instructions

### What to Submit:

**Via Course Learning Management System:**
1. Written Strategic Plan (PDF)
2. Executive Presentation (PowerPoint/Google Slides)
3. Jupyter Notebook (`.ipynb` file)
4. Any supporting files (Excel financial models, architecture diagrams, etc.)

**File Naming Convention:**
- `LastName_FirstName_Strategic_Plan.pdf`
- `LastName_FirstName_Presentation.pptx`
- `LastName_FirstName_Technical_Demo.ipynb`

**Submission Deadline:** Week 15, [Date/Time]

**Late Policy:** 10% penalty per day up to 3 days. After 3 days, project will not be accepted without documented extenuating circumstances.

---

## Tips for Success

### Start Early
- **Week 10:** Select organization, begin readiness assessment
- **Week 11:** Identify use cases, prioritize top 2
- **Week 12:** Design technical solutions, begin Jupyter notebook
- **Week 13:** Financial analysis, governance framework
- **Week 14:** Write strategic plan, create presentation
- **Week 15:** Final polish, practice presentation

### Leverage Course Materials
- Review all 15 weekly notebooks for technical approaches
- Reference assignment solutions for formatting and depth
- Use prompting techniques from Weeks 1-5 for prompting solutions
- Apply agentic frameworks from Weeks 6-8 for agent solutions
- Incorporate governance from Weeks 11-12
- Use ROI frameworks from Week 14

### Seek Feedback
- **Week 12:** Optional project pitch (5 minutes, office hours) for early feedback
- **Week 13:** Draft financial analysis review (optional)
- **Week 14:** Practice presentation with peers

### Common Pitfalls to Avoid
1. Choosing an organization that's too small or too large for meaningful analysis
2. Selecting overly ambitious use cases that can't be demonstrated
3. Ignoring organizational change management (technical solution alone is insufficient)
4. Unrealistic ROI projections without proper justification
5. Too much technical detail in executive presentation
6. Failing to demonstrate working technical solutions in Jupyter notebook
7. Missing the "so what?" - not connecting AI initiatives to business strategy

---

## Example Project Outlines

### Example 1: Regional Healthcare System

**Organization:** 5-hospital regional health system, $2B revenue, 8,000 employees

**Top Use Cases:**
1. Clinical documentation assistant (RAG-based)
2. Patient scheduling optimization (multi-agent)
3. Prior authorization automation (prompt chaining)

**Key Insights:**
- High regulatory complexity (HIPAA, FDA)
- Strong ROI from reducing physician documentation burden (2 hours/day → 30 min)
- Change management critical due to physician resistance

**Investment:** $4.5M over 3 years
**Expected Return:** $22M NPV (physician time savings, reduced denials)
**Payback:** 9 months

---

### Example 2: Mid-Market Manufacturing Company

**Organization:** Industrial equipment manufacturer, $500M revenue, 1,200 employees, 3 factories

**Top Use Cases:**
1. Predictive maintenance for equipment (agentic monitoring)
2. RFQ/quote generation (advanced prompting + RAG)
3. Supply chain optimization (multi-agent coordination)

**Key Insights:**
- Limited AI maturity (Level 2/5), needs foundational investment
- High value from reducing unplanned downtime (current cost: $8M/year)
- Data quality challenges require Phase 1 focus

**Investment:** $2.8M over 3 years
**Expected Return:** $15M NPV (downtime reduction, faster quoting)
**Payback:** 11 months

---

## Frequently Asked Questions

**Q: Can I work on this project in a team?**
A: No, this is an individual project. However, you may interview colleagues or domain experts for context.

**Q: What if I don't have API access to an LLM?**
A: You can use mock outputs or demonstrate prompts without actual API calls. The emphasis is on strategy and design, not production implementation.

**Q: How technical should the Jupyter notebook be?**
A: Show enough to prove you understand the implementation. Simplified/mocked code is acceptable. Focus on demonstrating the concepts (prompt engineering techniques, agent design) rather than production-ready code.

**Q: Can I use AI tools (ChatGPT, Claude) to help with this project?**
A: Yes, but you must:
- Disclose AI assistance in your submission
- Demonstrate genuine understanding (you'll present and answer questions)
- Provide original analysis and strategic thinking (AI can help with formatting, calculations, brainstorming—not replace your thinking)

**Q: What if my current employer won't allow me to share information?**
A: Either (a) anonymize/generalize the information, (b) use only publicly available information, or (c) choose a different organization.

**Q: How realistic do the financials need to be?**
A: Use realistic assumptions based on industry benchmarks, case studies, or reasonable extrapolation. If you make assumptions, state them clearly and justify them.

**Q: Can I focus on just one major use case instead of two?**
A: Only with instructor approval, if the single use case is sufficiently complex (e.g., a multi-agent system with 4+ agents). Otherwise, two use cases are required.

---

## Resources

### Financial Benchmarks
- **LLM API Costs:** $0.01-0.08 per 1K tokens (varies by model)
- **ML Engineer Salary:** $150-200K
- **Data Scientist Salary:** $130-180K
- **AI Product Manager:** $140-190K
- **Typical AI Project:** $500K-5M depending on scope
- **Industry ROI Benchmarks:** Review Week 14 materials

### Case Studies
- Klarna: Customer service automation
- Morgan Stanley: Knowledge management
- Capital One: AI operating model transformation
- Healthcare systems: Clinical documentation
- Manufacturing: Predictive maintenance

### Templates Provided
- Financial model spreadsheet
- Governance framework template
- Risk register template
- Presentation template (optional)

---

## Academic Integrity

- All analysis must be your own work
- Properly cite all sources (academic, industry reports, company data)
- If using AI assistance, disclose it and ensure you understand all content
- Plagiarism or copying from other students will result in a zero and potential academic conduct referral

---

## Grading Timeline

- **Week 15:** Projects submitted and presentations delivered
- **Week 16 (Finals Period):** Grading completed, final grades posted

---

**This project is your opportunity to synthesize everything you've learned and create a portfolio piece demonstrating your AI strategy capabilities. Approach it as if you're presenting to your CEO or a client. Good luck!**

---

*Version 1.0*
*Last Updated: [Date]*
