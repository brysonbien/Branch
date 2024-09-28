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
            SELECT `Username`, `Image`, `InterestList`,`PasswordHash`, `Location`, `mutuals`, `Extended Interests`
            FROM `Users` 
            WHERE `UserID` = %s
            """
            cursor.execute(sql, (userid,))
            result = cursor.fetchone()
            
            if result:
                UserOBJ.Username = result['Username']
                UserOBJ.Image = result['Image']
                UserOBJ.InterestList = parse_json_list(result['InterestList'])
                UserOBJ.ExtendedInterestList = parse_json_list(result['Extended Interests'])
                UserOBJ.Password = result['PasswordHash']
                UserOBJ.Location = result['Location']
                print(f"User data retrieved successfully for UserID: {userid}")
            else:
                print(f"No user found with UserID: {userid}")

    except pymysql.MySQLError as e:
        print(f"Database error: {e.args[1]} (Error Code: {e.args[0]})")
    finally:
        if connection:
            connection.close()

    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute("USE `UserManagement`;")
            sql = """
            SELECT `UserID`, `EventID`
            FROM `EventAttendees` 
            WHERE `UserID` = %s
            """
            cursor.execute(sql, (userid,))
            results = cursor.fetchall()
            
            if results:
                print(f"Found {len(results)} events for UserID: {userid}")
                for result in results:
                    UserOBJ.myEventIDArr.append(result)
                    print(f"EventID: {result['EventID']}")
                return results
            else:
                print(f"No events found for UserID: {userid}")
                return []

    except pymysql.MySQLError as e:
        print(f"Database error: {e.args[1]} (Error Code: {e.args[0]})")
        return []
    finally:
        if connection:
            connection.close()

# Function to add a user to the Users table
def fill_user_friends(UserOBJ):
    userid = UserOBJ.UserID
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute("USE `UserManagement`;")
            sql = """
            SELECT `Username`, `Image`, `InterestList`,`PasswordHash`, `Location`, `mutuals`, `Extended Interests`
            FROM `Users` 
            WHERE `UserID` = %s
            """
            cursor.execute(sql, (userid,))
            result = cursor.fetchone()
            
            if result:
                UserOBJ.Username = result['Username']
                UserOBJ.Image = result['Image']
                UserOBJ.InterestList = parse_json_list(result['InterestList'])
                UserOBJ.ExtendedInterestList = parse_json_list(result['Extended Interests'])
                UserOBJ.Password = result['PasswordHash']
                UserOBJ.Location = result['Location']
                print(f"User data retrieved successfully for UserID: {userid}")
            else:
                print(f"No user found with UserID: {userid}")

    except pymysql.MySQLError as e:
        print(f"Database error: {e.args[1]} (Error Code: {e.args[0]})")
    finally:
        if connection:
            connection.close()


if __name__ == "__main__":
    # Add a user (example)
    tempuser = User(1)
    fill_user(tempuser)
    print(tempuser.UserID, tempuser.Username, tempuser.InterestList, tempuser.Password, tempuser.Image, tempuser.ExtendedInterestList, tempuser.Location)
    print(tempuser.myEventIDArr)