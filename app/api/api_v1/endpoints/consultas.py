# app/api/api_v1/endpoints/consultas.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ... import schemas, crud
from ..deps import get_db, get_current_user
from ...utils import llm

router = APIRouter()

@router.post("/", response_model=schemas.Consulta)
def crear_consulta(pregunta: str, db: Session = Depends(get_db), current_user: schemas.Usuario = Depends(get_current_user)):
    # Obtener contexto relevante del usuario, por ejemplo, datos de salud
    contexto = "Datos de salud recientes: frecuencia cardíaca promedio de 70 bpm, sueño de 7 horas diarias."

    respuesta = llm.generar_respuesta(pregunta, contexto)

    consulta_create = schemas.ConsultaCreate(
        pregunta=pregunta,
        respuesta=respuesta
    )
    consulta = crud.create_consulta(db=db, consulta=consulta_create, usuario_id=current_user.id)
    return consulta
