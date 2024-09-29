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
        print("Message sent successfully!")
    else:
        print(f"Failed to send message: {response.json()['error']}")

# Function to view conversation
def view_conversation(user1_id, user2_id):
    view_url = f"{base_url}/view_conversation/{user1_id}/{user2_id}"
    response = requests.get(view_url)
    
    if response.status_code == 200:
        conversation = response.json()['conversation']
        for message in conversation:
            print(f"{message['SenderID']} -> {message['ReceiverID']}: {message['Message']}")
    else:
        print(f"Failed to retrieve conversation: {response.json()['error']}")

if __name__ == "__main__":
    user_id = int(input("Enter your user ID: "))
    other_user_id = int(input("Enter the other user's ID: "))

    while True:
        action = input("Enter 'send' to send a message or 'view' to view the conversation: ").strip().lower()
        if action == 'send':
            # Ask whether the user wants to be the sender or receiver
            role = input("Are you the sender or receiver? (type 'sender' or 'receiver'): ").strip().lower()
            message = input("Enter your message: ")

            if role == 'sender':
                send_message(user_id, other_user_id, message)
            elif role == 'receiver':
                send_message(other_user_id, user_id, message)
            else:
                print("Invalid role! Please choose 'sender' or 'receiver'.")
        elif action == 'view':
            view_conversation(user_id, other_user_id)
        else:
            print("Invalid action! Please type 'send' or 'view'.")
