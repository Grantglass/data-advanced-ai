# MBA 590: Advanced AI Strategy - Course Notebooks

## Advanced AI Strategy: Prompting and Agentic Frameworks - Spring 2026

This repository contains comprehensive Python Jupyter notebooks for the MBA 590 course, designed to provide hands-on learning experiences for mastering advanced AI interaction paradigms, prompt engineering techniques, and strategic implementation of agentic systems.

---

## ⭐ What's New in Version 1.0

This repository now includes comprehensive infrastructure and support materials:

- 📝 **4 Assignment Templates** - Complete starter files for all major assignments
- 🗂️ **Sample Datasets** - Real-world data for hands-on practice
- 🎯 **Prompt Templates Library** - Reusable templates organized by use case
- 🛠️ **Python Utilities** - Helper functions for LLMs, data analysis, and evaluation
- 🐳 **Docker Support** - Reproducible environment with one command
- 🧪 **Automated Testing** - Verify all notebooks execute correctly
- 📚 **Comprehensive Documentation** - Setup guides, FAQ, troubleshooting
- 🔄 **CI/CD Pipeline** - GitHub Actions for quality assurance
- 📄 **Export Scripts** - Convert notebooks to PDF, HTML, slides

---

## 📂 Repository Structure

```
data-advanced-ai/
├── notebooks/          # 15 weekly Jupyter notebooks
├── assignments/        # 4 assignment templates
├── data/
│   ├── samples/        # Sample datasets (CSV, JSON)
│   └── examples/       # Example data and prompts
├── prompt_templates/   # Reusable prompt library
├── utils/              # Python utilities module
│   ├── llm_helpers.py
│   ├── data_helpers.py
│   ├── prompt_helpers.py
│   └── evaluation_helpers.py
├── scripts/            # Automation scripts
│   ├── test_notebooks.py
│   └── export_notebooks.py
├── .github/workflows/  # CI/CD configuration
├── Dockerfile          # Docker container definition
├── docker-compose.yml  # Docker orchestration
├── requirements.txt    # Python dependencies
├── environment.yml     # Conda environment
├── .env.example        # API key template
└── docs/               # Documentation files
```

---

## Course Overview

This advanced course equips leaders and strategists with the knowledge and skills to effectively leverage sophisticated language models and emerging agentic systems. The curriculum provides an in-depth exploration of:

- **Prompt Engineering**: From fundamentals to advanced techniques (Chain-of-Thought, RAG, Self-Refine)
- **LLM Evaluation**: Rigorous frameworks for assessing quality, safety, and business suitability
- **Agentic Systems**: Architecture, capabilities, and strategic applications
- **Implementation Strategy**: Tech-ready operating models, governance, and ethical frameworks
- **Strategic Leadership**: Technology strategy formulation, ROI measurement, and future trends

---

## 📚 Course Structure

The course consists of 15 weeks, each with a dedicated Jupyter notebook containing:
- Learning objectives
- Academic readings references
- Conceptual explanations
- Practical Python code examples
- Hands-on exercises
- Discussion questions
- Key takeaways

---

## 📓 Weekly Notebooks

### Part I: Prompt Engineering Mastery (Weeks 1-4)

#### Week 1: Foundations of Effective Prompt Engineering
**File**: `week01_foundations_prompt_engineering.ipynb`

**Topics**:
- Core principles of prompt engineering
- LLM input/output processing
- Context, specificity, and clarity
- Basic prompt types: zero-shot, role-playing, simple instruction

**Key Skills**: Understanding fundamental prompting principles and comparing different approach styles

---

#### Week 2: Advanced Prompting I - Few-Shot, Chain-of-Thought & Self-Ask
**File**: `week02_advanced_prompting_1.ipynb`

**Topics**:
- Few-shot learning for improved context
- Chain-of-Thought (CoT) prompting for complex reasoning
- Self-Ask for problem decomposition
- Combining techniques for optimal results

**Key Skills**: Implementing sophisticated prompting methods for complex business tasks

---

#### Week 3: Advanced Prompting II - Problem Decomposition & Self-Correction
**File**: `week03_advanced_prompting_2.ipynb`

**Topics**:
- Least-to-Most (LtM) prompting
- Plan-and-Solve approaches
- Self-Refine for iterative improvement
- Chain-of-Verification (CoVe) for accuracy

**Key Skills**: Breaking down complex tasks and enabling LLM self-correction

---

#### Week 4: Advanced Prompting III - RAG & Prompt Chaining
**File**: `week04_rag_prompt_chaining.ipynb`

