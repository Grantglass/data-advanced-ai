# Troubleshooting Guide

Common issues and their solutions for MBA 590 course materials.

## Installation Issues

### Python Version Issues

**Problem**: "Python 3.8 or higher required"

**Solution**:
```bash
# Check your Python version
python --version

# If too old, install Python 3.11
# On Mac with Homebrew:
brew install python@3.11

# On Ubuntu/Debian:
sudo apt update
sudo apt install python3.11

# On Windows: Download from python.org
```

### Package Installation Failures

**Problem**: `pip install` fails with permission errors

**Solution**:
```bash
# Use virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

# Or install for user only
pip install --user -r requirements.txt
```

**Problem**: `ModuleNotFoundError` after installation

**Solution**:
```bash
# Ensure you're in the correct environment
which python  # Should show venv/bin/python

# Reinstall requirements
pip install -r requirements.txt --force-reinstall
```

### Jupyter Not Found

**Problem**: `jupyter: command not found`

**Solution**:
```bash
# Install Jupyter
pip install jupyter jupyterlab

# Verify installation
jupyter --version

# Launch Jupyter
jupyter lab
```

## Runtime Issues

### Kernel Dies or Restarts

**Problem**: Jupyter kernel keeps dying

**Solutions**:
1. **Reduce memory usage**:
   - Close other applications
   - Restart the kernel
   - Process data in smaller batches

2. **Increase memory limit**:
   ```bash
   # For JupyterLab
   jupyter lab --NotebookApp.max_buffer_size=1000000000
   ```

3. **Check for infinite loops**:
   - Review recent code changes
   - Add print statements to track progress

### Import Errors

**Problem**: `ModuleNotFoundError: No module named 'tiktoken'`

**Solution**:
```bash
# Install missing package
pip install tiktoken

# Or reinstall all requirements
pip install -r requirements.txt
```

**Problem**: `ImportError: cannot import name 'PromptTemplate'`

**Solution**:
```bash
# Ensure utils module is in Python path
export PYTHONPATH="${PYTHONPATH}:/path/to/data-advanced-ai"

# Or add to notebook:
import sys
sys.path.append('/path/to/data-advanced-ai')
```

### API Issues

**Problem**: `AuthenticationError: Invalid API key`

**Solution**:
1. Check `.env` file exists and contains your key
2. Verify key is correct (no extra spaces)
3. Check API key is active in provider dashboard
4. Ensure `.env` is loaded:
   ```python
   from dotenv import load_dotenv
   load_dotenv()
   import os
   print(os.getenv('OPENAI_API_KEY')[:10])  # Should show first 10 chars
   ```

**Problem**: `RateLimitError` or `QuotaExceeded`

**Solution**:
1. Check your usage limits in API dashboard
2. Add delays between requests:
   ```python
   import time
   time.sleep(1)  # Wait 1 second between calls
   ```
3. Use cheaper models for testing (`gpt-3.5-turbo`)
4. Work with mock responses during development

## Data Issues

### File Not Found

**Problem**: `FileNotFoundError: [Errno 2] No such file or directory: 'data/samples/...'`

**Solution**:
```bash
# Check current directory
pwd

# Should be in repo root
cd /path/to/data-advanced-ai

# Verify data files exist
ls data/samples/

# If missing, check git status
git status
```

### CSV Encoding Issues

**Problem**: `UnicodeDecodeError` when loading CSV

**Solution**:
```python
# Try different encodings
df = pd.read_csv('file.csv', encoding='utf-8')
# Or
df = pd.read_csv('file.csv', encoding='latin-1')
# Or
df = pd.read_csv('file.csv', encoding='cp1252')
```

## Visualization Issues

### Plots Not Displaying

**Problem**: Matplotlib plots don't show

**Solution**:
```python
# Add to first cell of notebook
%matplotlib inline

# Or use explicit display
import matplotlib.pyplot as plt
plt.show()
```

**Problem**: Plotly plots not interactive

**Solution**:
```python
# Install required extensions
pip install jupyter-dash

# Enable in notebook
import plotly.io as pio
pio.renderers.default = 'notebook'
```

## Git Issues

### Large Files

**Problem**: `remote: error: File is too large`

**Solution**:
```bash
# Remove from staging
git rm --cached large_file.csv

# Add to .gitignore
echo "large_file.csv" >> .gitignore

# Use Git LFS for large files (if needed)
git lfs install
git lfs track "*.csv"
```

### Merge Conflicts in Notebooks

**Problem**: Merge conflicts in `.ipynb` files

**Solution**:
```bash
# Install nbdime for better notebook diffs
pip install nbdime

# Configure git to use nbdime
nbdime config-git --enable --global

# Use nbdime to merge
nbdime mergetool
```

## Docker Issues

### Docker Build Fails

**Problem**: `ERROR: failed to solve`

**Solution**:
```bash
# Clean Docker cache
docker system prune -a

# Rebuild without cache
docker-compose build --no-cache

# Check Docker resources (Memory, CPU)
docker info
```

### Permission Issues in Container

**Problem**: Cannot write files in Docker container

**Solution**:
```yaml
# In docker-compose.yml, add user mapping
user: "${UID}:${GID}"

# Or run with current user
docker-compose run --user $(id -u):$(id -g) jupyter
```

## Performance Issues

### Slow Notebook Execution

**Solutions**:
1. **Reduce data size**:
   ```python
   # Sample large datasets
   df_sample = df.sample(n=1000)
   ```

2. **Use caching**:
   ```python
   from functools import lru_cache

   @lru_cache(maxsize=128)
   def expensive_function(param):
       # ...
   ```

3. **Profile code**:
   ```python
   %time your_function()  # Time single execution
   %timeit your_function()  # Time multiple runs
   ```

## Getting Additional Help

If you're still experiencing issues:

1. **Check the FAQ**: See [FAQ.md](FAQ.md)
2. **Search existing issues**: [GitHub Issues](https://github.com/yourusername/data-advanced-ai/issues)
3. **Check package documentation**: Most errors have solutions in package docs
4. **Ask in course forum**: Other students may have encountered the same issue
5. **Open a new issue**: Include:
   - Error message (full traceback)
   - Steps to reproduce
   - Your environment (OS, Python version)
   - What you've already tried

## Environment Information

To help diagnose issues, provide:

```bash
# Python version
python --version

# Installed packages
pip list

# Jupyter version
jupyter --version

# OS information
# On Mac/Linux:
uname -a
# On Windows:
systeminfo
```

---

**Last Updated**: November 2025
