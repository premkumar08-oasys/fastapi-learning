from sqlalchemy import inspect

from database.session import engine

inspector = inspect(engine)

tables = inspector.get_table_names()

print(tables)