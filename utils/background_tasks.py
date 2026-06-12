from datetime import datetime


def log_book_creation(
    username: str,
    book_title: str
):
    print(
        f"[AUDIT LOG] "
        f"{datetime.now()} | "
        f"User '{username}' "
        f"created book "
        f"'{book_title}'"
    )