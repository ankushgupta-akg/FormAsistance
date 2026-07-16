from fastapi import FastAPI

from app.core.config import settings
from app.routes import register_routes

app = FastAPI(title=settings.APP_NAME)

register_routes(app)