# app/api/api_v1/router.py
from fastapi import APIRouter
from .endpoints import auth, activities, health, huawei, consultas

api_router = APIRouter()
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(activities.router, prefix="/activities", tags=["activities"])
api_router.include_router(health.router, prefix="/health", tags=["health"])
api_router.include_router(huawei.router, prefix="/huawei", tags=["huawei"])
api_router.include_router(consultas.router, prefix="/consultas", tags=["consultas"])
