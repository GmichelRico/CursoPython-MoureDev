### Clasess ###

# las clases son un tipo de estructura de datos que permite agrupar datos 
# y funciones en un solo objeto

class MyEmptyPerson: 
    pass

print(MyEmptyPerson)
print(MyEmptyPerson())


class Person:
    def __init__ (self, name, surname, alias="Sin alias"):
        self.full_name = f"{name} {surname}, ({alias})"
        #Asi creamos una propiedad privada
        self.__name = name
        self.__surname = surname


    def walk(self):
        print("Estoy caminando")    


my_person = Person("Gerardo", "Michel")


print(my_person.full_name)



my_person.walk()
my_person.full_name = "Hector de Léon"
print(my_person.full_name)

my_other_person = Person("Juan", "Perez", "El chido")
my_other_person.walk()
my_other_person.full_name = "Juan pablo Rico"
print(my_other_person.full_name)

