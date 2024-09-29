import os
import sys
import pymysql
from classes import *
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', 'genAI'))
import interests_recommender
import json
from db_reader import *

# Read database password from pass.txt file
def get_db_password():
    with open(os.path.join(os.path.dirname(__file__), '..', 'password.txt'), 'r') as f:
        return f.read().strip()

DB_PASSWORD = get_db_password()

# Function to get a database connection
def get_connection():
    """Create a new database connection."""
    timeout = 10  # Define connection parameters
    return pymysql.connect(
        charset="utf8mb4",
        connect_timeout=timeout,
        cursorclass=pymysql.cursors.DictCursor,
        db="defaultdb",
        host="mysql-223d04d7-branch-hackathon.h.aivencloud.com",
        password=DB_PASSWORD,
        read_timeout=timeout,
        port=14022,
        user="avnadmin",
        write_timeout=timeout,
    )

# Function to add a user to the Users table
def add_user(username, password_hash, mutuals):
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute("USE `UserManagement`;")
            sql = """
            INSERT INTO `Users` (`Username`, `PasswordHash`, `mutuals`)
            VALUES (%s, %s, %s)
            ON DUPLICATE KEY UPDATE
            `PasswordHash` = VALUES(`PasswordHash`),
            `Location` = VALUES(`Location`),
            `mutuals` = VALUES(`mutuals`);
            """
            cursor.execute(sql, (username, password_hash, mutuals))
        connection.commit()
        print(f"User '{username}' added/updated in Users table.")
    except pymysql.MySQLError as e:
        print(f"Failed to add user: {e.args[1]} (Error Code: {e.args[0]})")
    finally:
        if connection:
            connection.close()

def update_user(UserOBJ):
    interest_list = json.dumps(UserOBJ.InterestList)
    extended_interest_list = json.dumps(interests_recommender.get_interests_recommender(UserOBJ.InterestList))
    print(extended_interest_list)
    password_hash = UserOBJ.Password
    username = UserOBJ.Username
    image = UserOBJ.Image
    location = UserOBJ.Location
    userid = UserOBJ.UserID
    
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute("USE `UserManagement`;")
            sql = """
            UPDATE `Users` 
            SET
                `Username` = %s,
                `Image` = %s,
                `InterestList` = %s,
                `PasswordHash` = %s,
                `Location` = %s,
                `Extended Interests` = %s
            WHERE `UserID` = %s;
            """
            print(userid, userid, username, image, interest_list, password_hash, location, extended_interest_list)
            cursor.execute(sql, (username, image, interest_list, password_hash, location, extended_interest_list, userid))
        connection.commit()
        print(f"User '{username}' added/updated in Users table.")
    except pymysql.MySQLError as e:
        print(f"Failed to update user: {e.args[1]} (Error Code: {e.args[0]})")
    finally:
        if connection:
            connection.close()

def add_event(EventOBJ):
    EventID = EventOBJ.EventID
    AttendeeArr = EventOBJ.AttendeeArr
    EventName = EventOBJ.EventName
    Description = EventOBJ.EventDescription
    Date = EventOBJ.EventDate
    Location = EventOBJ.Location
    Attendees = EventOBJ.AllAttendeeArr
    EventTags = interests_recommender.get_event_tags(EventName, Description)
    return
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute("USE `UserManagement`;")
            sql = """
            INSERT INTO `Users` (`Username`, `Image`, `InterestList`, `PasswordHash`, `Location`, `Extended Interests`)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE
            `PasswordHash` = VALUES(`PasswordHash`),
            `Location` = VALUES(`Location`),
            `mutuals` = VALUES(`mutuals`);
            """
            cursor.execute(sql, (username, image, interest_list, password_hash, location, extended_interest_list))
        connection.commit()
        print(f"User '{username}' added/updated in Users table.")
    except pymysql.MySQLError as e:
        print(f"Failed to add user: {e.args[1]} (Error Code: {e.args[0]})")
    finally:
        if connection:
            connection.close()


if __name__ == "__main__":
    # Add a user (example)
    add_user('johnny test', 'doge', json.dumps('john_doe'))
    #print(json.dumps(['reading', 'traveling', 'coding', 'fucking']))
    tempuser = User(find_userid('johnny test'))
    tempuser.fill_user()
    tempuser.InterestList = ['refrevre', 'trreveng', 'cewfeg', 'skarevng']
    tempuser.Location = 'Mommyc'

    update_user(tempuser)
    #print(tempuser.UserID, tempuser.Username, tempuser.InterestList, tempuser.Password, tempuser.Image, tempuser.ExtendedInterestList, tempuser.Location)
    #print(tempuser.myEventIDArr)
