# app/api/api_v1/endpoints/users.py

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from .... import schemas, crud
from ....api.deps import get_db, get_current_user

router = APIRouter()

@router.get("/me", response_model=schemas.Usuario)
def read_current_user(current_user: schemas.Usuario = Depends(get_current_user)):
    """
    Devuelve los datos del usuario actualmente autenticado.
    """
    return current_user

@router.get("/", response_model=List[schemas.Usuario])
def read_users(
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db)
):
    """
    Devuelve una lista de usuarios.
    Nota: Este endpoint podría estar restringido a administradores.
    """
    users = crud.get_users(db=db, skip=skip, limit=limit)
    return users
