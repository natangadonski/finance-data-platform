from .db import get_connection

def create_transactions_table():

    # Open a connection to the SQLite database
    conn = get_connection()

    #Create a cursor object that will be used to execute SQL commands
    cursor = conn.cursor()

    # Execute SQL command to create the transactions table
    # IF NOT EXISTS prevents errors if the table was aready created before
    cursor.execute("""CREATE TABLE IF NOT EXISTS transactions (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   date TEXTO NOT NULL,
                   description TEXT NOT NULL,
                   amount REAL NOT NULL)""")
    
    # Sabe the changes to the database
    conn.commit()

    # Close the database connection to free resources
    conn.close()
