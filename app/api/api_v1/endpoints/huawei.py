from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .... import schemas, crud
from ...deps import get_db, get_current_user
from ....utils import huawei_api

router = APIRouter()

@router.post("/sync", response_model=dict)
def sincronizar_datos(codigo_autorizacion: str, db: Session = Depends(get_db), current_user: schemas.Usuario = Depends(get_current_user)):
    """
    Sincroniza los datos de salud y actividad de Huawei con la base de datos.
    """
    tokens = huawei_api.obtener_token_autorizacion(codigo_autorizacion)
    if "access_token" not in tokens:
        raise HTTPException(status_code=400, detail="Error al obtener el token de acceso")

    datos = huawei_api.obtener_datos_salud(tokens["access_token"], usuario_id=current_user.id)

    # Insertar datos de actividad en la BD
    for actividad in datos.get("actividades", []):
        actividad_create = schemas.ActividadCreate(
            tipo=actividad.get("tipo", "desconocido"),
            pasos=actividad.get("pasos", 0),
            calorias=actividad.get("calorias", 0.0),
            distancia=actividad.get("distancia", 0.0),
            fecha=actividad.get("fecha")
        )
        crud.create_actividad(db=db, actividad=actividad_create, usuario_id=current_user.id)

    # Insertar datos de salud en la BD
    for salud in datos.get("salud", []):
        salud_create = schemas.SaludCreate(
            frecuencia_cardiaca=salud.get("frecuencia_cardiaca", 0.0),
            calidad_sueno=salud.get("calidad_sueno", None),  # Puede ser None si no es hora de sueño
            nivel_estres=salud.get("nivel_estres", 0.0),
            fecha=salud.get("fecha")
        )
        crud.create_salud(db=db, salud=salud_create, usuario_id=current_user.id)

    return {"mensaje": "Datos sincronizados correctamente"}
