# app/main.py
from fastapi import FastAPI
from .api.router import api_router
from .core.config import settings
from fastapi.middleware.cors import CORSMiddleware
from .core.logger import setup_logging

# Configurar el logger
setup_logging()

app = FastAPI(
    title=settings.PROJECT_NAME,
    description=settings.PROJECT_DESCRIPTION,
    version=settings.PROJECT_VERSION,
)

# Configurar CORS
origins = [
    "http://localhost:4200",  # Dirección del frontend Angular
    # Añade otros orígenes si es necesario
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir routers
app.include_router(api_router, prefix=settings.API_V1_STR)