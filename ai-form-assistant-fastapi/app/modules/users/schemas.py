from datetime import datetime
import uuid

from pydantic import BaseModel


class UserResponse(BaseModel):
    id: uuid.UUID
    username: str
    full_name: str

    created_at: datetime
    updated_at: datetime

    model_config = {
        "from_attributes": True
    }