FROM python:3.9-slim

WORKDIR /app

COPY kafka_producer.py /app/

RUN pip install kafka-python

CMD ["python", "kafka_producer.py"]