**Topics**:
- Retrieval-Augmented Generation (RAG) concepts
- Grounding LLMs in specific knowledge
- Prompt chaining for multi-step workflows
- Building complex LLM applications

**Key Skills**: Implementing RAG and orchestrating multi-step LLM workflows

---

### Part II: LLM Evaluation (Week 5)

#### Week 5: Evaluating LLM Outputs - Metrics and Frameworks
**File**: `week05_evaluating_llm_outputs.ipynb`

**Topics**:
- Evaluation metrics (BLEU, ROUGE, perplexity, F1-score)
- Quality assessment frameworks
- Bias detection and safety evaluation
- Business suitability criteria

**Key Skills**: Critically evaluating LLM outputs using established metrics and frameworks

---

### Part III: Agentic Systems (Weeks 6-8)

#### Week 6: Introduction to Agentic Frameworks
**File**: `week06_intro_agentic_frameworks.ipynb`

**Topics**:
- Defining agentic systems: autonomy, planning, reasoning
- Core concepts: perception, action loops, memory
- ReAct framework and basic architectures
- Tool use and decision-making

**Key Skills**: Understanding agentic system architecture and capabilities

---

#### Week 7: Multi-Agent Systems & Collaboration
**File**: `week07_multi_agent_systems.ipynb`

**Topics**:
- Multi-Agent Systems (MAS) concepts
- Communication protocols and patterns
- Coordination and collaboration strategies
- Applications in complex problem-solving

**Key Skills**: Designing multi-agent systems for business applications

---

#### Week 8: Agentic Frameworks - Business Applications & Case Studies
**File**: `week08_agentic_business_applications.ipynb`

**Topics**:
- Real-world applications (customer service, data analysis, supply chain)
- Case studies and implementation examples
- Challenges and success factors
- Strategic opportunities assessment

**Key Skills**: Evaluating business applications and implementation challenges

**Assignment 1 Due**: Advanced Prompt Engineering Analysis

---

### Part IV: Tech-Ready Organizations (Weeks 9-10)

#### Week 9: Building Tech-Ready Operating Models I - Structure & Governance
**File**: `week09_tech_ready_operating_models_1.ipynb`

**Topics**:
- Organizational structures (centralized, decentralized, CoE)
- Technology governance frameworks
- Roles and responsibilities
- Decision rights and accountability

**Key Skills**: Designing organizational structures for advanced technology adoption

---

#### Week 10: Building Tech-Ready Operating Models II - Talent & Culture
**File**: `week10_tech_ready_operating_models_2.ipynb`

**Topics**:
- Talent needs and acquisition strategies
- Training and development programs
- Building a culture of experimentation
- Change management and adoption strategies

**Key Skills**: Developing talent strategies and fostering adaptive cultures

**Assignment 2 Due**: Agentic Framework Application Proposal

---

### Part V: Governance & Ethics (Weeks 11-12)

#### Week 11: Technology Governance & Ethics I - Frameworks & Principles
**File**: `week11_governance_ethics_1.ipynb`

**Topics**:
- Ethical risks (bias, fairness, transparency, accountability)
- Responsible AI frameworks (NIST, OECD, IEEE)
- Core principles for ethical deployment
- Policy translation

**Key Skills**: Applying ethical frameworks to technology governance

---

#### Week 12: Technology Governance & Ethics II - Regulation & Implementation
**File**: `week12_governance_ethics_2.ipynb`

**Topics**:
- Regulatory landscape (EU AI Act, GDPR)
- Bias audits and testing
- Transparency reporting and model cards
- Human oversight mechanisms

**Key Skills**: Implementing governance controls and regulatory compliance

**Assignment 3 Due**: Tech-Ready Operating Model Design

---

### Part VI: Strategy & Future (Weeks 13-15)

#### Week 13: Developing Technology Strategy & Portfolio Management
**File**: `week13_technology_strategy.ipynb`

**Topics**:
- Technology strategy frameworks
- Project prioritization methodologies
- Portfolio management and balance
- Roadmap development

**Key Skills**: Formulating comprehensive technology strategies

---

#### Week 14: Measuring ROI for Technology Initiatives
**File**: `week14_measuring_roi.ipynb`

**Topics**:
- ROI calculation fundamentals (NPV, IRR, Payback Period)
- Total Cost of Ownership (TCO) analysis
- Tangible and intangible benefits
- Balanced Scorecard for technology

**Key Skills**: Calculating and assessing technology initiative ROI

