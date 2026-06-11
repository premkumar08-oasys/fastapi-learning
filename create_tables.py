from database.session import Base, engine

# VERY IMPORTANT
from database.models import UserModel
from database.models import BookModel

Base.metadata.create_all(bind=engine)

print("Tables created successfully")