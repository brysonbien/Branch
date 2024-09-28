import pymysql
from ..config import DB_PASSWORD

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
            `CreatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """
    )

    # Create EventAttendees table
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS `EventAttendees` (
            `EventID` INT,
            `UserID` INT,
            `AttendedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            PRIMARY KEY (`EventID`, `UserID`),
            FOREIGN KEY (`EventID`) REFERENCES `Events`(`EventID`) ON DELETE CASCADE,
            FOREIGN KEY (`UserID`) REFERENCES `Users`(`UserID`) ON DELETE CASCADE
        );
        """
    )

    # Create UserFriends table
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS `UserFriends` (
            `UserID` INT,
            `FriendID` INT,
            `AddedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            PRIMARY KEY (`UserID`, `FriendID`),
            FOREIGN KEY (`UserID`) REFERENCES `Users`(`UserID`) ON DELETE CASCADE,
            FOREIGN KEY (`FriendID`) REFERENCES `Users`(`UserID`) ON DELETE CASCADE
        );
        """
    )
    print(cursor.fetchall())
finally:
    connection.close()
