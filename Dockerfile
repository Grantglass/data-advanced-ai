# MBA 590 - Advanced AI Strategy Course Environment
FROM python:3.11-slim

# Set working directory
WORKDIR /workspace

# Install system dependencies
RUN apt-get update && apt-get install -y \
    git \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy course materials
COPY . .

# Create necessary directories
RUN mkdir -p /workspace/outputs /workspace/data

# Expose Jupyter port
EXPOSE 8888

# Set environment variables
ENV PYTHONPATH=/workspace
ENV JUPYTER_ENABLE_LAB=yes

# Create non-root user
RUN useradd -m -u 1000 student && \
    chown -R student:student /workspace

USER student

# Default command: start JupyterLab
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]
