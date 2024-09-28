import json
import os

# Define file paths for storing data
CREDENTIALS_FILE = "credentials.txt"
MUTUALS_FILE = "mutuals.json"

def store_credentials(username, password):
    """
    Store the username and password in 'username-password' format.
    """
    credentials = f"{username}-{password}"
    with open(CREDENTIALS_FILE, "w") as file:
        file.write(credentials)

def retrieve_credentials():
    """
    Retrieve and unpack the stored username and password.
    """
    if not os.path.exists(CREDENTIALS_FILE):
        return None, None
    
    with open(CREDENTIALS_FILE, "r") as file:
        credentials = file.read().strip()
    
    username, password = credentials.split("-", 1)
    return username, password

def store_mutuals(username, mutuals):
    """
    Store the mutual followers in a dictionary format:
    {username: [list_of_mutuals]}
    """
    data = {username: mutuals}
    with open(MUTUALS_FILE, "w") as file:
        json.dump(data, file, indent=4)

def retrieve_mutuals():
    """
    Retrieve the stored mutual followers from the file.
    """
    if not os.path.exists(MUTUALS_FILE):
        return {}
    
    with open(MUTUALS_FILE, "r") as file:
        return json.load(file)
