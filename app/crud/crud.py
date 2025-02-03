# app/crud/crud.py
from sqlalchemy.orm import Session
from .. import models, schemas
from ..core.security import get_password_hash, verify_password

def get_usuario_by_email(db: Session, email: str):
    return db.query(models.Usuario).filter(models.Usuario.email == email).first()

def create_usuario(db: Session, usuario: schemas.UsuarioCreate):
    hashed_password = get_password_hash(usuario.password)
    db_usuario = models.Usuario(email=usuario.email, hashed_password=hashed_password)
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

def authenticate_user(db: Session, email: str, password: str):
    user = get_usuario_by_email(db, email)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

def create_actividad(db: Session, actividad: schemas.ActividadCreate, usuario_id: int):
    db_actividad = models.Actividad(**actividad.dict(), usuario_id=usuario_id)
    db.add(db_actividad)
    db.commit()
    db.refresh(db_actividad)
    return db_actividad

def get_actividades(db: Session, usuario_id: int, skip: int = 0, limit: int = 10):
    return db.query(models.Actividad).filter(models.Actividad.usuario_id == usuario_id).offset(skip).limit(limit).all()

def create_salud(db: Session, salud: schemas.SaludCreate, usuario_id: int):
    db_salud = models.Salud(**salud.dict(), usuario_id=usuario_id)
    db.add(db_salud)
    db.commit()
    db.refresh(db_salud)
    return db_salud

def create_consulta(db: Session, consulta: schemas.ConsultaCreate, usuario_id: int):
    db_consulta = models.Consulta(**consulta.dict(), usuario_id=usuario_id)
    db.add(db_consulta)
    db.commit()
    db.refresh(db_consulta)
    return db_consulta
