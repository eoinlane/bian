# Dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY customer_billing.py /app/

RUN pip install flask

CMD ["python", "customer_billing.py"]
