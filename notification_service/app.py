from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/send_notification', methods=['POST'])
def send_notification():
    data = request.json
    return jsonify({"message": f"Notification sent to {data['user']}"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
