from fastapi import Depends
from fastapi import HTTPException
from fastapi import status

from database.models import UserModel

from dependencies.auth import get_current_user


def require_admin(
    current_user: UserModel = Depends(get_current_user)
):

    if current_user.role != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin access required"
        )

    return current_user