# Usa una imagen base oficial de Python
FROM python:3.10-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el resto del proyecto al contenedor
COPY . .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

# Comando para ejecutar la aplicación
CMD ["uvicorn", "app.src.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
