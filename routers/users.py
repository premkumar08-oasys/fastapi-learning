from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from database.connection import get_db
from schemas.user import UserCreate
from schemas.user_response import UserResponse

from fastapi.security import OAuth2PasswordRequestForm
from services.user_service import authenticate_user, create_user
from utils.jwt_handler import create_access_token
from schemas.token import Token

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.post(
    "/register",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED
)
def register_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):

    new_user = create_user(
        user,
        db
    )

    if not new_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already exists"
        )

    return new_user

@router.post(
    "/login",
    response_model=Token
)
def login_user(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):

    authenticated_user = authenticate_user(
        form_data.username,
        form_data.password,
        db
    )

    if not authenticated_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password"
        )

    access_token = create_access_token(
        {
            "sub": authenticated_user.username
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }