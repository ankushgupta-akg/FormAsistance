"""
Import every SQLAlchemy model here.

Alembic imports this file so Base.metadata
contains all tables.
"""

from app.modules.users.model import User

__all__ = [
    "User",
]