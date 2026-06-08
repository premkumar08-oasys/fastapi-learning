from fastapi import APIRouter

from data.books_data import books

router = APIRouter(
    prefix="/stats",
    tags=["Statistics"]
)

@router.get("/count")
def count_books():
    return {
        "total_books": len(books)
    }

@router.get("/latest")
def latest_book():
    return books[-1]

@router.get("/average-price")
def average_book_price():
    if not books:
        return {"average_price": 0}

    total_price = sum(book["price"] for book in books)
    average_price = total_price / len(books)
    return {"average_price": average_price}

@router.get("/author-count")
def author_count():
    authors = {book["author"].lower() for book in books}
    return {"author_count": len(authors)}

@router.get("/most-expensive")
def most_expensive_book():
    return max(books, key=lambda book: book["price"])
