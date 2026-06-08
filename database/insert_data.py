import sqlite3

connection = sqlite3.connect("database/books.db")

cursor = connection.cursor()

books = [
    (1, "python Basics", "John", 399.8, 2022),
    (2, "FastAPI Guide", "Jacob", 278.6, 2021),
    (3, "REST API Fundamentals", "Prem", 450.0, 2023),
    (4, "Advanced Python", "Arun", 599.9, 2020),
    (5, "Data Structures", "Kumar", 320.5, 2022),
    (6, "Machine Learning Basics", "Rahul", 799.0, 2024),
    (7, "Deep Learning Guide", "Rahul", 950.0, 2024),
    (8, "SQL for Beginners", "aaruhi", 299.0, 2021),
    (9, "Database Design", "sanjana", 650.0, 2023),
    (10, "Cloud Computing", "Vijay", 850.0, 2022),
    (11, "Docker Essentials", "Vijay", 550.0, 2023),
    (12, "Kubernetes Handbook", "Meena", 1200.0, 2024),
    (13, "Java Programming", "Arun", 499.0, 2020),
    (14, "Microservices Architecture", "Jacob", 999.0, 2024),
    (15, "System Design Interview", "Prem", 1500.0, 2025)
]

cursor.executemany("""
INSERT INTO books
(id, title, author, price, year)
VALUES (?, ?, ?, ?, ?)
""", books)

connection.commit()
connection.close()

print("books inserted successfully!")