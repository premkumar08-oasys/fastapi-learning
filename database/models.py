from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float

from database.session import Base


class BookModel(Base):

    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String)

    author = Column(String)

    price = Column(Float)

    year = Column(Integer)