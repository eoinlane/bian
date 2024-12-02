from kafka import KafkaConsumer
import json

# Kafka Consumer Setup
consumer = KafkaConsumer(
    "invoice_events",  # Topic name
    bootstrap_servers="kafka:9092",  # Kafka container hostname and port
    value_deserializer=lambda m: json.loads(m.decode("utf-8")),
    auto_offset_reset="earliest",  # Start consuming from the earliest message
    group_id="invoice_consumer_group",  # Consumer group ID
)

print("Listening for messages on 'invoice_events' topic...")

# Consume messages
for message in consumer:
    print(f"Received message: {message.value}")