---

#### Week 15: Future Technology Trends & Strategic Leadership
**File**: `week15_future_trends.ipynb`

**Topics**:
- Emerging technology trends (multimodal AI, AGI, quantum)
- Future scenarios and strategic planning
- Leadership capabilities for the AI era
- Course synthesis and personal action planning

**Key Skills**: Assessing future trends and developing strategic leadership capabilities

**Assignment 4 Due**: AI Strategic Implementation Plan

---

##  🎯 Prompt Templates Library

Access pre-built prompts for common business tasks:

```python
from prompt_templates.business_templates import swot_analysis

# Fill in a template
prompt = swot_analysis.fill(
    context="Entering the AI automation market",
    subject="Our AI Platform",
    market="Mid-market B2B SaaS"
)
```

**Available Templates**:
- Business Analysis (SWOT, competitive analysis, market opportunities)
- Customer Service (complaint handling, product inquiries)
- Content Creation (product descriptions, marketing copy)
- Data Analysis (trend analysis, anomaly detection)
- Technical (code review, API documentation)

See `prompt_templates/README.md` for full documentation.

---

## 🛠️ Python Utilities

Helper functions for common tasks:

```python
from utils import count_tokens, estimate_cost, create_mock_llm_response
from utils import load_sample_data, create_comparison_chart
from utils import validate_prompt, measure_prompt_quality

# Count tokens and estimate costs
tokens = count_tokens("Your prompt here")
cost = estimate_cost(tokens, expected_output=500, model="gpt-4")

# Load sample data
df = load_sample_data("customer_service_tickets.csv")

# Validate prompts
quality = validate_prompt("Your prompt")
print(f"Quality score: {quality['score']}/100")
```

See inline documentation for all available functions.

---

## 📝 Assignments

Four comprehensive assignment templates aligned with course milestones:

1. **Assignment 1** (Week 8): Advanced Prompt Engineering Analysis - 20%
2. **Assignment 2** (Week 10): Agentic Framework Application Proposal - 20%
3. **Assignment 3** (Week 12): Tech-Ready Operating Model Design - 20%
4. **Assignment 4** (Week 15): AI Strategic Implementation Plan - 30%

Each includes:
- Detailed instructions
- Code scaffolding
- Evaluation rubrics
- Submission checklists

---

## 🚀 Getting Started

### Choose Your Deployment Option

We support **three deployment options** to fit your needs:

| Option | Best For | Setup Time | Cost | Privacy |
|--------|----------|------------|------|---------|
| **🏢 Azure Cloud** | Enterprise, compliance needs | 15-30 min | $$ | High (VNet) |
| **🖥️ Local LLM** | Privacy, offline, no API costs | 10-20 min | Free | Complete |
| **☁️ OpenAI Direct** | Quick start, best quality | 5 min | $ | Standard |

---

### Option 1: Azure OpenAI (Enterprise Cloud) ⭐ Recommended for Organizations

Enterprise-grade deployment with security, compliance, and VNet integration.

```bash
# See complete guide
cat DEPLOY_AZURE.md

# Quick deploy with Azure CLI
az group create --name mba590-rg --location eastus
az deployment group create \
  --resource-group mba590-rg \
  --template-file azure/deploy-azure-openai.bicep

# Copy credentials to .env
cp .env.example .env
# Set LLM_PROVIDER=azure and add your Azure credentials
```

**Benefits**:
- ✅ SOC 2, HIPAA, ISO compliance
- ✅ Private network (VNet) integration
- ✅ Data residency control
- ✅ Enterprise SLA (99.9%)
- ✅ Cost tracking and quotas

📘 **[Full Azure Setup Guide →](DEPLOY_AZURE.md)**

---

### Option 2: Local LLM with Ollama (On-Premises) ⭐ Recommended for Privacy

Run completely locally with no cloud API required.

```bash
# See complete guide
cat DEPLOY_LOCAL.md

# Quick start with Docker
docker-compose -f docker-compose.local-llm.yml up

# Or install Ollama directly
curl -fsSL https://ollama.ai/install.sh | sh
ollama pull llama2:7b

# Start Jupyter
cp .env.example .env
# Set LLM_PROVIDER=ollama
docker-compose up
```

**Benefits**:
- ✅ Complete data privacy (nothing leaves your machine)
- ✅ No API costs (free to use)
- ✅ Works offline
- ✅ Full model control
- ✅ Open-source models

📘 **[Full Local Setup Guide →](DEPLOY_LOCAL.md)**

