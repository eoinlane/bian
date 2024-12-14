# Use a slim Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements.txt and install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY kafka_consumer.py /app/

# Set the command to run the consumer script
CMD ["python", "kafka_consumer.py"]