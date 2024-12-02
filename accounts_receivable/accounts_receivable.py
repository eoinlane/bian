# accounts_receivable.py
from flask import Flask, jsonify, request

app = Flask(__name__)

# Mock database for payments
payments = {}


@app.route("/update_payment", methods=["POST"])
def update_payment():
    data = request.json
    payments[data["invoice_id"]] = {"amount_paid": data["amount"], "status": "Paid"}
    return jsonify({"message": "Payment updated"}), 200


@app.route("/get_status/<int:invoice_id>", methods=["GET"])
def get_status(invoice_id):
    payment = payments.get(invoice_id)
    if payment:
        return jsonify(payment), 200
    return jsonify({"message": "No payment record found"}), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8001)
