from fastapi import FastAPI

from app.modules.health.router import router as health_router
# from app.modules.auth.routes import router as auth_router
# from app.modules.users.routes import router as users_router
# from app.modules.forms.routes import router as forms_router
# from app.modules.ai.routes import router as ai_router


def register_routes(app: FastAPI) -> None:
    app.include_router(health_router)
    # app.include_router(auth_router)
    # app.include_router(users_router)
    # app.include_router(forms_router)
    # app.include_router(ai_router)