from flask import Flask, jsonify, request
from kafka import KafkaProducer

app = Flask(__name__)
producer = KafkaProducer(bootstrap_servers='kafka:9092', value_serializer=lambda v: str(v).encode('utf-8'))

@app.route('/api/customers', methods=['POST'])
def create_customer():
    data = request.json
    producer.send('customer_interaction', value=data)
    return jsonify({"message": "Customer interaction sent to Kafka"}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
