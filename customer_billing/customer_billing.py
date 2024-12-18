# customer_billing.py
from flask import Flask, jsonify, request
from kafka import KafkaProducer
import json

app = Flask(__name__)

# Mock database for invoices
invoices = {}

# Kafka producer setup
producer = KafkaProducer(
    bootstrap_servers='kafka:9092',  # Kafka container name from Docker Compose
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

@app.route("/create", methods=["POST"])
def create_invoice():
    data = request.json
    invoice_id = len(invoices) + 1
    invoices[invoice_id] = {
        "customer_id": data["customer_id"],
        "amount": data["amount"],
        "status": "Created",
        "due_date": data["due_date"],
    }

        # Send an event to Kafka topic
    producer.send('invoices', value={
        "invoice_id": invoice_id,
        "customer_id": data["customer_id"],
        "amount": data["amount"],
        "due_date": data["due_date"],
        "status": "Created"
    })

    return jsonify({"invoice_id": invoice_id, "message": "Invoice created"}), 201


@app.route("/retrieve/<int:invoice_id>", methods=["GET"])
def retrieve_invoice(invoice_id):
    invoice = invoices.get(invoice_id)
    if invoice:
        return jsonify(invoice), 200
    return jsonify({"message": "Invoice not found"}), 404


@app.route("/overdue", methods=["GET"])
def get_overdue_invoices():
    overdue = [id_ for id_, inv in invoices.items() if inv["status"] == "Overdue"]
    return jsonify(overdue), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
