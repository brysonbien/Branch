import requests
from data_handler import store_credentials, store_mutuals

# Define the base URL for your Flask app
base_url = "http://127.0.0.1:5000"

# Function to log in to the Flask app
def login(username, password):
    login_url = f"{base_url}/login"
    data = {
        "username": username,
        "password": password
    }
    response = requests.post(login_url, json=data)
    
    if response.status_code != 200:
        print("Login failed. Please check your credentials.")
        return False
    
    # Store credentials after successful login
    store_credentials(username, password)
    return True

# Function to get mutual followers
def get_mutuals(username):
    mutuals_url = f"{base_url}/mutuals"
    response = requests.get(mutuals_url)
    
    if response.status_code == 200:
        mutuals = response.json().get('mutuals', [])
        mutual_usernames = [mutual['username'] for mutual in mutuals]
        
        # Store mutual followers
        store_mutuals(username, mutual_usernames)
        
        # Display the mutuals associated with your username
        print(f"Mutuals associated with {username}: {mutual_usernames}")
        return mutual_usernames
    else:
        print("Failed to retrieve mutual followers.")
        return None

if __name__ == "__main__":
    # Prompt user for credentials
    username = input("Enter your Instagram username: ")
    password = input("Enter your Instagram password: ")

    # Step 1: Log in
    if login(username, password):
        # Step 2: Get mutual followers and associate with username
        get_mutuals(username)
