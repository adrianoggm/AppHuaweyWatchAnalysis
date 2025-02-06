import requests
import random
from datetime import datetime, timedelta
from ..core.config import settings

TOKEN_URL = "https://oauth-login.cloud.huawei.com/oauth2/v3/token"
DATA_API_URL = "https://api-mifit.huawei.com/healthdata/v1/data"

MODO_MOCK = True  # Cambia a False cuando tengas acceso a la API real

def obtener_token_autorizacion(codigo_autorizacion: str) -> dict:
    """Obtiene el token de autorización desde la API de Huawei o devuelve un token mock."""
    if MODO_MOCK:
        return {
            "access_token": "mock_access_token",
            "expires_in": 3600,
            "refresh_token": "mock_refresh_token",
            "scope": "mock_scope",
            "token_type": "Bearer"
        }
    
    payload = {
        "grant_type": "authorization_code",
        "client_id": settings.HUAWEI_CLIENT_ID,
        "client_secret": settings.HUAWEI_CLIENT_SECRET,
        "code": codigo_autorizacion,
        "redirect_uri": settings.HUAWEI_REDIRECT_URI,
    }
    response = requests.post(TOKEN_URL, data=payload)
    response.raise_for_status()
    return response.json()

def generar_datos_mock(usuario_id: int) -> dict:
    """Genera datos de salud y actividad por cada hora del día para un usuario."""
    fecha_inicio = datetime(2025, 1, 1)
    fecha_fin = datetime(2025, 1, 31)
    dias = (fecha_fin - fecha_inicio).days

    datos_mock = {
        "actividades": [],
        "salud": []
    }
    
    for i in range(dias):
        for hora in range(24):  # 24 horas por día
            timestamp = fecha_inicio + timedelta(days=i, hours=hora)
            
            # Actividad física (tabla `actividades`)
            pasos = random.randint(0, 500)  # Puede haber horas sin pasos (0)
            calorias = round(random.uniform(5, 60), 2)
            distancia = round(pasos * random.uniform(0.5, 1.5) / 1000, 2)  # km

            datos_mock["actividades"].append({
                "usuario_id": usuario_id,
                "tipo": "caminata" if pasos > 0 else "sedentario",
                "pasos": pasos,
                "calorias": calorias,
                "distancia": distancia,
                "fecha": timestamp.strftime("%Y-%m-%d %H:%M:%S")
            })

            # Datos de salud (tabla `salud`)
            frecuencia_cardiaca = random.randint(50, 130)
            calidad_sueno = round(random.uniform(1, 10), 2) if 22 <= hora or hora <= 6 else None
            nivel_estres = round(random.uniform(1, 100), 2)

            datos_mock["salud"].append({
                "usuario_id": usuario_id,
                "frecuencia_cardiaca": frecuencia_cardiaca,
                "calidad_sueno": calidad_sueno,
                "nivel_estres": nivel_estres,
                "fecha": timestamp.strftime("%Y-%m-%d %H:%M:%S")
            })

    return datos_mock

def obtener_datos_salud(token_acceso: str, usuario_id: int) -> dict:
    """Obtiene los datos de salud desde la API de Huawei o devuelve datos mock."""
    if MODO_MOCK:
        return generar_datos_mock(usuario_id)

    headers = {
        "Authorization": f"Bearer {token_acceso}",
        "Content-Type": "application/json",
    }
    params = {
        "startTime": "20250101",
        "endTime": "20250131",
    }
    response = requests.get(DATA_API_URL, headers=headers, params=params)
    response.raise_for_status()
    return response.json()
