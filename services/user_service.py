from sqlalchemy.orm import Session

from database.models import UserModel
from schemas.user import UserCreate
from utils.hashing import (
    hash_password,
    verify_password
)


def create_user(
    user: UserCreate,
    db: Session
):

    existing_user = (
        db.query(UserModel)
        .filter(UserModel.email == user.email)
        .first()
    )

    if existing_user:
        return None

    new_user = UserModel(
        username=user.username,
        email=user.email,
        password=hash_password(user.password),
        role=user.role
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


def authenticate_user(
    username: str,
    password: str,
    db: Session
):

    user = (
        db.query(UserModel)
        .filter(UserModel.username == username)
        .first()
    )

    print("Username entered:", username)
    print("User found:", user)

    if not user:
        return None

    print("Stored hash:", user.password)

    result = verify_password(
        password,
        user.password
    )

    print("Password Match:", result)

    if not result:
        return None

    return user