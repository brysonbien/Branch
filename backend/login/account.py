import pymysql
from ..config import DB_PASSWORD

# Database connection parameters
timeout = 10
connection = pymysql.connect(
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
def add_user(username, image, interest_list, instagram_token, password_hash):
    try:
        with connection.cursor() as cursor:
            cursor.execute("USE `UserManagement`;")
            sql = """
            INSERT INTO `Users` (`Username`, `Image`, `InterestList`, `InstagramToken`, `PasswordHash`)
            VALUES (%s, %s, %s, %s, %s);
            """
            cursor.execute(sql, (username, image, interest_list, instagram_token, password_hash))
        connection.commit()
        print(f"User '{username}' added to Users table.")
    except pymysql.MySQLError as e:
        print(f"Failed to add user: {e}")

# Function to add an event to the Events table
def add_event(event_name, event_description, event_date, location, tags):
    try:
        with connection.cursor() as cursor:
            cursor.execute("USE `UserManagement`;")
            sql = """
            INSERT INTO `Events` (`EventName`, `EventDescription`, `EventDate`, `Location`, `Tags`)
            VALUES (%s, %s, %s, %s, %s);
            """
            cursor.execute(sql, (event_name, event_description, event_date, location, tags))
        connection.commit()
        print(f"Event '{event_name}' added to Events table.")
    except pymysql.MySQLError as e:
        print(f"Failed to add event: {e}")

# Function to add an attendee to an event
def add_event_attendee(event_id, user_id):
    try:
        with connection.cursor() as cursor:
            cursor.execute("USE `UserManagement`;")
            sql = """
            INSERT INTO `EventAttendees` (`EventID`, `UserID`)
            VALUES (%s, %s);
            """
            cursor.execute(sql, (event_id, user_id))
        connection.commit()
        print(f"User ID '{user_id}' added as attendee to event ID '{event_id}'.")
    except pymysql.MySQLError as e:
        print(f"Failed to add attendee: {e}")

# Function to add a friend connection between users
def add_user_friend(user_id, friend_id):
    try:
        with connection.cursor() as cursor:
            cursor.execute("USE `UserManagement`;")
            sql = """
            INSERT INTO `UserFriends` (`UserID`, `FriendID`)
            VALUES (%s, %s);
            """
            cursor.execute(sql, (user_id, friend_id))
        connection.commit()
        print(f"Friend connection added between user ID '{user_id}' and friend ID '{friend_id}'.")
    except pymysql.MySQLError as e:
        print(f"Failed to add friend connection: {e}")
