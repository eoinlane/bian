# Dockerfile
# Use a slim Python image to reduce the image size
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY customer_billing.py /app/

# Expose the application port
EXPOSE 8000

# Command to run the application
CMD ["python", "customer_billing.py"]
