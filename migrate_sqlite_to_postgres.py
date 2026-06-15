from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database.models import BookModel, UserModel

# SQLite database
sqlite_engine = create_engine("sqlite:///database/books.db")

# PostgreSQL database
postgres_engine = create_engine(
    "postgresql://book_management_larj_user:bnD2BpIuyn3QoSnolzY58ChwTRTHH2ba@dpg-d8npnmhkh4rs73ff2ipg-a.singapore-postgres.render.com/book_management_larj"
)

SQLiteSession = sessionmaker(bind=sqlite_engine)
PostgresSession = sessionmaker(bind=postgres_engine)

sqlite_db = SQLiteSession()
postgres_db = PostgresSession()

try:
    # Migrate Books
    books = sqlite_db.query(BookModel).all()

    for book in books:
        exists = postgres_db.query(BookModel).filter(
            BookModel.id == book.id
        ).first()

        if not exists:
            postgres_db.add(
                BookModel(
                    id=book.id,
                    title=book.title,
                    author=book.author,
                    price=book.price,
                    year=book.year,
                )
            )

    # Migrate Users
    users = sqlite_db.query(UserModel).all()

    for user in users:
        exists = postgres_db.query(UserModel).filter(
            UserModel.id == user.id
        ).first()

        if not exists:
            postgres_db.add(
                UserModel(
                    id=user.id,
                    username=user.username,
                    email=user.email,
                    password=user.password,
                    role=user.role,
                )
            )

    postgres_db.commit()

    print(f"Migrated {len(books)} books")
    print(f"Migrated {len(users)} users")

except Exception as e:
    postgres_db.rollback()
    print("Migration failed:", e)

finally:
    sqlite_db.close()
    postgres_db.close()