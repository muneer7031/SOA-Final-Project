from flask import Flask, request, jsonify
import uuid
from datetime import datetime

app = Flask(__name__)

# In-memory storage for orders
orders = []

@app.route('/create_order', methods=['POST'])
def create_order():
    data = request.json
    
    # Validate required fields
    if not data or 'user_id' not in data or 'items' not in data:
        return jsonify({"error": "Missing required fields"}), 400
    
    # Create new order with unique ID
    order = {
        "order_id": str(uuid.uuid4()),
        "user_id": data['user_id'],
        "items": data['items'],
        "total_amount": data.get('total_amount', 0),
        "status": "pending",
        "created_at": datetime.now().isoformat()
    }
    
    orders.append(order)
    return jsonify({"message": "Order created successfully", "order": order}), 201

@app.route('/orders', methods=['GET'])
def get_orders():
    return jsonify(orders), 200

@app.route('/orders/<order_id>', methods=['GET'])
def get_order(order_id):
    for order in orders:
        if order['order_id'] == order_id:
            return jsonify(order), 200
    return jsonify({"error": "Order not found"}), 404

@app.route('/orders/<order_id>/update_status', methods=['PUT'])
def update_order_status(order_id):
    data = request.json
    
    if not data or 'status' not in data:
        return jsonify({"error": "Status field is required"}), 400
    
    for order in orders:
        if order['order_id'] == order_id:
            order['status'] = data['status']
            return jsonify({"message": "Order status updated", "order": order}), 200
    
    return jsonify({"error": "Order not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
