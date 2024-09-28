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

# Function to add a message to the Messages table
def add_message(sender_id, receiver_id, message):
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute("USE `UserManagement`;")
            sql = """
            INSERT INTO `Messages` (`SenderID`, `ReceiverID`, `Message`)
            VALUES (%s, %s, %s);
            """
            cursor.execute(sql, (sender_id, receiver_id, message))
        connection.commit()
        print(f"Message from '{sender_id}' to '{receiver_id}' added.")
    except pymysql.MySQLError as e:
        print(f"Failed to add message: {e.args[1]} (Error Code: {e.args[0]})")
    finally:
        if connection:
            connection.close()

# Function to retrieve a conversation between two users
def get_conversation(user1_id, user2_id):
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute("USE `UserManagement`;")
            sql = """
            SELECT `SenderID`, `ReceiverID`, `Message`, `Timestamp`
            FROM `Messages`
            WHERE (`SenderID` = %s AND `ReceiverID` = %s)
               OR (`SenderID` = %s AND `ReceiverID` = %s)
            ORDER BY `Timestamp`;
            """
            cursor.execute(sql, (user1_id, user2_id, user2_id, user1_id))
            return cursor.fetchall()
    except pymysql.MySQLError as e:
        print(f"Failed to retrieve conversation: {e.args[1]} (Error Code: {e.args[0]})")
        return []
    finally:
        if connection:
            connection.close()
