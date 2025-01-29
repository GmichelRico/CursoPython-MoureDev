# Instala FastAPI: pip install "fastapi[standard]"

#Impportamos FastAPI de fastapi
from fastapi import FastAPI

#Creamos una instancia de FastAPI
app = FastAPI()

# Url local: http://127.0.0.1:8000

@app.get("/")
async def root():
    return "Hola FastAPI!"

# Url local: http://127.0.0.1:8000/url

@app.get("/url")
async def url():
    return {"url": "https://mouredev.com/python"}

# Inicia el server: fastapi dev main.py
# Detener el server: CTRL+C

# Documentación con Swagger: http://127.0.0.1:8000/docs
# Documentación con Redocly: http://127.0.0.1:8000/redoc