from database.connection import SessionLocal
from sqlalchemy import text

db = SessionLocal()

db.execute(
    text("DROP TABLE users")
)

db.commit()
db.close()

print("Users table deleted successfully")