from flask import Flask, request, jsonify
from flask_cors import CORS
from instagrapi import Client
from instagrapi.exceptions import ChallengeRequired, LoginRequired
from classes import Profile, Event, CustomHashSet
from mySQLconn import connection
from backend.connection import *
from backend.login import *


# Initialize Flask app and Instagram client
app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes
cl = Client()

# Convert all non-serializable objects in user info to strings for instagramapi user/pass
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

# Home route that returns 404 as this is not used
@app.route('/')
def home():
    return "404 Not Found", 404

# Handles Instagram login and returns user information if successful
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    
    try:
        cl.login(username, password)
        user_info_serialized = serialize_user_info(cl.user_info_by_username(username).dict())
        return jsonify({'message': 'Login successful', 'user_info': user_info_serialized}), 200
    except ChallengeRequired:
        return jsonify({'error': '2FA challenge required. Check your email or SMS for the code.'}), 403
    except LoginRequired:
        return jsonify({'error': 'Login failed. Check your credentials and try again.'}), 401
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Retrieves mutual followers (people who follow you and you follow back)
@app.route('/mutuals', methods=['GET'])
def mutual_followers():
    try:
        followers = cl.user_followers(cl.user_id)
        following = cl.user_following(cl.user_id)
        mutual_ids = set(followers.keys()).intersection(set(following.keys()))
        mutuals = [{"username": followers[user_id].username} for user_id in mutual_ids]
        return jsonify({'mutuals': mutuals}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400
    
@app.route('/newprofile', methods=['POST'])
def new_profile():
    data = request.json
    userID = data.get('userID')  #USER ID
    username = data.get('username') 
    password = data.get('password')
    location = data.get('location')
    interests = data.get('interests')
    friendList = data.get('friendList')

    
    try:
        db_writer.new_profile(jsonify(userID, username, password, location, interests, friendList))
        return jsonify({'message': 'Login successful', 'user_info': user_info_serialized}), ???
    except ____:
        return jsonify({'error': 'Duplicate profile already exists, try updateprofile medthod.'}), ???
    except ____:
        return jsonify({'error': 'One or more parameters are incorrect.'}), ???
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@app.route('/profile/<int:profile_id>', methods=['GET'])
def get_profile(profile_id):
    try:
        profile = Profile(profile_id)
        return jsonify({
            'ProfileID': profile.ProfileID,
            'FriendIDArr': profile.FriendIDArr,
            'myEventIDArr': profile.myEventIDArr
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/events', methods=['GET'])
def get_events():
    try:
        events = init.GLOBALEventOBJ
        event_data = [{
            'EventID': event.EventID,
            'KAttendeeArr': event.KAttendeeArr,
            'UKAttendeeArr': event.UKAttendeeArr
        } for event in events]
        return jsonify({'events': event_data}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/friends', methods=['GET'])
def get_friends():
    try:
        friends = init.GLOBALFriendOBJ
        friend_data = [{
            'ProfileID': friend.ProfileID,
            'FriendIDArr': friend.FriendIDArr,
            'myEventIDArr': friend.myEventIDArr
        } for friend in friends]
        return jsonify({'friends': friend_data}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
