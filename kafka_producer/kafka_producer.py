from kafka import KafkaProducer
import json

producer = KafkaProducer(
    bootstrap_servers="kafka:9092",  # Use the Kafka container hostname
    value_serializer=lambda v: json.dumps(v).encode("utf-8"),
)

# Produce an invoice creation event
producer.send(
    "invoices",
    {"event_type": "invoice_created", "invoice_id": 123, "amount": 500.0},
)
producer.flush()
