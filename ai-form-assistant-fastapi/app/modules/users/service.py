from sqlalchemy.orm import Session
import uuid

from .repository import user_repository
from .model import User


class UserService:

    def get_users(self, db: Session):
        return user_repository.get_all(db)

    def get_user(self, db: Session, user_id: uuid.UUID):
        return user_repository.get_by_id(db, user_id)

    def create_user(self, db: Session, user: User) -> User:
        try:
            db_user = user_repository.create(db, user)
            db.commit()
            return db_user
        except Exception:
            db.rollback()
            raise

    def delete_user(self, db: Session, user: User) -> None:
        try:
            user_repository.delete(db, user)
            db.commit()
        except Exception:
            db.rollback()
            raise


user_service = UserService()