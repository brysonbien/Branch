from flask import Flask, request, jsonify
from flask_cors import CORS
from dm_handler import send_message, get_messages, create_messages_table

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Ensure the Messages table is created
create_messages_table()

# Route to send a message from one user to another
@app.route('/send_message', methods=['POST'])
def send_message_route():
    data = request.json
    sender_id = data.get('sender_id')
    receiver_id = data.get('receiver_id')
    message = data.get('message')

    try:
        send_message(sender_id, receiver_id, message)
        return jsonify({'message': 'Message sent successfully'}), 200
    except Exception as e:
        print(f"Failed to send message: {e}")
        return jsonify({'error': str(e)}), 400

# Route to get messages between two users
@app.route('/get_messages', methods=['GET'])
def get_messages_route():
    user1_id = request.args.get('user1_id')
    user2_id = request.args.get('user2_id')

    try:
        messages = get_messages(user1_id, user2_id)
        return jsonify({'messages': messages}), 200
    except Exception as e:
        print(f"Failed to retrieve messages: {e}")
        return jsonify({'error': str(e)}), 400

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