---

### Option 3: OpenAI Direct (Quick Start)

Fastest way to get started:

```bash
# Clone the repository
git clone https://github.com/yourusername/data-advanced-ai.git
cd data-advanced-ai

# Copy environment template
cp .env.example .env
# Add your OpenAI API key to .env
# LLM_PROVIDER=openai
# OPENAI_API_KEY=your_key_here

# Start with Docker
docker-compose up

# Access Jupyter at http://localhost:8888
```

---

### Manual Installation (All Options)

#### Prerequisites

- Python 3.8 or higher
- Jupyter Notebook or JupyterLab
- Basic understanding of Python programming
- Familiarity with business strategy concepts

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/data-advanced-ai.git
   cd data-advanced-ai
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install required packages**:
   ```bash
   pip install jupyter pandas numpy matplotlib seaborn plotly scikit-learn
   ```

4. **Optional - Install LLM API libraries** (for running live examples):
   ```bash
   pip install openai anthropic
   ```

### Running the Notebooks

1. **Launch Jupyter**:
   ```bash
   jupyter notebook
   ```
   or
   ```bash
   jupyter lab
   ```

2. **Navigate to the notebooks folder** and open the desired week's notebook

3. **Follow the instructions** in each notebook, running cells sequentially

---

## 📋 Course Assignments

### Major Assignments (80% of grade):

1. **Advanced Prompt Engineering Analysis** (20%) - Due Week 8
   - Apply advanced prompting techniques to a real business scenario
   - Evaluate effectiveness using multiple approaches

2. **Agentic Framework Application Proposal** (20%) - Due Week 10
   - Design an agentic system for a specific business use case
   - Include architecture, capabilities, and implementation plan

3. **Tech-Ready Operating Model Design** (20%) - Due Week 12
   - Develop organizational structure and governance for AI adoption
   - Address talent, culture, and change management

4. **AI Strategic Implementation Plan** (30%) - Due Week 15
   - Comprehensive technology strategy document
   - Include prioritization, roadmap, ROI analysis, and governance

### Weekly Application & Discussion (10% of grade):
- Active participation in discussion forums
- Completion of hands-on exercises in notebooks

---

## 🎯 Learning Outcomes

Upon successful completion of this course, you will be able to:

1. **Master Advanced Prompt Engineering**: Apply sophisticated prompting methods for complex tasks
2. **Critically Evaluate LLM Outputs**: Use metrics and frameworks to assess quality and suitability
3. **Analyze Agentic Systems**: Understand architectures and capabilities
4. **Evaluate Strategic Applications**: Identify opportunities and assess risks
5. **Design Tech-Ready Operating Models**: Create organizational structures and cultural attributes
6. **Implement Governance**: Develop ethical and responsible technology frameworks
7. **Formulate Technology Strategies**: Create comprehensive strategies aligned with business goals
8. **Measure ROI**: Apply methodologies to assess technology initiative value
9. **Assess Future Trends**: Analyze emerging technologies and strategic implications

---

## 💡 Best Practices for Using These Notebooks

1. **Sequential Learning**: Work through notebooks in order, as concepts build on previous weeks
2. **Hands-On Practice**: Complete all "YOUR TURN" exercises to reinforce learning
3. **Experimentation**: Modify code examples to explore different scenarios
4. **Discussion Participation**: Engage with discussion questions and share insights
5. **Real-World Application**: Apply concepts to your own business context
6. **Resource Exploration**: Review additional resources provided in each notebook

---

## 🔧 Technical Notes

### Code Examples

- Most code examples are **self-contained** and can run without external APIs
- Some examples demonstrate **API integration** (OpenAI, Anthropic) but include placeholder code
- Visualization libraries used: **matplotlib**, **seaborn**, **plotly**
- Data analysis with: **pandas**, **numpy**, **scikit-learn**

### API Keys

If you want to run live LLM examples:

1. Obtain API keys from:
   - OpenAI: https://platform.openai.com/
   - Anthropic: https://console.anthropic.com/

2. Set environment variables:
   ```bash
   export OPENAI_API_KEY='your-key-here'
   export ANTHROPIC_API_KEY='your-key-here'
   ```

3. Or create a `.env` file in the project root (included in .gitignore)

---

## 📖 Academic Readings

Each notebook references academic papers and industry reports. Key papers include:

