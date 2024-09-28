import os
import pymysql

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
def add_user(username, image, interest_list, password_hash, location, mutuals):
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute("USE `UserManagement`;")
            sql = """
            INSERT INTO `Users` (`Username`, `Image`, `InterestList`, `PasswordHash`, `Location`, `mutuals`)
            VALUES (%s, %s, %s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE
            `PasswordHash` = VALUES(`PasswordHash`),
            `Location` = VALUES(`Location`),
            `mutuals` = VALUES(`mutuals`);
            """
            cursor.execute(sql, (username, image, interest_list, password_hash, location, mutuals))
        connection.commit()
        print(f"User '{username}' added/updated in Users table.")
    except pymysql.MySQLError as e:
        print(f"Failed to add user: {e.args[1]} (Error Code: {e.args[0]})")
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
        print(f"Friend connection added between user '{user_id}' and friend '{friend_id}'.")
    except pymysql.MySQLError as e:
        print(f"Failed to add friend connection: {e.args[1]} (Error Code: {e.args[0]})")
    finally:
        if connection:
            connection.close()
