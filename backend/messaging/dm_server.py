from flask import Flask, request, jsonify
from flask_cors import CORS
from dm_handler import save_message, get_conversation

app = Flask(__name__)
CORS(app)

# Send a message between users
@app.route('/send_message', methods=['POST'])
def send_message():
    data = request.json
    sender_id = data.get('sender_id')
    receiver_id = data.get('receiver_id')
    message = data.get('message')

    try:
        save_message(sender_id, receiver_id, message)
        return jsonify({'message': 'Message sent successfully.'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Get conversation between two users
@app.route('/get_conversation', methods=['GET'])
def get_conversation_route():
    sender_id = request.args.get('sender_id')
    receiver_id = request.args.get('receiver_id')

    try:
        conversation = get_conversation(sender_id, receiver_id)
        return jsonify({'conversation': conversation}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
