from fastapi import APIRouter

from .controller import health_controller
from .schemas import HealthResponse

router = APIRouter(
    prefix="/health",
    tags=["Health"]
)


@router.get(
    "",
    response_model=HealthResponse
)
async def health():
    return health_controller.check()