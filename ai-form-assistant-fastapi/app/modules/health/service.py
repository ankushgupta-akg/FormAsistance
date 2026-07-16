from app.core.config import settings


class HealthService:

    def check(self):
        return {
            "status": "healthy",
            "service": settings.APP_NAME
        }


health_service = HealthService()