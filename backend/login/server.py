# python3 /backend/login/server.py
from flask import Flask, request, jsonify, Response
from flask_cors import CORS
from instagrapi import Client
from instagrapi.exceptions import ChallengeRequired, LoginRequired
import json
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'database'))
import db_writer
import classes
import db_reader
import initializeApp
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'messaging'))
import dm_handler

# Initialize Flask app and Instagram client
app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes
cl = Client()

class AppInstance:
    def __init__(self):
        self.MyUser = None
        self.FriendUserList = []
        self.EventList = []
    
    def reset(self):
        self.MyUser = None
        self.FriendUserList = []
        self.EventList = []

CurrentInstance = AppInstance()

# Convert all non-serializable objects in user info to strings for Instagram API user/pass
def serialize_user_info(user_info_dict):
    """
    Serialize user_info to ensure all non-serializable objects are converted to strings.
    """
    for key, value in user_info_dict.items():
        try:
            jsonify({key: value})
        except TypeError:
            user_info_dict[key] = str(value)
    return user_info_dict

# Handles Instagram login and retrieves mutual followers if successful
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    try:
        # Log in to Instagram
        cl.login(username, password)

        # Fetch user info
        try:
            user_info = cl.user_info_by_username(username)
            user_info_serialized = serialize_user_info(user_info.dict())
        except json.JSONDecodeError as json_err:
            print(f"JSON decoding failed: {json_err}")
            return jsonify({'error': 'Unable to parse response from Instagram.'}), 500

        # Fetch mutual followers immediately after successful login
        followers = cl.user_followers(cl.user_id)
        following = cl.user_following(cl.user_id)
        mutual_ids = set(followers.keys()).intersection(set(following.keys()))
        mutuals = [{"username": followers[user_id].username} for user_id in mutual_ids]

        # Print mutuals for debugging
        mutual_usernames = [follower['username'] for follower in mutuals]
        print(f"Mutual followers for {username}: {mutual_usernames}")

        # Store user credentials, user info, and mutual followers in the database
        db_writer.add_user(
            username=username,
            password_hash=password,  # Consider hashing the password before storing it
            mutuals=json.dumps(mutual_usernames)  # Convert mutuals to JSON string
        )

        # Return response
        return jsonify({'message': 'Login successful', 'user_info': user_info_serialized, 'mutuals': mutuals}), 200
    
    except ChallengeRequired:
        return jsonify({'error': '2FA challenge required. Check your email or SMS for the code.'}), 403
    except LoginRequired:
        return jsonify({'error': 'Login failed. Check your credentials and try again.'}), 401
    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({'error': str(e)}), 400

# Initialization
@app.route('/init', methods=['POST'])
def init():
    data = request.json
    username = data.get('username')
    try:
        userID = db_reader.find_userid(username)
    except Exception as e:
        return jsonify({'error': 'Username Invalid!'})
    
    
    CurrentInstance.MyUser = classes.User(userID)
    initializeApp.init(CurrentInstance)
    print(CurrentInstance.EventList)

    
    return jsonify({
    'message': 'Initialization successful.',
}), 200

# Get My Profile Page
@app.route('/myprofilepage', methods=['GET'])
def myprofilepage():
    """data = request.json
    username = data.get('username')
    try:
        userID = db_reader.find_userid(username)
    except Exception as e:
        return jsonify({'error': 'Username Invalid!'})"""

    
    return jsonify({
    'message': 'User Found',
    'Name' : CurrentInstance.MyUser.Name,
    'Image': CurrentInstance.MyUser.Image,
    'InterestList': CurrentInstance.MyUser.InterestList,
    'Location': CurrentInstance.MclsyUser.Location,
}), 200

# Update Profile
@app.route('/updateprofile', methods=['GET', 'POST'])
def updateprofilepage():
    data = request.json
    CurrentInstance.MyUser.Name = data.get('Name')
    CurrentInstance.MyUser.InterestList = data.get('interest_list')
    CurrentInstance.MyUser.Location = data.get('location')
    try:
        db_writer.update_user(CurrentInstance.MyUser)
    except Exception as e:
        return jsonify({'error': 'Failed to Update'})

    
    return jsonify({
    'message': 'Sucessful Update',
}), 200

