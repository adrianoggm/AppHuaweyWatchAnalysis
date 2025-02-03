# app/utils/huawei_api.py
import requests
from ..core.config import settings

TOKEN_URL = "https://oauth-login.cloud.huawei.com/oauth2/v3/token"
DATA_API_URL = "https://api-mifit.huawei.com/healthdata/v1/data"

def obtener_token_autorizacion(codigo_autorizacion: str) -> dict:
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

def obtener_datos_salud(token_acceso: str) -> dict:
    headers = {
        "Authorization": f"Bearer {token_acceso}",
        "Content-Type": "application/json",
    }
    params = {
        # Parámetros específicos según la API de Huawei
        "startTime": "20250101",
        "endTime": "20250131",
        # Añade otros parámetros según la documentación de Huawei Health API
    }
    response = requests.get(DATA_API_URL, headers=headers, params=params)
    response.raise_for_status()
    return response.json()
