import logging
from kafka import KafkaConsumer
import json

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("kafka_consumer")

try:
    # Initialize Kafka consumer
    consumer = KafkaConsumer(
        "invoices",
        bootstrap_servers="kafka:9092",
        value_deserializer=lambda m: json.loads(m.decode("utf-8")),
        auto_offset_reset="earliest",
        enable_auto_commit=True,
        group_id="invoice_consumer_group",
    )
    logger.info("Kafka consumer successfully connected and listening...")
except Exception as e:
    logger.error(f"Error connecting Kafka consumer: {e}")
    exit(1)

# Consume messages
try:
    while True:
        logger.info("Polling for new messages...")
        raw_messages = consumer.poll(timeout_ms=1000)
        for topic_partition, messages in raw_messages.items():
            for message in messages:
                logger.info(f"Received message: {message.value}")
        logger.info("Still waiting for messages...")
except KeyboardInterrupt:
    logger.info("Kafka consumer interrupted.")
except Exception as e:
    logger.error(f"Error during consumption: {e}")