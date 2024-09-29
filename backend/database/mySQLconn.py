import os
import pymysql

# Read database password from pass.txt file
def get_db_password():
    with open(os.path.join(os.path.dirname(__file__), '..', 'password.txt'), 'r') as f:
        return f.read().strip()

DB_PASSWORD = get_db_password()

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

try:
    cursor = connection.cursor()

    # Create schema
    cursor.execute("CREATE SCHEMA IF NOT EXISTS `UserManagement`;")

    # Use the new schema
    cursor.execute("USE `UserManagement`;")

    # Create Users table
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS `Users` (
            `UserID` INT AUTO_INCREMENT PRIMARY KEY,
            `Username` VARCHAR(50) NOT NULL UNIQUE,
            `Image` BLOB,
            `InterestList` JSON,
            `InstagramToken` VARCHAR(255),
            `PasswordHash` VARCHAR(255) NOT NULL,
            `Location` VARCHAR(50),
            `mutuals` JSON,
            `ExtendedInterestList` JSON,
            `EventsList` JSON,
            `CreatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """
    )

    # Create Events table
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS `Events` (
            `EventID` INT AUTO_INCREMENT PRIMARY KEY,
            `EventName` VARCHAR(100) NOT NULL,
            `EventDescription` TEXT,
            `EventDate` DATETIME,
            `Location` VARCHAR(255),
            `Tags` JSON,
            `Attendees` JSON,
            `CreatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """
    )

    print(cursor.fetchall())
finally:
    connection.close()

