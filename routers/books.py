from datetime import datetime

from fastapi import APIRouter, HTTPException

from schemas.book import Book
from database.connection import get_connection

current_year = datetime.now().year

router = APIRouter(
    prefix="/books",
    tags=["Books"]
)

@router.get("/")
def get_books():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
    SELECT * FROM books
    """)

    rows = cursor.fetchall()

    connection.close()

    books = []

    for row in rows:
        books.append({
            "id": row[0],
            "title": row[1],
            "author": row[2],
            "price": row[3],
            "year": row[4]
        })

    return books

@router.get("/{book_id}")
def get_book(book_id: int):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
    SELECT * FROM books
    WHERE id = ?
    """, (book_id,))

    row = cursor.fetchone()

    connection.close()

    if row:
        return {
            "id": row[0],
            "title": row[1],
            "author": row[2],
            "price": row[3],
            "year": row[4]
        }

    raise HTTPException(
        status_code=404,
        detail="Book not found"
    )

@router.post("/")
def create_book(book: Book):

    if book.year > current_year:
        return {
            "message": "Invalid publication year"
        }

    connection = get_connection()
    cursor = connection.cursor()

    # Check if ID already exists
    cursor.execute(
        """
        SELECT * FROM books
        WHERE id = ?
        """,
        (book.id,)
    )

    existing_book = cursor.fetchone()

    if existing_book:
        connection.close()

        return {
            "message": "Book ID already exists"
        }

    cursor.execute(
        """
        INSERT INTO books
        (id, title, author, price, year)
        VALUES (?, ?, ?, ?, ?)
        """,
        (
            book.id,
            book.title,
            book.author,
            book.price,
            book.year
        )
    )

    connection.commit()
    connection.close()

    return {
        "message": "Book added successfully",
        "book": book
    }

@router.put("/{book_id}")
def update_book(book_id: int, updated_book: Book):

    connection = get_connection()
    cursor = connection.cursor()

    # Check whether book exists
    cursor.execute(
        """
        SELECT * FROM books
        WHERE id = ?
        """,
        (book_id,)
    )

    existing_book = cursor.fetchone()

    if not existing_book:
        connection.close()

        return {
            "message": "Book not found"
        }

    cursor.execute(
        """
        UPDATE books
        SET title = ?,
            author = ?,
            price = ?,
            year = ?
        WHERE id = ?
        """,
        (
            updated_book.title,
            updated_book.author,
            updated_book.price,
            updated_book.year,
            book_id
        )
    )

    connection.commit()
    connection.close()

    return {
        "message": "Book updated successfully",
        "book_id": book_id
    }

@router.delete("/{book_id}")
def delete_book(book_id: int):

    connection = get_connection()
    cursor = connection.cursor()

    # Check whether book exists
    cursor.execute(
        """
        SELECT * FROM books
        WHERE id = ?
        """,
        (book_id,)
    )

    existing_book = cursor.fetchone()

    if not existing_book:
        connection.close()

        return {
            "message": "Book not found"
        }

    cursor.execute(
        """
        DELETE FROM books
        WHERE id = ?
        """,
        (book_id,)
    )

    connection.commit()
    connection.close()

    return {
        "message": "Book deleted successfully",
        "book_id": book_id
    }