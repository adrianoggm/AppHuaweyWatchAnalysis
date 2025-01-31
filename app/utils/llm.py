# app/utils/llm.py
import openai
from ..core.config import settings

openai.api_key = settings.OPENAI_API_KEY

def generar_respuesta(pregunta: str, contexto: str = "") -> str:
    prompt = f"{contexto}\n\nPregunta: {pregunta}\nRespuesta:"
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",  # O el motor que prefieras
            prompt=prompt,
            max_tokens=150,
            n=1,
            stop=None,
            temperature=0.7,
        )
        respuesta = response.choices[0].text.strip()
        return respuesta
    except Exception as e:
        return "Lo siento, no pude procesar tu solicitud en este momento."
