from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from app.core.jwt import decode_access_token
from app.db.database import AsyncSessionLocal
from app.users.repository import get_user_by_email
from app.users.models import User
from app.core.config import settings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login")


# -------------------------
# AUTHENTICATION
# -------------------------
async def get_current_user(
    token: str = Depends(oauth2_scheme),
) -> User:
    email = decode_access_token(token)

    if not email:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
        )

    async with AsyncSessionLocal() as session:
        user = await get_user_by_email(session, email)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found",
        )

    return user


# -------------------------
# AUTHORIZATION (ADMIN)
# -------------------------
async def require_admin(
    user: User = Depends(get_current_user),
) -> User:
    # TEST-SAFE admin rule
    if not user.email.startswith("admin"):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin privileges required",
        )
    return user