- **Wei et al. (2022)**: Chain-of-Thought Prompting
- **Lewis et al. (2020)**: Retrieval-Augmented Generation
- **Xi et al. (2023)**: Large Language Model Based Agents Survey
- **Madaan et al. (2023)**: Self-Refine
- **Zhou et al. (2022)**: Least-to-Most Prompting
- **Chang et al. (2023)**: Evaluation of Large Language Models
- **NIST (2023)**: AI Risk Management Framework

Full references are provided within each notebook.

---

## 🧪 Testing & Quality Assurance

### Run Automated Tests

Verify all notebooks execute correctly:

```bash
# Test all notebooks
python scripts/test_notebooks.py

# Test specific directory
python scripts/test_notebooks.py --dir notebooks

# With custom timeout
python scripts/test_notebooks.py --timeout 300
```

### Export Notebooks

Convert notebooks to various formats:

```bash
# Export to HTML
python scripts/export_notebooks.py --formats html

# Export to multiple formats
python scripts/export_notebooks.py --formats html pdf slides

# Custom output directory
python scripts/export_notebooks.py --output my_exports
```

### Code Quality

```bash
# Format code
black utils/ prompt_templates/

# Lint code
pylint utils/ prompt_templates/

# Type checking
mypy utils/
```

---

## 📚 Documentation

- **[README.md](README.md)** - This file, repository overview
- **[CONTRIBUTING.md](CONTRIBUTING.md)** - How to contribute
- **[FAQ.md](FAQ.md)** - Frequently asked questions
- **[TROUBLESHOOTING.md](TROUBLESHOOTING.md)** - Common issues and solutions
- **[CHANGELOG.md](CHANGELOG.md)** - Version history and updates
- **[prompt_templates/README.md](prompt_templates/README.md)** - Prompt library guide

---

## 🤝 Contributing

We welcome contributions from students, instructors, and the community!

**Ways to Contribute**:
- Report bugs or errors
- Suggest improvements
- Add new examples
- Update documentation
- Share interesting use cases

See **[CONTRIBUTING.md](CONTRIBUTING.md)** for detailed guidelines.

**Quick contribution workflow**:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

---

## 📄 License

This course material is provided for educational purposes. Please refer to your institution's academic policies regarding use and distribution of course materials.

---

## 👥 Course Information

**Course**: MBA 590 - Advanced AI Strategy: Prompting and Agentic Frameworks
**Institution**: NC State University, Poole College of Management
**Term**: Spring 2026
**Credit Hours**: 3
**Format**: Online with synchronous office hours

**Instructor Information**: See course syllabus on WolfWare

---

## 📞 Support

- **Technical Issues**: Contact OIT Help Desk at 919-515-HELP or help@ncsu.edu
- **Course Content Questions**: Use the discussion forum or attend office hours
- **Notebook Issues**: Open an issue in this repository

---

## 🎓 Course Website

Official course materials and submissions:
https://wolfware.ncsu.edu/courses/details/?sis_id=SIS:2026:1:1:MBA:590:639

---

## 📅 Quick Reference

| Week | Topic | Notebook File | Assignment Due |
|------|-------|---------------|----------------|
| 1 | Prompt Engineering Foundations | week01_foundations_prompt_engineering.ipynb | - |
| 2 | Advanced Prompting I | week02_advanced_prompting_1.ipynb | - |
| 3 | Advanced Prompting II | week03_advanced_prompting_2.ipynb | - |
| 4 | RAG & Prompt Chaining | week04_rag_prompt_chaining.ipynb | - |
| 5 | Evaluating LLM Outputs | week05_evaluating_llm_outputs.ipynb | - |
| 6 | Intro to Agentic Frameworks | week06_intro_agentic_frameworks.ipynb | - |
| 7 | Multi-Agent Systems | week07_multi_agent_systems.ipynb | - |
| 8 | Agentic Business Applications | week08_agentic_business_applications.ipynb | Assignment 1 |
| 9 | Operating Models I | week09_tech_ready_operating_models_1.ipynb | - |
| 10 | Operating Models II | week10_tech_ready_operating_models_2.ipynb | Assignment 2 |
| 11 | Governance & Ethics I | week11_governance_ethics_1.ipynb | - |
| 12 | Governance & Ethics II | week12_governance_ethics_2.ipynb | Assignment 3 |
| 13 | Technology Strategy | week13_technology_strategy.ipynb | - |
| 14 | Measuring ROI | week14_measuring_roi.ipynb | - |
| 15 | Future Trends & Leadership | week15_future_trends.ipynb | Assignment 4 |

---

**Last Updated**: November 2025
**Version**: 1.0

Happy Learning! 🚀
