from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from database.connection import get_db

from schemas.book import Book
from schemas.book_response import BookResponse
from dependencies.auth import get_current_user

from database.models import UserModel
from dependencies.roles import require_admin

from services.book_service import (
    get_all_books,
    get_book_by_id,
    create_new_book,
    update_existing_book,
    delete_existing_book
)

router = APIRouter(
    prefix="/books",
    tags=["Books"]
)


@router.get(
    "/",
    response_model=list[BookResponse]
)
def get_books(
    db: Session = Depends(get_db)
):
    return get_all_books(db)


@router.get(
    "/{book_id}",
    response_model=BookResponse
)
def get_book(
    book_id: int,
    db: Session = Depends(get_db)
):
    return get_book_by_id(book_id, db)


@router.post(
    "/",
    response_model=BookResponse,
    status_code=status.HTTP_201_CREATED
)
def create_book(
    book: Book,
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(require_admin)
):
    print("User ID:", current_user.id)
    print("Username:", current_user.username)
    print("Email:", current_user.email)

    return create_new_book(
        book,
        db
    )

@router.put(
    "/{book_id}",
    response_model=BookResponse
)
def update_book(
    book_id: int,
    updated_book: Book,
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(require_admin)
):
    print("Current User:", current_user)

    return update_existing_book(
        book_id,
        updated_book,
        db
    )


@router.delete("/{book_id}")
def delete_book(
    book_id: int,
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(require_admin)
):
    print("Current User:", current_user)

    return delete_existing_book(
        book_id,
        db
    )