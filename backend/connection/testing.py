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
    cursor.execute("Use UserManagement;")
    # Insert a test user into the Users table
    insert_user_sql = """
    INSERT INTO `Users` (
        `Username`, 
        `Image`, 
        `InterestList`, 
        `InstagramToken`, 
        `PasswordHash`
    ) VALUES (
        %s, %s, %s, %s, %s
    );
    """
    
    # Define the test user data
    test_user_data = (
        'jane_doe', 
        None,  # Use None for NULL
        '["reading", "traveling", "coding"]', 
        'sample_instagram_token', 
        'hashed_password_123'
    )
    
    cursor.execute(insert_user_sql, test_user_data)
    connection.commit()  # Commit the transaction
    print("Test user inserted successfully.")
    
    # Fetch and print the user to confirm insertion
    cursor.execute("SELECT * FROM `Users` WHERE `Username` = 'jane_doe';")
    print(cursor.fetchall())
finally:
    connection.close()