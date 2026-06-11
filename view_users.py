from database.connection import SessionLocal
from database.models import UserModel

db = SessionLocal()

users = db.query(UserModel).all()

for user in users:
    print(
        user.id,
        user.username,
        user.email,
        user.role
    )

db.close()