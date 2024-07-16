import mysql.connector
from mysql.connector import errorcode

# Database connection configuration
config = {
    'user': 'root',  # Replace with your MySQL username
    'password': '1234',  # Replace with your MySQL password
    'host': '127.0.0.1',
    'raise_on_warnings': True
}

# Path to the SQL file
sql_file_path = r'society_management.sql'  # Use a raw string for the file path

# Read the SQL file
with open(sql_file_path, 'r') as file:
    sql_commands = file.read().split(';')

def create_database(cursor, database_name):
    try:
        cursor.execute(
            f"CREATE DATABASE IF NOT EXISTS {database_name} DEFAULT CHARACTER SET 'utf8mb4'")
    except mysql.connector.Error as err:
        print(f"Failed creating database: {err}")
        exit(1)

def execute_sql_commands(cursor, commands):
    for command in commands:
        if command.strip():
            try:
                cursor.execute(command)
            except mysql.connector.Error as err:
                print(f"Failed executing command: {command}\nError: {err}")

try:
    # Connect to MySQL server
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    
    # Create database
    database_name = 'society_management'
    create_database(cursor, database_name)
    
    # Select the new database
    cnx.database = database_name
    
    # Execute SQL commands from file
    execute_sql_commands(cursor, sql_commands)
    
    # Commit changes
    cnx.commit()
    print("Database created and SQL commands executed successfully.")
    
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
finally:
    cursor.close()
    cnx.close()
