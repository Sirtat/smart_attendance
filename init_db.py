import sqlite3

# Connect or create DB
conn = sqlite3.connect('attendance.db')
c = conn.cursor()

# Create table if not exists
c.execute('''
    CREATE TABLE IF NOT EXISTS attendance (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        date TEXT NOT NULL,
        time TEXT NOT NULL
    )
''')

conn.commit()
conn.close()
print("Database and table created.")
