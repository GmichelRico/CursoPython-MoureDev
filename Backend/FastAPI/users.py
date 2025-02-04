from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


#Entidad de usuarios
class User(BaseModel):
    id: int
    name: str
    surname: str
    age: int

#Lista de usuarios en formato JSON probicional
user_list = [
    User(id=1, name="Rick", surname="Sanchez", age=60),
    User(id=2, name="Morty", surname="Smith", age=14),
    User(id=3, name="Summer", surname="Smith", age=17)
]


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

#Ruta para obtener un usuario en especifico
#PATH parameter
@app.get("/user/{id}")
async def user(id: int):
    return search_user(id)
    
#QUERY parameter
#Ruta para agregar un usuario por query params
@app.get("/userQuery/")
async def user(id: int):
    return search_user(id)
        

def search_user(id: int):
    users = filter(lambda user: user.id == id, user_list)
    try:
        return list(users)[0]
    except:
        return {"error": "No se ha encontrado el usuario"}

#-------------------POST-------------------
#Ruta para agregar un usuario por body
@app.post("/user/")
async def user(user: User):
    if type(search_user(user.id)) == User:
        return {"error": "El usuario ya existe"}
    else:
        user_list.append(user)
        return user

#-------------------PUT-------------------
#Ruta para actualizar un usuario por body
@app.put("/user/")
async def user(user: User):
    found = False

    for index, saved_user in enumerate(user_list):
        if saved_user.id == user.id:
            user_list[index] = user
            found = True
            return user

    if not found:
        return {"error": "No se ha actualizado el usuario"}
    else:
        return user

#-------------------DELETE-------------------
@app.delete("/user/{id}")
async def user(id: int):
    for index, saved_user in enumerate(user_list):
        if saved_user.id == id:
            user_list.pop(index)
            return {"message": "Usuario fue eliminado"}
    return {"error": "No se ha encontrado el usuario"}


#Para iniciar el server de FastAPI ejecutar el siguiente comando
# fastapi dev users:app --reload
