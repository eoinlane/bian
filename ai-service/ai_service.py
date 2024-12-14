from flask import Flask, request, jsonify
from kafka import KafkaConsumer
import pickle
import numpy as np
import logging
import os

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("kafka_consumer")

# Flask app
app = Flask(__name__)

# Kafka Consumer setup
kafka_broker = os.getenv("KAFKA_BROKER", "kafka:9092")
consumer = KafkaConsumer(
    "customer_interaction",
    bootstrap_servers=kafka_broker,
    auto_offset_reset="earliest",
    group_id="ai-service-group",
)

# Load the trained model
try:
    with open("clv_model.pkl", "rb") as f:
        model = pickle.load(f)
except FileNotFoundError:
    logger.error("Model file not found.")
    model = None
except Exception as e:
    logger.error(f"Error loading model: {e}")
    model = None


def predict_clv(total_purchases, avg_purchase_value):
    if model is None:
        raise ValueError("Model is not loaded.")
    return model.predict(np.array([[total_purchases, avg_purchase_value]]))[0]


@app.route("/listen", methods=["GET"])
def listen_to_kafka():
    messages = []
    for message in consumer:
        logger.info("Processing message: %s", message.value.decode("utf-8"))
        messages.append(message.value.decode("utf-8"))
        if len(messages) >= 5:  # Stop after processing 5 messages
            break
    return jsonify({"messages_processed": messages})


@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    try:
        total_purchases = float(data.get("total_purchases", 0))
        avg_purchase_value = float(data.get("avg_purchase_value", 0))
    except ValueError:
        return jsonify({"error": "Invalid input data"}), 400

    try:
        prediction = predict_clv(total_purchases, avg_purchase_value)
    except ValueError as e:
        return jsonify({"error": str(e)}), 500

    return jsonify({"predicted_lifetime_value": prediction})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
