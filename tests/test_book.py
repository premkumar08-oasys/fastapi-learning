from tests.conftest import client


def test_get_books():

    response = client.get("/books")

    assert response.status_code == 200


def test_get_book_by_id(test_book):

    response = client.get(
        f"/books/{test_book.id}"
    )

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == test_book.id


def test_get_non_existing_book():

    response = client.get("/books/999")

    assert response.status_code == 404