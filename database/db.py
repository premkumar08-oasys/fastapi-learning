import sqlite3

connection = sqlite3.connect("database/books.db")

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    price REAL NOT NULL,
    year INTEGER NOT NULL           
)
""")

connection.commit()

connection.close()

print("Database and table created successfully.")