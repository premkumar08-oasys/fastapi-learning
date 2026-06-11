from sqlalchemy import inspect
from database.session import engine

inspector = inspect(engine)

columns = inspector.get_columns("users")

print("Users Table Columns:")
print("-" * 25)

for column in columns:
    print(column["name"])