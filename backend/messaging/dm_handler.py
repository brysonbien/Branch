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
        password=DB_PASSWORD,  # Replace with the actual password
        read_timeout=timeout,
        port=14022,
        user="avnadmin",
        write_timeout=timeout,
    )

# Function to create the messages table
def create_messages_table():
    """Creates a Messages table in the database if not exists."""
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute("USE `UserManagement`;")
            sql = """
            CREATE TABLE IF NOT EXISTS `Messages` (
                `MessageID` INT AUTO_INCREMENT PRIMARY KEY,
                `SenderID` INT,
                `ReceiverID` INT,
                `Message` TEXT,
                `Timestamp` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (`SenderID`) REFERENCES `Users`(`UserID`) ON DELETE CASCADE,
                FOREIGN KEY (`ReceiverID`) REFERENCES `Users`(`UserID`) ON DELETE CASCADE
            );
            """
            cursor.execute(sql)
        connection.commit()
        print("Messages table created or already exists.")
    except pymysql.MySQLError as e:
        print(f"Failed to create messages table: {e.args[1]} (Error Code: {e.args[0]})")
    finally:
        if connection:
            connection.close()

# Function to send a message
def send_message(sender_id, receiver_id, message):
    """Stores a message sent from sender_id to receiver_id."""
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
        print(f"Message from user '{sender_id}' to user '{receiver_id}' stored successfully.")
    except pymysql.MySQLError as e:
        print(f"Failed to send message: {e.args[1]} (Error Code: {e.args[0]})")
    finally:
        if connection:
            connection.close()

# Function to retrieve messages between two users
def get_messages(user1_id, user2_id):
    """Retrieves messages between user1_id and user2_id."""
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute("USE `UserManagement`;")
            sql = """
            SELECT `SenderID`, `ReceiverID`, `Message`, `Timestamp`
            FROM `Messages`
            WHERE (`SenderID` = %s AND `ReceiverID` = %s)
               OR (`SenderID` = %s AND `ReceiverID` = %s)
            ORDER BY `Timestamp` ASC;
            """
            cursor.execute(sql, (user1_id, user2_id, user2_id, user1_id))
            messages = cursor.fetchall()
        return messages
    except pymysql.MySQLError as e:
        print(f"Failed to retrieve messages: {e.args[1]} (Error Code: {e.args[0]})")
        return []
    finally:
        if connection:
            connection.close()
