from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.connection import get_db

from services.stats_service import (
    get_total_books,
    get_latest_book,
    get_average_price,
    get_author_count,
    get_most_expensive_book,
    get_least_expensive_book
)

router = APIRouter(
    prefix="/stats",
    tags=["Statistics"]
)


@router.get("/count")
def count_books(
    db: Session = Depends(get_db)
):
    return get_total_books(db)


@router.get("/latest")
def latest_book(
    db: Session = Depends(get_db)
):
    return get_latest_book(db)


@router.get("/average-price")
def average_book_price(
    db: Session = Depends(get_db)
):
    return get_average_price(db)


@router.get("/author-count")
def author_count(
    db: Session = Depends(get_db)
):
    return get_author_count(db)


@router.get("/most-expensive")
def most_expensive_book(
    db: Session = Depends(get_db)
):
    return get_most_expensive_book(db)


@router.get("/least-expensive")
def least_expensive_book(
    db: Session = Depends(get_db)
):
    return get_least_expensive_book(db)