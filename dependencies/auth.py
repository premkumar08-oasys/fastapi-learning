from fastapi import Depends, HTTPException, status

from sqlalchemy.orm import Session

from fastapi.security import OAuth2PasswordBearer

from database.connection import get_db
from database.models import UserModel

from utils.jwt_handler import verify_access_token

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="users/login"
)


def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):

    username = verify_access_token(
        token
    )

    if username is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token"
        )

    user = (
        db.query(UserModel)
        .filter(UserModel.username == username)
        .first()
    )

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found"
        )

    return user


def get_current_admin(
    current_user: UserModel = Depends(get_current_user)
):

    if current_user.role != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admins only"
        )

    return current_user