# Dockerfile del backend

# Usar una imagen base oficial de Python
FROM python:3.10-slim

# Instalar netcat (nc) para poder esperar a que la base de datos esté lista
RUN apt-get update && apt-get install -y netcat-openbsd && rm -rf /var/lib/apt/lists/*

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar y instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código de la aplicación y el script de entrada
COPY . .

# Dar permisos de ejecución al script de entrada
RUN chmod +x /app/entrypoint.sh

# Exponer el puerto
EXPOSE 8000

# Usar el script de entrada para inicializar el contenedor y luego ejecutar uvicorn
ENTRYPOINT ["/app/entrypoint.sh"]

# Comando para ejecutar la aplicación
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
