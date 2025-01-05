import sqlite3
import os

# Path to the SQLite database
DB_PATH = 'database.db'

def add_string_to_db(string):
    # Connect to the SQLite database (this will create it if it doesn't exist)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Create the table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS strings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            text TEXT NOT NULL
        )
    ''')

    # Insert the new string
    cursor.execute('INSERT INTO strings (text) VALUES (?)', (string,))

    # Commit changes and close the connection
    conn.commit()
    conn.close()

if __name__ == '__main__':
    string_to_add = os.environ.get('STRING_TO_ADD')
    if string_to_add:
        add_string_to_db(string_to_add)
    else:
        print("No string provided.")
