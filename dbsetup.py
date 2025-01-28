import sqlite3
conn = sqlite3.connect('useful.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER,
        email TEXT UNIQUE
    )
''')

conn.commit()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS register (
        id text PRIMARY KEY,
        name TEXT NOT NULL,
        type TEXT UNIQUE
    )
''')
conn.commit()
conn.close()


