# Dockerfile
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the application files
COPY ai_agent.py /app/

# Install dependencies
RUN pip install --no-cache-dir \
    flask \
    langchain-openai \
    langchain_community \
    openai

# Set the environment variable (you should replace YOUR_API_KEY with your actual key or set it dynamically)
ENV OPENAI_API_KEY="YOUR_API_KEY"

# Set the entry point
CMD ["python", "ai_agent.py"]
