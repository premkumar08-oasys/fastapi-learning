from database.session import engine
from database.models import BookModel

BookModel.metadata.create_all(bind=engine)

print("ORM Connected Successfully")