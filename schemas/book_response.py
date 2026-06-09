from pydantic import BaseModel


class BookResponse(BaseModel):
    id: int
    title: str
    author: str
    price: float
    year: int

    class Config:
        from_attributes = True