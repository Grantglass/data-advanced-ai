# Frequently Asked Questions (FAQ)

## General Questions

### Q: Do I need programming experience to take this course?
**A:** Basic Python knowledge is helpful but not required. The notebooks include explanations and examples to help you learn.

### Q: Do I need to pay for LLM API access?
**A:** No. Most examples work with mock data. API access is optional for live experimentation.

### Q: Can I run these notebooks in Google Colab?
**A:** Yes! Upload the notebook to Colab and install required packages using `!pip install -r requirements.txt`

### Q: How long does each week's content take?
**A:** Plan for 3-4 hours per week including reading, exercises, and assignments.

## Technical Questions

### Q: I'm getting a "Module not found" error
**A:** Ensure you've installed all requirements:
```bash
pip install -r requirements.txt
```

### Q: The notebooks won't run
**A:** Check that you:
1. Activated your virtual environment
2. Installed Jupyter: `pip install jupyter`
3. Are running Python 3.8 or higher

### Q: How do I get an OpenAI API key?
**A:** Visit https://platform.openai.com/, create an account, and generate an API key under "API Keys"

### Q: My API calls are expensive. How do I control costs?
**A:**
- Use `gpt-3.5-turbo` for practice (much cheaper)
- Set usage limits in your API dashboard
- Use the `count_tokens()` utility to estimate costs
- Work with mock responses for development

### Q: Can I use Claude instead of GPT?
**A:** Yes! The course covers both. Get an Anthropic API key at https://console.anthropic.com/

## Assignment Questions

### Q: When are assignments due?
**A:**
- Assignment 1: End of Week 8
- Assignment 2: End of Week 10
- Assignment 3: End of Week 12
- Assignment 4: End of Week 15

### Q: Can I work in groups?
**A:** Check your syllabus. Typically, assignments are individual but discussions are encouraged.

### Q: What format should I submit?
**A:** Submit the completed `.ipynb` notebook file through the course platform.

### Q: Can I use AI tools to help with assignments?
**A:** Check with your instructor. Generally, using LLMs to help understand concepts is okay, but submitting AI-generated work as your own is not.

## Content Questions

### Q: The notebooks reference papers behind paywalls. What should I do?
**A:** Check if your university library provides access, or email the instructor for alternatives.

### Q: Can I skip weeks if I'm already familiar with the topic?
**A:** We recommend completing all content as each week builds on previous concepts.

### Q: Are there video lectures?
**A:** Check your course platform. These notebooks are designed for self-paced learning.

### Q: How do I cite this course material?
**A:**
```
MBA 590: Advanced AI Strategy Course Materials (2026).
NC State University, Poole College of Management.
```

## Common Issues

### Q: Jupyter kernel keeps dying
**A:** Try:
1. Restart the kernel
2. Clear all outputs and restart
3. Check memory usage (close other applications)
4. Reduce batch sizes in code

### Q: Plots aren't displaying
**A:** Add this to the top of your notebook:
```python
%matplotlib inline
```

### Q: Git says my files are too large
**A:** Large datasets should not be committed. Check `.gitignore` and use Git LFS if needed.

### Q: How do I update to the latest course materials?
**A:**
```bash
git pull origin main
```

## Getting Help

### Still stuck?

1. **Check the documentation**: README, TROUBLESHOOTING.md
2. **Search existing issues**: Someone may have had the same problem
3. **Ask in the forum**: Course discussion board
4. **Office hours**: Attend instructor office hours
5. **Open an issue**: For technical problems with the repository

---

**Last Updated**: November 2025
