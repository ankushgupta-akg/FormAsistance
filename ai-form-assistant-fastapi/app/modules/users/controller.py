from sqlalchemy.orm import Session
import uuid

from .service import user_service


class UserController:

    def get_users(self, db: Session):
        return user_service.get_users(db)

    def get_user(self, db: Session, user_id: uuid.UUID):
        return user_service.get_user(db, user_id)


user_controller = UserController()