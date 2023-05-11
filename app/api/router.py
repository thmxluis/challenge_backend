from fastapi import APIRouter
from api.v1.services import router as service_router
from api.v1.packages import router as package_router

api_router = APIRouter()

api_router.include_router(service_router, prefix="/v1/services", tags=["services"])
api_router.include_router(package_router, prefix="/v1/packages", tags=["packages"])