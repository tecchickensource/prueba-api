# Imagen base oficial de Python
FROM python:3.12-slim

# Definir carpeta de trabajo
WORKDIR /app

# Instalar dependencias directamente
RUN pip install --no-cache-dir fastapi uvicorn[standard] pydantic

# Copiar el código fuente
COPY . .

# Exponer el puerto
EXPOSE 8000

# Comando para ejecutar la API
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]