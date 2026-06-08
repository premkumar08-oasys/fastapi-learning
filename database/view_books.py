import sqlite3

connection = sqlite3.connect("database/books.db")
cursor = connection.cursor()

cursor.execute("""
UPDATE books
SET title = 'DATABASE TEST'
WHERE id = 1
""")

connection.commit()
connection.close()

print("updated")