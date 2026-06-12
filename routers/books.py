from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from database.connection import get_db

from schemas.book import Book
from schemas.book_response import BookResponse
from dependencies.auth import get_current_user

from database.models import UserModel
from dependencies.roles import require_admin

from fastapi import BackgroundTasks

from utils.background_tasks import (
    log_book_creation
)

from services.book_service import (
    get_all_books,
    get_book_by_id,
    create_new_book,
    update_existing_book,
    delete_existing_book
)

from dependencies.auth import (
    get_current_user,
    get_current_admin
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
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db)
):
    return get_all_books(
        db,
        skip,
        limit
    )


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
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(require_admin)
):
    print("Book Created")
    print("User ID:", current_user.id)
    print("Username:", current_user.username)
    print("Email:", current_user.email)
    print("Role:", current_user.role)

    background_tasks.add_task(
    log_book_creation,
    current_user.username,
    book.title
    )

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
    current_admin: UserModel = Depends(require_admin)
):
    print("Current User:", current_admin.username)

    return update_existing_book(
        book_id,
        updated_book,
        db
    )


@router.delete("/{book_id}")
def delete_book(
    book_id: int,
    db: Session = Depends(get_db),
    current_admin: UserModel = Depends(require_admin)
):
    print("Current User:", current_admin.username)

    return delete_existing_book(
        book_id,
        db
    )
