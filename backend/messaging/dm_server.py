from flask import Flask, request, jsonify
from flask_cors import CORS
import pymysql
import dm_handler  # Import database handler functions

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Endpoint to send a message
@app.route('/send_message', methods=['POST'])
def send_message():
    data = request.json
    sender_id = data.get('sender_id')
    receiver_id = data.get('receiver_id')
    message = data.get('message')
    
    try:
        # Write the message to the database
        dm_handler.add_message(sender_id, receiver_id, message)
        return jsonify({'message': 'Message sent successfully!'}), 200
    except pymysql.MySQLError as e:
        return jsonify({'error': str(e)}), 500

# Endpoint to view conversation between two users
@app.route('/view_conversation/<int:user1_id>/<int:user2_id>', methods=['GET'])
def view_conversation(user1_id, user2_id):
    try:
        # Retrieve conversation from the database
        conversation = dm_handler.get_conversation(user1_id, user2_id)
        return jsonify({'conversation': conversation}), 200
    except pymysql.MySQLError as e:
        return jsonify({'error': str(e)}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
