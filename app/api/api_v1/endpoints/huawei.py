# app/api/api_v1/endpoints/huawei.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .... import schemas, crud
from ...deps import get_db, get_current_user
from ....utils import huawei_api

router = APIRouter()

@router.post("/sync", response_model=dict)
def sincronizar_datos(codigo_autorizacion: str, db: Session = Depends(get_db), current_user: schemas.Usuario = Depends(get_current_user)):
    tokens = huawei_api.obtener_token_autorizacion(codigo_autorizacion)
    if "access_token" not in tokens:
        raise HTTPException(status_code=400, detail="Error al obtener el token de acceso")

    datos_salud = huawei_api.obtener_datos_salud(tokens["access_token"])

    # Procesar y almacenar los datos en la base de datos
    for dato in datos_salud.get("health_data", []):
        salud_create = schemas.SaludCreate(
            frecuencia_cardiaca=dato.get("heart_rate", 0.0),
            calidad_sueno=dato.get("sleep_quality", 0.0),
            nivel_estres=dato.get("stress_level", 0.0),
            fecha=dato.get("timestamp", "2025-01-30T07:30:00Z")
        )
        crud.create_salud(db=db, salud=salud_create, usuario_id=current_user.id)

    return {"mensaje": "Datos sincronizados correctamente"}
