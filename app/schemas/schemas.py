# app/schemas/schemas.py
from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import datetime

class ActividadBase(BaseModel):
    tipo: str
    pasos: int
    calorias: float
    distancia: float
    fecha: datetime

class ActividadCreate(ActividadBase):
    pass

class Actividad(ActividadBase):
    id: int
    usuario_id: int

    class Config:
        orm_mode = True

class SaludBase(BaseModel):
    frecuencia_cardiaca: float
    calidad_sueno: float
    nivel_estres: float
    fecha: datetime

class SaludCreate(SaludBase):
    pass

class Salud(SaludBase):
    id: int
    usuario_id: int

    class Config:
        orm_mode = True

class UsuarioBase(BaseModel):
    email: EmailStr

class UsuarioCreate(UsuarioBase):
    password: str

class Usuario(UsuarioBase):
    id: int
    preferencias: Optional[str] = None
    actividades: List[Actividad] = []
    salud: List[Salud] = []

    class Config:
        orm_mode = True

class ConsultaBase(BaseModel):
    pregunta: str
    respuesta: str

class ConsultaCreate(ConsultaBase):
    pass

class Consulta(ConsultaBase):
    id: int
    fecha: datetime
    usuario_id: int

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None
