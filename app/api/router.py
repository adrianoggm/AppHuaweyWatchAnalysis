# app/api/router.py
from fastapi import APIRouter
from .api_v1.router import api_router as api_v1_router

api_router = APIRouter()
api_router.include_router(api_v1_router, prefix="/v1")
