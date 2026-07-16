from typing import Generic, Type, TypeVar, List, Optional
from sqlalchemy.orm import Session
from app.database.base import Base

ModelType = TypeVar("ModelType", bound=Base)


class BaseRepository(Generic[ModelType]):

    def __init__(self, model: Type[ModelType]):
        self.model = model

    def get_all(self, db: Session) -> List[ModelType]:
        return db.query(self.model).all()

    def get_by_id(self, db: Session, id_val) -> Optional[ModelType]:
        return db.query(self.model).filter(
            self.model.id == id_val
        ).first()

    def create(self, db: Session, obj: ModelType) -> ModelType:
        db.add(obj)
        db.flush()
        db.refresh(obj)
        return obj

    def delete(self, db: Session, obj: ModelType) -> None:
        db.delete(obj)
        db.flush()
