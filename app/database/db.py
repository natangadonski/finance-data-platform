import sqlite3
from pathlib import Path

# Define the path where the SQLite database file will be stored.
# If the file does not exist, SQLite will automatically create it.
DB_PATH = Path("data/finance.db")

def get_connection():

    # Establish a connection to the SQLite database file.
    # If the database file does not exist yet, it will be created automatically.
    conn = sqlite3.connect(DB_PATH)

    # Return the database connection so other parts of the application
    # can use it to execute queries (create tables, insert data, etc.)
    return conn