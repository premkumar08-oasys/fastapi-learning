from sqlalchemy.orm import Session

from database.models import BookModel


def get_books_less_than_price(
    price: float,
    db: Session
):

    return (
        db.query(BookModel)
        .filter(BookModel.price < price)
        .all()
    )


def get_books_greater_than_price(
    price: float,
    db: Session
):

    return (
        db.query(BookModel)
        .filter(BookModel.price > price)
        .all()
    )


def get_books_in_price_range(
    min_price: float,
    max_price: float,
    db: Session
):

    return (
        db.query(BookModel)
        .filter(
            BookModel.price >= min_price,
            BookModel.price <= max_price
        )
        .all()
    )


def get_books_published_after(
    year: int,
    db: Session
):

    return (
        db.query(BookModel)
        .filter(BookModel.year > year)
        .all()
    )


def get_books_published_before(
    year: int,
    db: Session
):

    return (
        db.query(BookModel)
        .filter(BookModel.year < year)
        .all()
    )