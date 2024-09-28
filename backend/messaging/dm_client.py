import requests

# Define the base URL for your Flask app
base_url = "http://127.0.0.1:5000"

# Function to send a message
def send_message(sender_id, receiver_id, message):
    url = f"{base_url}/send_message"
    data = {
        "sender_id": sender_id,
        "receiver_id": receiver_id,
        "message": message
    }
    response = requests.post(url, json=data)
    if response.status_code == 200:
        print("Message sent successfully.")
    else:
        print(f"Failed to send message: {response.json().get('error')}")

# Function to get messages between two users
def get_messages(user1_id, user2_id):
    url = f"{base_url}/get_messages"
    params = {
        "user1_id": user1_id,
        "user2_id": user2_id
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        messages = response.json().get('messages')
        for msg in messages:
            print(f"[{msg['Timestamp']}] {msg['SenderID']} to {msg['ReceiverID']}: {msg['Message']}")
    else:
        print(f"Failed to retrieve messages: {response.json().get('error')}")

if __name__ == "__main__":
    # Test sending and receiving messages
    sender_id = input("Enter sender ID: ")
    receiver_id = input("Enter receiver ID: ")
    message = input("Enter message: ")

    send_message(sender_id, receiver_id, message)

    # Fetch and display messages
    get_messages(sender_id, receiver_id)
