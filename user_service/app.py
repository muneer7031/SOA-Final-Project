from flask import Flask, request, jsonify
import requests  # <-- New import

app = Flask(__name__)

users = []

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    users.append(data)

    # Send notification to notification-service
    try:
        notify_response = requests.post(
            "http://notification-service/send_notification",
            json={
                "name": data.get("name"),
                "email": data.get("email")
            },
            timeout=5  # optional: avoid long waits
        )
        print("Notification response:", notify_response.text)
    except Exception as e:
        print("Failed to send notification:", str(e))

    return jsonify({"message": "User registered successfully"}), 201

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
