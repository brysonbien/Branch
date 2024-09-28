import os
import pymysql
#update_user()
#implement user-pass, mutuals

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
def add_user(username, image, interest_list, password_hash):
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute("USE `UserManagement`;")
            sql = """
            INSERT INTO `Users` (`Username`, `Image`, `InterestList`, `PasswordHash`)
            VALUES (%s, %s, %s, %s, %s);
            """
            cursor.execute(sql, (username, image, interest_list, password_hash))
        connection.commit()
        print(f"User '{username}' added to Users table.")
    except pymysql.MySQLError as e:
        print(f"Failed to add user: {e.args[1]} (Error Code: {e.args[0]})")
    finally:
        if connection:
            connection.close()

# Function to add an event to the Events table
def add_event(event_name, event_description, event_date, location, tags):
    try:
        connection = get_connection()
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
        print(f"Failed to add event: {e.args[1]} (Error Code: {e.args[0]})")
    finally:
        if connection:
            connection.close()

# Function to add an attendee to an event
def add_event_attendee(event_id, user_id):
    try:
        connection = get_connection()
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
        print(f"Failed to add attendee: {e.args[1]} (Error Code: {e.args[0]})")
    finally:
        if connection:
            connection.close()

# Function to add a friend connection between users
def add_user_friend(user_id, friend_id):
    try:
        connection = get_connection()
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
        print(f"Failed to add friend connection: {e.args[1]} (Error Code: {e.args[0]})")
    finally:
        if connection:
            connection.close()

# Example Usage
if __name__ == "__main__":
    # Add a user (example)
    add_user(
        username="john_doe",
        image=None,  # Use None if there's no image, or provide bytes data for a BLOB
        interest_list='["sports", "coding"]',  # JSON string representation
        password_hash="hashed_password_here"
    )

    # Add an event (example)
    add_event(
        event_name="Hackathon",
        event_description="A fun coding event!",
        event_date="2024-12-15 10:00:00",  # Use 'YYYY-MM-DD HH:MM:SS' format
        location="New York City",
        tags='["coding", "fun"]'  # JSON string representation
    )

    # Add an attendee to an event (example)
    add_event_attendee(
        event_id=1,  # Replace with actual event ID
        user_id=1  # Replace with actual user ID
    )

    # Add a friend connection between two users (example)
    add_user_friend(
        user_id=1,  # Replace with actual user ID
        friend_id=2  # Replace with actual friend ID
    )