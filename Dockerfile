# Base image
FROM python:3.9-slim

# Install dependencies
RUN pip install --no-cache-dir pandas pyhdfs

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Define entry point
CMD ["python", "scripts/execute_model.py"]
