from fastapi import FastAPI
from pydantic import BaseModel



app = FastAPI()

@app.get("/users/")
async def read_users():
    return [{"username": "Rick"}, {"username": "Morty"}]