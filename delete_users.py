from database.connection import SessionLocal
from database.models import UserModel

db = SessionLocal()

user = (
    db.query(UserModel)
    .filter(UserModel.id == 1)
    .first()
)

if user:
    db.delete(user)
    db.commit()
    print("User deleted successfully")
else:
    print("User not found")

db.close()