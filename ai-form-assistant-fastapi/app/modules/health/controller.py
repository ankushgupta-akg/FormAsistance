from .service import health_service


class HealthController:

    def check(self):
        return health_service.check()


health_controller = HealthController()