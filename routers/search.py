from fastapi import APIRouter

from database.connection import get_connection

router = APIRouter(
    prefix="/search",
    tags=["Search"]
)

@router.get("/title/{book_title}")
def get_books_by_title(book_title: str):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT * FROM books
        WHERE LOWER(title) = LOWER(?)
        """,
        (book_title,)
    )

    rows = cursor.fetchall()

    connection.close()

    return [
        {
            "id": row[0],
            "title": row[1],
            "author": row[2],
            "price": row[3],
            "year": row[4]
        }
        for row in rows
    ]

@router.get("/author/{author_name}")
def get_books_by_author(author_name: str):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT * FROM books
        WHERE LOWER(author) = LOWER(?)
        """,
        (author_name,)
    )

    rows = cursor.fetchall()

    connection.close()

    return [
        {
            "id": row[0],
            "title": row[1],
            "author": row[2],
            "price": row[3],
            "year": row[4]
        }
        for row in rows
    ]

@router.get("/price/{book_price}")
def get_books_by_price(book_price: float):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT * FROM books
        WHERE price = ?
        """,
        (book_price,)
    )

    rows = cursor.fetchall()

    connection.close()

    if not rows:
        return {"message": "No books found"}

    return [
        {
            "id": row[0],
            "title": row[1],
            "author": row[2],
            "price": row[3],
            "year": row[4]
        }
        for row in rows
    ]

@router.get("/year/{year}")
def get_books_by_year(year: int):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT * FROM books
        WHERE year = ?
        """,
        (year,)
    )

    rows = cursor.fetchall()

    connection.close()

    return [
        {
            "id": row[0],
            "title": row[1],
            "author": row[2],
            "price": row[3],
            "year": row[4]
        }
        for row in rows
    ]
