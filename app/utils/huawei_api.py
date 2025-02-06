import requests
import random
from datetime import datetime, timedelta
from ..core.config import settings

TOKEN_URL = "https://oauth-login.cloud.huawei.com/oauth2/v3/token"
DATA_API_URL = "https://api-mifit.huawei.com/healthdata/v1/data"

# Variable para activar o desactivar el modo mock
MODO_MOCK = True

def obtener_token_autorizacion(codigo_autorizacion: str) -> dict:
    """Obtiene el token de autorización desde la API de Huawei, o devuelve un token mock si MODO_MOCK está activado."""
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

def generar_datos_mock() -> dict:
    """Genera datos de salud aleatorios simulando la API de Huawei."""
    fecha_inicio = datetime(2025, 1, 1)
    fecha_fin = datetime(2025, 1, 31)
    dias = (fecha_fin - fecha_inicio).days
    
    datos_mock = {
        "steps": [],
        "heart_rate": [],
        "sleep": []
    }
    
    for i in range(dias):
        fecha = fecha_inicio + timedelta(days=i)
        datos_mock["steps"].append({
            "date": fecha.strftime("%Y-%m-%d"),
            "count": random.randint(3000, 15000)
        })
        datos_mock["heart_rate"].append({
            "date": fecha.strftime("%Y-%m-%d"),
            "resting": random.randint(50, 80),
            "peak": random.randint(120, 180)
        })
        datos_mock["sleep"].append({
            "date": fecha.strftime("%Y-%m-%d"),
            "duration": random.randint(300, 600),
            "deep_sleep": random.randint(100, 300),
            "light_sleep": random.randint(100, 300)
        })

    return datos_mock

def obtener_datos_salud(token_acceso: str) -> dict:
    """Obtiene los datos de salud desde la API de Huawei o devuelve datos mock si MODO_MOCK está activado."""
    if MODO_MOCK:
        return generar_datos_mock()

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
