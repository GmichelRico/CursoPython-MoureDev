from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


#Entidad de usuarios
class User(BaseModel):
    name: str
    surname: str
    age: int

user_list = [{"username": "Rick", "surname": "Sanchez", "age": 60}, 
            {"username": "Morty", "surname": "Smith", "age": 14},
            {"username": "Summer", "surname": "Smith", "age": 17}]


#Ruta para obtener los usuarios
@app.get("/usersJson/")
async def usersJson():
    return [{"username": "Rick", "surname": "Sanchez", "age": 60}, 
            {"username": "Morty", "surname": "Smith", "age": 14},
            {"username": "Summer", "surname": "Smith", "age": 17}]


#Ruta para obtener los usuarios en formato JSON
@app.get("/users/")
async def users():
    return user_list

#Para iniciar el server de FastAPI ejecutar el siguiente comando
# fastapi dev users:app --reload
