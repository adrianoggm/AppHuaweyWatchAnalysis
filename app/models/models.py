# app/models/models.py
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from ..database import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    preferencias = Column(String, nullable=True)

    actividades = relationship("Actividad", back_populates="propietario")
    salud = relationship("Salud", back_populates="propietario")
    consultas = relationship("Consulta", back_populates="propietario")

class Actividad(Base):
    __tablename__ = "actividades"

    id = Column(Integer, primary_key=True, index=True)
    tipo = Column(String, index=True)
    pasos = Column(Integer)
    calorias = Column(Float)
    distancia = Column(Float)
    fecha = Column(DateTime, default=datetime.utcnow)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))

    propietario = relationship("Usuario", back_populates="actividades")

class Salud(Base):
    __tablename__ = "salud"

    id = Column(Integer, primary_key=True, index=True)
    frecuencia_cardiaca = Column(Float)
    calidad_sueno = Column(Float)
    nivel_estres = Column(Float)
    fecha = Column(DateTime, default=datetime.utcnow)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))

    propietario = relationship("Usuario", back_populates="salud")

class Consulta(Base):
    __tablename__ = "consultas"

    id = Column(Integer, primary_key=True, index=True)
    pregunta = Column(String, nullable=False)
    respuesta = Column(String, nullable=False)
    fecha = Column(DateTime, default=datetime.utcnow)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))

    propietario = relationship("Usuario", back_populates="consultas")
