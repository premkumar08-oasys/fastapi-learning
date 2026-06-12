from datetime import datetime

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from database.models import BookModel
from schemas.book import Book

current_year = datetime.now().year


def get_all_books(
        db: Session,
        skip: int = 0,
        limit: int = 10
):
    return (
        db.query(BookModel)
        .offset(skip)
        .limit(limit)
        .all()        
    )


def get_book_by_id(book_id: int, db: Session):

    book = (
        db.query(BookModel)
        .filter(BookModel.id == book_id)
        .first()
    )

    if not book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Book not found"
        )

    return book


def create_new_book(book: Book, db: Session):

    if book.year > current_year:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid publication year"
        )

    existing_book = (
        db.query(BookModel)
        .filter(BookModel.id == book.id)
        .first()
    )

    if existing_book:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Book ID already exists"
        )

    new_book = BookModel(
        id=book.id,
        title=book.title,
        author=book.author,
        price=book.price,
        year=book.year
    )

    db.add(new_book)
    db.commit()
    db.refresh(new_book)

    return new_book


def update_existing_book(
    book_id: int,
    updated_book: Book,
    db: Session
):

    book = (
        db.query(BookModel)
        .filter(BookModel.id == book_id)
        .first()
    )

    if not book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Book not found"
        )

    book.title = updated_book.title
    book.author = updated_book.author
    book.price = updated_book.price
    book.year = updated_book.year

    db.commit()
    db.refresh(book)

    return book


def delete_existing_book(
    book_id: int,
    db: Session
):

    book = (
        db.query(BookModel)
        .filter(BookModel.id == book_id)
        .first()
    )

    if not book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Book not found"
        )

    db.delete(book)
    db.commit()

    return {
        "message": "Book deleted successfully",
        "book_id": book_id
    }