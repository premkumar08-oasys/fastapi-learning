from fastapi import APIRouter

from data.books_data import books

router = APIRouter(
    prefix="/filter",
    tags=["Filters"]
)

@router.get("/price-less-than/{price}")
def get_books_less_than(price: float):
    result = []
    for book in books:
        if book["price"] < price:
            result.append(book)
    return result

@router.get("/price-greater-than/{price}")
def get_books_greater_than(price: float):
    result = []
    for book in books:
        if book["price"] > price:
            result.append(book)
    return result
