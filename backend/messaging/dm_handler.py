import pymysql
import os

# Load database password
def get_db_password():
    with open(os.path.join(os.path.dirname(__file__), '..', 'password.txt'), 'r') as f:
        return f.read().strip()

DB_PASSWORD = get_db_password()

# Establish a connection to the database
def get_connection():
    timeout = 10
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

# Save a message to the database
def save_message(sender_id, receiver_id, message):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("USE `UserManagement`;")
            sql = """
            INSERT INTO `Messages` (`SenderID`, `ReceiverID`, `Message`, `Timestamp`)
            VALUES (%s, %s, %s, NOW());
            """
            cursor.execute(sql, (sender_id, receiver_id, message))
        connection.commit()
    finally:
        connection.close()

# Get conversation between two users
def get_conversation(sender_id, receiver_id):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("USE `UserManagement`;")
            sql = """
            SELECT `SenderID`, `ReceiverID`, `Message`, `Timestamp`
            FROM `Messages`
            WHERE (`SenderID` = %s AND `ReceiverID` = %s)
               OR (`SenderID` = %s AND `ReceiverID` = %s)
            ORDER BY `Timestamp` ASC;
            """
            cursor.execute(sql, (sender_id, receiver_id, receiver_id, sender_id))
            return cursor.fetchall()
    finally:
        connection.close()
