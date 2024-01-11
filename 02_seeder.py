import sqlite3

# Create a connection to the SQLite database
conn = sqlite3.connect('database.db')

# Create a cursor object to interact with the database
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        email TEXT NOT NULL
    )
''')


# Insert sample data into the 'users' table
cursor.execute("INSERT INTO users (username, email) VALUES (?, ?)",
               ('user1', 'user1@example.com'))
cursor.execute("INSERT INTO users (username, email) VALUES (?, ?)",
               ('user2', 'user2@example.com'))
cursor.execute("INSERT INTO users (username, email) VALUES (?, ?)",
               ('user3', 'user3@example.com'))

# Commit the changes and close the connection
conn.commit()
conn.close()
