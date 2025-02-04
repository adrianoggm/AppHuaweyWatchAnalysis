# app/api/api_v1/endpoints/auth.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ...deps import get_db
from .... import schemas, crud
from ....core.security import create_access_token
from datetime import timedelta
from ....core.config import settings
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter()

@router.post("/token", response_model=schemas.Token)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = crud.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/register", response_model=schemas.Usuario)
def register_user(usuario: schemas.UsuarioCreate, db: Session = Depends(get_db)):
    db_user = crud.get_usuario_by_email(db, email=usuario.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_usuario(db=db, usuario=usuario)
