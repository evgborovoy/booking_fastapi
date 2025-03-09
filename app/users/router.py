from fastapi import APIRouter, HTTPException

from app.users.auth import get_password_hash
from app.users.schemas import SUserAuth
from app.users.service import UsersDao

router = APIRouter(prefix="/auth", tags=["Auth and users"])


@router.post("/register")
async def register_user(user_data: SUserAuth):
    existing_user = await UsersDao.find_one_or_none(email=user_data.email)
    if existing_user:
        raise HTTPException(status_code=400)
    hashed_password = get_password_hash(user_data.password)
    await UsersDao.create(email=user_data.email, hashed_password=hashed_password)
