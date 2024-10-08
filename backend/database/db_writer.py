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
    timeout = 10
    connection = pymysql.connect(
    charset="utf8mb4",
    connect_timeout=timeout,
    cursorclass=pymysql.cursors.DictCursor,
    db="defaultdb",
    host="gatech-hackathon-2024-branch-hackgt.h.aivencloud.com",
    password=DB_PASSWORD,
    read_timeout=timeout,
    port=10703,
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
            `EventsList` = VALUES(`EventsList`)
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
    event_list = json.dumps(UserOBJ.myEventIDArr)
    extended_interest_list = json.dumps(interests_recommender.get_interests_recommender(UserOBJ.InterestList))
    UserOBJ.ExtendedInterestList = parse_json_list(extended_interest_list)
    print(extended_interest_list)
    password_hash = UserOBJ.Password
    username = UserOBJ.Username
    image = UserOBJ.Image
    location = UserOBJ.Location
    userid = UserOBJ.UserID
    name = UserOBJ.Name
    
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
                `Extended Interests` = %s,
                `EventsList` = %s,
                `Name` = %s
            WHERE `UserID` = %s;
            """
            print(userid, userid, username, image, interest_list, password_hash, location, extended_interest_list)
            cursor.execute(sql, (username, image, interest_list, password_hash, location, extended_interest_list, event_list, name, userid))
        connection.commit()
        print(f"User '{username}' added/updated in Users table.")
    except pymysql.MySQLError as e:
        print(f"Failed to update user: {e.args[1]} (Error Code: {e.args[0]})")
    finally:
        if connection:
            connection.close()

def add_event(EventOBJ):
    EventName = EventOBJ.EventName
    Description = EventOBJ.EventDescription
    Date = EventOBJ.EventDate
    Location = EventOBJ.Location
    Tags = json.dumps(interests_recommender.find_tags(EventName, Description))

    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute("USE `UserManagement`;")
            sql = """
            INSERT INTO `Events` (`EventName`, `EventDate`, `EventDescription`, `Location`,`Tags`) 
            Values(%s, %s, %s, %s, %s)
            """

            cursor.execute(sql, (EventName, Date, Description, Location, Tags))
            EventOBJ.EventID = eventid = cursor.lastrowid
        connection.commit()
        print(f"Event '{EventName}' added to Events Table with id {eventid}")
    except pymysql.MySQLError as e:
        print(f"Failed to create event: {e.args[1]} (Error Code: {e.args[0]})")
    finally:
        if connection:
            connection.close()


if __name__ == "__main__":
    """# Add a user (example)
    #print(json.dumps(['reading', 'traveling', 'coding', 'fucking']))
    db_reader.create_user('adityasht', 'passs', json.dumps('rebelxhawk'))
    tempuser = User(find_userid('adityasht'))
    tempuser.fill_user()
    number_list = ['15', '0']
    json_result = json.dumps(number_list)
    tempuser.myEventIDArr = json.dumps(number_list)
    tempuser.Name = 'the hulk'
    update_user(tempuser)
    tempuser.Name = 'jahrath'
    tempuser.InterestList = ['refrevre', 'trreveng', 'cewfeg', 'skarevng']
    tempuser.Location = 'Mommyc'"""



    newEvent = Event([])
    newEvent.EventDate = '2024-09-29 10:45:00'
    newEvent.EventDescription = 'Step right up and make a difference! Create solutions for social issues, environmental sustainability, healthcare, and mental health to build a better world for all. The text appears to be a call to action encouraging people to get involved in addressing various societal and global challenges to improve the world.'
    newEvent.EventName = 'Test test etst etst'
    newEvent.Location = 'Mommyc'


    add_event(newEvent)
    """

    tempuser.myEventIDArr.append(newEvent.EventID)
    update_user(tempuser)
    print(tempuser.UserID, tempuser.Username, tempuser.InterestList, tempuser.Password, tempuser.Image, tempuser.ExtendedInterestList, tempuser.Location, tempuser.Name)
    #print(tempuser.myEventIDArr)"""


