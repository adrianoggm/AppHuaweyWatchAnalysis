# app/api/api_v1/endpoints/health.py

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
# Usamos 4 puntos para subir hasta la raíz del paquete 'app'
from .... import schemas, crud
from ....api.deps import get_db, get_current_user

router = APIRouter()

@router.post("/", response_model=schemas.Salud, status_code=status.HTTP_201_CREATED)
def create_health(
    salud: schemas.SaludCreate,
    db: Session = Depends(get_db),
    current_user: schemas.Usuario = Depends(get_current_user)
):
    """
    Crea un registro de salud para el usuario actual.
    """
    return crud.create_salud(db=db, salud=salud, usuario_id=current_user.id)

@router.get("/", response_model=List[schemas.Salud])
def read_health(
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db),
    current_user: schemas.Usuario = Depends(get_current_user)
):
    """
    Obtiene una lista de registros de salud del usuario actual.
    """
    salud_list = crud.get_salud(db=db, usuario_id=current_user.id, skip=skip, limit=limit)
    return salud_list
