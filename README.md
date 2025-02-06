# Huawey App

Huawey App es una aplicación web que permite a los usuarios sincronizar, visualizar y analizar los datos recogidos por su reloj inteligente Huawei. La aplicación integra un potente backend desarrollado con **FastAPI** y **SQLAlchemy** (utilizando **PostgreSQL** como base de datos) y un frontend en **Angular**. Además, incorpora un Modelo de Lenguaje Grande (LLM) para permitir consultas en lenguaje natural sobre los datos de salud y actividad.

## Características principales

- **Gestión de Usuarios:**  
  Registro e inicio de sesión seguros utilizando JWT para autenticar a los usuarios.

- **Sincronización de Datos:**  
  Permite conectar y extraer datos directamente desde la API de Huawei para obtener información sobre actividad física, salud y patrones de sueño.

- **Visualización y Análisis:**  
  Dashboard interactivo que muestra gráficos y estadísticas sobre los datos recogidos, permitiendo a los usuarios seguir su progreso y obtener insights personalizados.

- **Consultas en Lenguaje Natural:**  
  Los usuarios pueden realizar preguntas en lenguaje natural (por ejemplo, "¿Cómo ha evolucionado mi ritmo cardíaco esta semana?") y recibir respuestas basadas en los datos almacenados, gracias a la integración con un LLM.

- **Automatización de Migraciones:**  
  El backend utiliza un entrypoint personalizado en Docker para ejecutar automáticamente las migraciones y asegurar que la base de datos esté actualizada cada vez que se inicie la aplicación.

## Tecnologías utilizadas

### Backend

- **Python 3.10**
- **FastAPI**
- **SQLAlchemy**
- **Alembic** (para migraciones)
- **PostgreSQL** (como base de datos)
- Integración con APIs de Huawei y LLM (por ejemplo, OpenAI GPT)

### Frontend

- **Angular**
- **Angular Material** (u otro framework UI)

### Contenedores y Orquestación

- **Docker**
- **Docker Compose**


# AppHuaweyWatchAnalysis
 huawei_watch_backend/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py
│   │   ├── security.py
│   │   └── logger.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── models.py
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── schemas.py
│   ├── crud/
│   │   ├── __init__.py
│   │   └── crud.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── deps.py
│   │   ├── api_v1/
│   │   │   ├── __init__.py
│   │   │   ├── endpoints/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── auth.py
│   │   │   │   ├── users.py
│   │   │   │   ├── activities.py
│   │   │   │   ├── health.py
│   │   │   │   ├── huawei.py
│   │   │   │   └── consultas.py
│   │   └── router.py
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   ├── huawei_api.py
│   │   └── llm.py
│   ├── tests/
│   │   ├── __init__.py
│   │   ├── conftest.py
│   │   ├── test_auth.py
│   │   ├── test_users.py
│   │   ├── test_activities.py
│   │   ├── test_health.py
│   │   ├── test_huawei.py
│   │   └── test_consultas.py
│   └── database.py
├── alembic/
│   ├── versions/
│   │   └── <timestamp>_initial_migration.py
│   ├── env.py
│   ├── README
│   └── script.py.mako
├── .env
├── .gitignore
├── requirements.txt
├── requirements-dev.txt
├── README.md
├── Dockerfile
├── docker-compose.yml
└── setup.cfg
