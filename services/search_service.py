from sqlalchemy.orm import Session

from database.models import BookModel


def search_by_title(book_title: str, db: Session):

    return (
        db.query(BookModel)
        .filter(BookModel.title.ilike(f"%{book_title}%"))
        .all()
    )


def search_by_author(author_name: str, db: Session):

    return (
        db.query(BookModel)
        .filter(BookModel.author.ilike(f"%{author_name}%"))
        .all()
    )


def search_by_price(book_price: float, db: Session):

    books = (
        db.query(BookModel)
        .filter(BookModel.price == book_price)
        .all()
    )

    if not books:
        return {"message": "No books found"}

    return books


def search_by_year(year: int, db: Session):

    return (
        db.query(BookModel)
        .filter(BookModel.year == year)
        .all()
    )