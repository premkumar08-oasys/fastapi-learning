from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.connection import get_db

from services.filter_service import (
    get_books_less_than_price,
    get_books_greater_than_price,
    get_books_in_price_range as filter_price_range,
    get_books_published_after,
    get_books_published_before
)

router = APIRouter(
    prefix="/filter",
    tags=["Filters"]
)


@router.get("/price-less-than/{price}")
def get_books_less_than(
    price: float,
    db: Session = Depends(get_db)
):
    return get_books_less_than_price(
        price,
        db
    )


@router.get("/price-greater-than/{price}")
def get_books_greater_than(
    price: float,
    db: Session = Depends(get_db)
):
    return get_books_greater_than_price(
        price,
        db
    )


@router.get("/price-range/{min_price}/{max_price}")
def get_books_in_price_range(
    min_price: float,
    max_price: float,
    db: Session = Depends(get_db)
):
    return get_books_in_price_range(
        min_price,
        max_price,
        db
    )


@router.get("/published-after/{year}")
def get_books_after(
    year: int,
    db: Session = Depends(get_db)
):
    return get_books_published_after(
        year,
        db
    )


@router.get("/published-before/{year}")
def get_books_before(
    year: int,
    db: Session = Depends(get_db)
):
    return get_books_published_before(
        year,
        db
    )