# Get Generic Profile
@app.route('/profilepage', methods=['POST'])
def profilepage():
    data = request.json
    username = data.get('username')
    try:
        userID = db_reader.find_userid(username)
    except Exception as e:
        return jsonify({'error': 'Username Invalid!'})

    user = classes.User(userID)
    user.fill_user()

    
    return jsonify({
    'message': 'User Found',
    'Name' : user.Name,
    'Image': user.Image,
    'InterestList': user.InterestList,
    'Location': user.Location
}), 200


# Get My Events Page
@app.route('/myeventspage', methods=['GET'])
def myeventspage():
    """data = request.json
    username = data.get('username')
    try:
        userID = db_reader.find_userid(username)
    except Exception as e:
        return jsonify({'error': 'Username Invalid!'})"""

    jsonArr = []
    for event in CurrentInstance.EventList:
        print(event.EventName, 'EVENTfrceewcercrcwecw')
        jsonArr.append(jsonify({
        'EventName' : event.EventName,
        'EventDate': event.EventDate,
        'Location': event.Location,
        'Known Attendees' : event.KAttendeeArr
        }))

    return Response(json.dumps(jsonArr), mimetype='application/json'), 200

# Get My Events Page
@app.route('/createevent', methods=['POST'])
def createevent():
    data = request.json
    username = data.get('username')

    userid = db_reader.find_userid(username)
    currUser = classes.User(userid)
    currUser.fill_user()

    newEvent = classes.Event([userid])
    newEvent.EventName  = data.get('EventName')
    newEvent.EventDate  = data.get('EventDate')
    newEvent.EventDescription  = data.get('EventDescripton')
    newEvent.Location = data.get('Location')
    try:
        db_writer.add_event(newEvent)
    except Exception as e:
        return jsonify({'error': 'Event Not Created!'})
    currUser.EventsList = json.dumps(newEvent.EventID)
    print(newEvent.EventID, 'this is the event id')
    try:
        db_writer.update_user(currUser)
        return jsonify({'message': newEvent.EventID})
    except Exception as e:
        return jsonify({'error': 'User Not Updated!'})

@app.route('/getusername', methods=['GET'])
def getusername():
    return CurrentInstance.MyUser.Username
    

# Get Generic Event
@app.route('/event', methods=['POST'])
def event():
    data = request.json
    EventID = data.get('eventID')
    
    newEvent = classes.Event([CurrentInstance.MyUser.UserID], EventID)
    db_reader.fill_event(newEvent)

    
    return jsonify({
        'message': 'Event Found',
        'EventName' : newEvent.EventName,
        'EventDate' : newEvent.EventDate,
        'EventDescription' : newEvent.EventDescription,
        'Location': newEvent.Location
    }), 200
# Get Generic Event
@app.route('/simpleinit', methods=['POST'])
def simpleinit():
    data = request.json
    EventID = data.get('eventID')
    
    newEvent = classes.Event([CurrentInstance.MyUser.UserID], EventID)
    db_reader.fill_event(newEvent)

    
    return jsonify({
        'message': 'Event Found',
        'EventName' : newEvent.EventName,
        'EventDate' : newEvent.EventDate,
        'EventDescription' : newEvent.EventDescription,
        'Location': newEvent.Location
    }), 200


# Debugging route for testing server status
@app.route('/')
def home():
    return "Server is running", 200

# --- Messaging Functionality ---
# Endpoint to send a message
@app.route('/send_message', methods=['POST'])
def send_message():
    data = request.json
    sender_id = data.get('sender_id')
    receiver_id = data.get('receiver_id')
    message = data.get('message')
    print(sender_id)
    print(receiver_id)
    try:
        # Write the message to the database
        dm_handler.add_message(sender_id, receiver_id, message)
        return jsonify({'message': 'Message sent successfully!'}), 200
    except pymysql.MySQLError as e:
        return jsonify({'error': str(e)}), 500

# Endpoint to view conversation between two users
@app.route('/view_conversation/<string:user1_id>/<string:user2_id>', methods=['GET'])
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
