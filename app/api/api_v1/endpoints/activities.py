# app/api/api_v1/endpoints/activities.py
from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from .... import schemas, crud
from ...deps import get_db, get_current_user

router = APIRouter()

@router.post("/", response_model=schemas.Actividad)
def create_actividad(actividad: schemas.ActividadCreate, db: Session = Depends(get_db), current_user: schemas.Usuario = Depends(get_current_user)):
    return crud.create_actividad(db=db, actividad=actividad, usuario_id=current_user.id)

@router.get("/", response_model=List[schemas.Actividad])
def read_actividades(skip: int = 0, limit: int = 10, db: Session = Depends(get_db), current_user: schemas.Usuario = Depends(get_current_user)):
    actividades = crud.get_actividades(db, usuario_id=current_user.id, skip=skip, limit=limit)
    return actividades
