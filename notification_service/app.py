from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/send_notification', methods=['POST'])
def send_notification():
    data = request.json
    name = data.get("name")  # safer than data["name"]
    email = data.get("email")

    if not name or not email:
        return jsonify({"error": "Missing name or email"}), 400

    return jsonify({"message": f"Notification sent to {name} at {email}"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
