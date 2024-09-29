import os
import pymysql
from classes import *
import json
import ast

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

def find_userid(username):
    #print(username, '<<<<<<<<<<<<<<')
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute("USE `UserManagement`;")
            sql = """
            SELECT `UserID`
            FROM `Users` 
            WHERE `Username` = %s
            """
            cursor.execute(sql, (username,))
            result = cursor.fetchone()
            
            if result:
                print(f"Userid is: {result}")
                return result['UserID']
            else:
                print(f"No user found with Username: {username}")

    except pymysql.MySQLError as e:
        print(f"Database error: {e.args[1]} (Error Code: {e.args[0]})")
    finally:
        if connection:
            connection.close()

def parse_json_list(list_str):
    if not list_str:
        return []
    try:
        # First, try to parse it as a JSON string
        return json.loads(list_str)
    except json.JSONDecodeError:
        try:
            # If JSON parsing fails, try to evaluate it as a Python literal
            return ast.literal_eval(list_str)
        except (SyntaxError, ValueError):
            # If both methods fail, fall back to splitting by comma
            return [interest.strip(' "[]') for interest in list_str.split(',')]

# Function to add a user to the Users table
def fill_user(UserOBJ):
    userid = UserOBJ.UserID
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute("USE `UserManagement`;")
            sql = """
            SELECT `Name`, `Username`, `Image`, `InterestList`,`PasswordHash`, `Location`, `mutuals`, `Extended Interests`, `EventsList`
            FROM `Users` 
            WHERE `UserID` = %s
            """
            cursor.execute(sql, (userid,))
            result = cursor.fetchone()
            
            if result:
                UserOBJ.Name = result['Name']
                UserOBJ.Username = result['Username']
                UserOBJ.Image = result['Image']
                UserOBJ.InterestList = parse_json_list(result['InterestList'])
                UserOBJ.ExtendedInterestList = parse_json_list(result['Extended Interests'])
                UserOBJ.Password = result['PasswordHash']
                UserOBJ.Location = result['Location']
                UserOBJ.myEventIDArr = (parse_json_list(result['EventsList']))
                print(result['EventsList'])
                print(f"User data retrieved successfully for UserID: {userid}")
            else:
                print(f"No user found with UserID: {userid}")

    except pymysql.MySQLError as e:
        print(f"Database error: {e.args[1]} (Error Code: {e.args[0]})")
        return []
    finally:
        if connection:
            connection.close()

def fill_event(EventOBJ):
    Eventid = EventOBJ.EventID
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute("USE `UserManagement`;")
            cursor.execute("""
                SELECT `EventName`, `EventDate`, `EventDescription`, `Location`,`Tags`
                FROM `Events` 
                WHERE `EventID` = %s
                """ % Eventid)
            result = cursor.fetchone()
            
            if result:
                EventOBJ.EventName = result['EventName']
                EventOBJ.EventDescription = result['EventDescription']
                EventOBJ.EventDate = result['EventDate']
                EventOBJ.Tags = parse_json_list(result['Tags'])
                EventOBJ.Location = result['Location']
                print(f"Event data retrieved successfully for UserID: {Eventid}")
            else:
                print(f"No event found with EventID: {Eventid}")

    except pymysql.MySQLError as e:
        print(f"Database error: {e.args[1]} (Error Code: {e.args[0]})")
        return []
    finally:
        if connection:
            connection.close()

# Function to add a user to the Users table
def fill_user_friends(UserOBJ):
    FriendIDs = []
    userid = UserOBJ.UserID
    try:
        connection = get_connection()
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            cursor.execute("USE `UserManagement`;")
            sql = """
            SELECT `mutuals`
            FROM `Users` 
            WHERE `UserID` = %s
            """
            cursor.execute(sql, (userid,))
            result = cursor.fetchall()
            #print('mut', result['mutuals'])

    except pymysql.MySQLError as e:
        print(f"Database error: {e.args[1]} (Error Code: {e.args[0]})")
        return None
    finally:
        if connection:
            connection.close()
    
    for n in result:
        try:
            text = n['mutuals']
            text = text[1:-1]
            print('text', '<<<finduseridinput')
            FriendIDs.append(find_userid(text))
        except pymysql.MySQLError as e:
            continue
    UserOBJ.UserFriendsList = parse_json_list(FriendIDs)
    return



def fill_event(EventOBJ):
    print(EventOBJ.EventID,' >>>>>>>>>>>>>>>>>')
    EventID = EventOBJ.EventID
    print(EventID, 'bjkslchuoiuwcijwjcp')
    try:
        connection = get_connection()
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            cursor.execute("USE `UserManagement`;")
            cursor.execute("""
            SELECT `EventName`, `EventDate`, `EventDescription`, `Location`, `Tags`
            FROM `Events` 
            WHERE `EventID` = %s
            """, (EventID,))
            result = cursor.fetchall()
            print(result)
            if result:
                EventOBJ.EventName = result[0]['EventName']
                EventOBJ.EventTags = parse_json_list(result[0]['Tags'])
                EventOBJ.EventDescription = result[0]['EventDescription']
                EventOBJ.EventDate = result[0]['EventDate']
                EventOBJ.Location = result[0]['Location']
                print(f"Event data retrieved successfully for EventID: {EventID}")
            else:
                print(f"No event found for EventID: {EventID}")
            #print('mut', result['mutuals'])
            return

    except pymysql.MySQLError as e:
        print(f"Database error: {e.args[1]} (Error Code: {e.args[0]})")
        return None
    finally:
        if connection:
            connection.close()



if __name__ == "__main__":
    # Add a user (example)
    newUser = User(83)
    newUser.fill_user()
    newUser.fill_user_friends()
    #numbers = [int(x) for x in newUser.myEventIDArr]
    #newEvent = Event(['coco'], numbers[0])
    #fill_event(newEvent)
    #print(newEvent.EventName, newEvent.EventDate, newEvent.EventDescription, newEvent.KAttendeeArr)