from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.connection import get_db

from services.search_service import (
    search_by_title,
    search_by_author,
    search_by_price,
    search_by_year
)

router = APIRouter(
    prefix="/search",
    tags=["Search"]
)


@router.get("/title/{book_title}")
def get_books_by_title(
    book_title: str,
    db: Session = Depends(get_db)
):
    return search_by_title(book_title, db)


@router.get("/author/{author_name}")
def get_books_by_author(
    author_name: str,
    db: Session = Depends(get_db)
):
    return search_by_author(author_name, db)


@router.get("/price/{book_price}")
def get_books_by_price(
    book_price: float,
    db: Session = Depends(get_db)
):
    return search_by_price(book_price, db)


@router.get("/year/{year}")
def get_books_by_year(
    year: int,
    db: Session = Depends(get_db)
):
    return search_by_year(year, db)