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
