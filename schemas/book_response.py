from pydantic import BaseModel, ConfigDict


class BookResponse(BaseModel):
    id: int
    title: str
    author: str
    price: float
    year: int

    class Config:
        model_config = ConfigDict(
        from_attributes = True
        )