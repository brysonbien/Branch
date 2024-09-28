import requests

# Define the base URL for your Flask app
base_url = "http://127.0.0.1:5000"

# Function to send a message
def send_message(sender_id, receiver_id, message):
    send_url = f"{base_url}/send_message"
    data = {
        "sender_id": sender_id,
        "receiver_id": receiver_id,
        "message": message
    }
    response = requests.post(send_url, json=data)
    if response.status_code == 200:
        print("Message sent successfully.")
    else:
        print(f"Failed to send message: {response.json().get('error')}")

# Function to get a conversation
def get_conversation(sender_id, receiver_id):
    get_url = f"{base_url}/get_conversation?sender_id={sender_id}&receiver_id={receiver_id}"
    response = requests.get(get_url)
    if response.status_code == 200:
        conversation = response.json().get('conversation', [])
        for message in conversation:
            print(f"{message['Timestamp']} - {message['SenderID']} to {message['ReceiverID']}: {message['Message']}")
    else:
        print(f"Failed to retrieve conversation: {response.json().get('error')}")

if __name__ == "__main__":
    # Sample flow for sending and receiving messages
    sender_id = input("Enter your user ID: ")
    receiver_id = input("Enter receiver's user ID: ")
    
    while True:
        action = input("Enter 'send' to send a message or 'view' to view the conversation: ").strip().lower()
        if action == 'send':
            message = input("Enter your message: ")
            send_message(sender_id, receiver_id, message)
        elif action == 'view':
            get_conversation(sender_id, receiver_id)
        else:
            print("Invalid action. Please enter 'send' or 'view'.")
