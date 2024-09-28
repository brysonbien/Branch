from flask import Flask, request, jsonify
from flask_cors import CORS
from instagrapi import Client
from instagrapi.exceptions import ChallengeRequired, LoginRequired
import json
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'database'))
import db_writer

# Initialize Flask app and Instagram client
app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes
cl = Client()

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

# Debugging route for testing server status
@app.route('/')
def home():
    return "Server is running", 200

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
