from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db

from .controller import user_controller
from .schemas import UserResponse

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.get(
    "",
    response_model=list[UserResponse]
)
async def get_users(
    db: Session = Depends(get_db)
):
    return user_controller.get_users(db)