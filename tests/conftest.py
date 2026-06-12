import pytest

from fastapi.testclient import TestClient

from main import app

from database.connection import get_db
from database.models import BookModel

from tests.test_database import (
    TestingSessionLocal
)


def override_get_db():

    db = TestingSessionLocal()

    try:
        yield db

    finally:
        db.close()


app.dependency_overrides[
    get_db
] = override_get_db


client = TestClient(app)


@pytest.fixture
def test_book():

    db = TestingSessionLocal()

    book = BookModel(
        title="Test Book",
        author="Prem",
        price=100.0,
        year=2025
    )

    db.add(book)
    db.commit()
    db.refresh(book)

    yield book

    # Cleanup after test
    db.delete(book)
    db.commit()

    db.close()