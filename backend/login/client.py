import requests

# Define the base URL for your Flask app
base_url = "http://127.0.0.1:5000"

def testInit(username):
    login_url = f"{base_url}/init"
    data = {
        "username": username,
    }
    response = requests.post(login_url, json=data)

def testMyProfile():
    login_url = f"{base_url}/myprofilepage"
    response = requests.post(login_url)

def tcreateEvent():
    login_url = f"{base_url}/createevent"
    data = {
        "username" : username,
        "EventName": 'Test Event for CreateEVENT API CALL',
        "EventDate": '2024-09-29 10:45:00',
        "EventDescription": 'noting',
        "EventLocation" : 'Mommyc'
    }
    response = requests.post(login_url, json=data)

def tupdateProfile():
    login_url = f"{base_url}/updateprofile"
    data = {
        'Name': 'reynaldo',
        'interest_list': ['Stargazing', 'Icecream', 'Tennis', 'Hiking', 'Food'],
        'location': 'belize'
    }
    response = requests.post(login_url, json=data)

def tgetAI():
    login_url = f"{base_url}/getAIInterests"
    response = requests.get(login_url)
    json_response = response.json()
    print("JSON Response:")
    print(json_response)


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
    
    return True

if __name__ == "__main__":
    # Prompt user for credentials
    username = input("Enter your Instagram username: ")
    password = input("Enter your Instagram password: ")

    # Log in
    testInit(username)
    tupdateProfile()
    tgetAI()
    tcreateEvent()
    #testMyProfile()
