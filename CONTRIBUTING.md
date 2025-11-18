# Contributing to MBA 590 - Advanced AI Strategy

Thank you for your interest in contributing to this course repository!

## Ways to Contribute

### For Students

1. **Report Issues**
   - Found an error in a notebook? Open an issue
   - Include the notebook name and cell number
   - Describe what's wrong and what you expected

2. **Suggest Improvements**
   - Have ideas for better examples?
   - Know of relevant recent papers or resources?
   - Open an issue with your suggestion

3. **Share Solutions**
   - Completed an interesting exercise variation?
   - Found a creative application?
   - Share in the discussion forum

### For Instructors/Contributors

1. **Code Contributions**
   - Fork the repository
   - Create a feature branch
   - Make your changes
   - Submit a pull request

2. **Content Improvements**
   - Add new examples
   - Update outdated references
   - Improve explanations
   - Add visualizations

## Contribution Guidelines

### Code Style

- **Python**: Follow PEP 8
- **Notebooks**: Clear markdown explanations
- **Comments**: Explain the "why", not just the "what"

### Notebook Standards

- Start with clear learning objectives
- Include practical examples
- Provide "YOUR TURN" exercises
- End with key takeaways
- Test that all cells run successfully

### Commit Messages

- Use present tense ("Add feature" not "Added feature")
- Be descriptive but concise
- Reference issues when applicable

Example:
```
Add advanced RAG example to Week 4 notebook

- Implements semantic chunking
- Adds visualization of embeddings
- Includes performance comparison

Closes #42
```

## Development Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/data-advanced-ai.git
   cd data-advanced-ai
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run tests**
   ```bash
   python scripts/test_notebooks.py
   ```

## Pull Request Process

1. **Before Starting**
   - Check existing issues and PRs
   - Open an issue to discuss major changes
   - Ensure your idea aligns with course objectives

2. **Making Changes**
   - Create a feature branch from `main`
   - Make focused, atomic commits
   - Test your changes thoroughly
   - Update documentation as needed

3. **Submitting PR**
   - Fill out the PR template completely
   - Link to related issues
   - Request review from maintainers
   - Be responsive to feedback

4. **After Submission**
   - Address review comments
   - Keep your branch updated
   - Be patient - reviews may take time

## Testing

Before submitting, ensure:

- [ ] All notebook cells execute without errors
- [ ] Code follows style guidelines
- [ ] Documentation is updated
- [ ] Examples are clear and working
- [ ] No sensitive data (API keys, credentials) is included

Run the test suite:
```bash
python scripts/test_notebooks.py --dir notebooks
```

## Adding New Content

### New Notebooks

1. Use existing notebooks as templates
2. Follow the standard structure:
   - Overview and objectives
   - Academic readings
   - Conceptual content
   - Code examples
   - Exercises
   - Discussion questions
   - Key takeaways
   - Additional resources

3. Place in appropriate directory
4. Update main README
5. Add to testing suite

### New Datasets

1. Place in `data/samples/` or `data/examples/`
2. Include `.gitignore` exception if needed
3. Document in dataset README
4. Provide data dictionary
5. Include usage examples

### New Utilities

1. Add to appropriate module in `utils/`
2. Include docstrings
3. Add type hints
4. Provide usage examples
5. Write tests

## Questions?

- **Technical Issues**: Open an issue
- **Course Content**: Contact instructor
- **General Questions**: Use discussion forum

## Code of Conduct

- Be respectful and professional
- Focus on constructive feedback
- Help create a welcoming environment
- Follow academic integrity guidelines

## License

By contributing, you agree that your contributions will be licensed under the same terms as the project.

---

Thank you for helping improve this course! 🚀
