
import sqlite3

conn = sqlite3.connect('database.db')

conn.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        score INTEGER,
        attendance INTEGER
    )
''')

# Insert dummy data
conn.executemany('INSERT INTO students (name, score, attendance) VALUES (?, ?, ?)', [
    ("Ananya Rao", 72, 82),
    ("Karthik Menon", 60, 70),
    ("Lakshmi Devi", 48, 55),
    ("Rohit R", 85, 90),
    ("Deepa Nair", 30, 45)
])

conn.commit()
conn.close()
print("Database and sample data created!")
