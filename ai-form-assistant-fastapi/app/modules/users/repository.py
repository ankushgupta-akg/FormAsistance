from sqlalchemy.orm import Session
from typing import Optional

from app.common.repositories.base_repository import BaseRepository
from .model import User


class UserRepository(BaseRepository[User]):

    def __init__(self):
        super().__init__(User)

    def get_by_username(self, db: Session, username: str) -> Optional[User]:
        return db.query(self.model).filter(
            self.model.username == username
        ).first()


user_repository = UserRepository()