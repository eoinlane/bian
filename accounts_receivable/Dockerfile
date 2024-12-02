# Dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY accounts_receivable.py /app/

RUN pip install flask

CMD ["python", "accounts_receivable.py"]

