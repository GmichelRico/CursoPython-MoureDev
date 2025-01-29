from fastapi import FastAPI
from pydantic import BaseModel



app = FastAPI()

@app.get("/users/")
async def read_users():
    return [{"username": "Rick"}, {"username": "Morty"}]

@app.get("/users/{user_id}")
async def read_user(user_id: int):
    return {"username": "fakeuser", "user_id": user_id}