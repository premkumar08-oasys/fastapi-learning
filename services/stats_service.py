from sqlalchemy.orm import Session

from database.models import BookModel


def get_total_books(db: Session):

    return {
        "total_books": db.query(BookModel).count()
    }


def get_latest_book(db: Session):

    return (
        db.query(BookModel)
        .order_by(BookModel.id.desc())
        .first()
    )


def get_average_price(db: Session):

    books = db.query(BookModel).all()

    if not books:
        return {"average_price": 0}

    average_price = (
        sum(book.price for book in books)
        / len(books)
    )

    return {
        "average_price": round(average_price, 2)
    }


def get_author_count(db: Session):

    books = db.query(BookModel).all()

    authors = {
        book.author.lower()
        for book in books
    }

    return {
        "author_count": len(authors)
    }


def get_most_expensive_book(db: Session):

    return (
        db.query(BookModel)
        .order_by(BookModel.price.desc())
        .first()
    )


def get_least_expensive_book(db: Session):

    return (
        db.query(BookModel)
        .order_by(BookModel.price.asc())
        .first()
    )