#!/bin/bash
set -e

# Espera a que PostgreSQL esté listo (opcional, pero recomendable)
# Puedes usar alguna herramienta como "wait-for-it" o un simple bucle:
echo "Esperando a que la base de datos esté lista..."
until nc -z db 5432; do
  sleep 1
done
echo "La base de datos está disponible."

# Ejecuta las migraciones con Alembic
echo "Ejecutando migraciones con Alembic..."
python -m alembic upgrade head

# Finalmente, ejecuta el comando que se haya pasado (por ejemplo, iniciar uvicorn)
exec "$@"
