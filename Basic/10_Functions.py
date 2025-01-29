### Functions ###

#Las funciones son bloques de codigo que se pueden reutilizar en cualquier parte de nuestro programa.
#Las funciones se definen con la palabra reservada def seguido del nombre de la funcion y parentesis.

#Ejemplo de una funcion que no recibe parametros
def myFunction():
    print("Hola, soy una funcion")

#Para llamar a una funcion, simplemente escribimos su nombre seguido de parentesis.
myFunction()
print("--------------------------------------------")

#Ejemplo de una funcion que recibe parametros
#El tipado en python es dinamico, por lo que no es necesario especificar 
# el tipo de dato que recibe la funcion.
def sumTwoValues(value1, value2):
    print("La suma de los valores es:", value1 + value2)

#Para mandar a llamar a una funcion que recibe parametros, debemos mandar los valores que necesita.
sumTwoValues(5, 10)
sumTwoValues(54754, 71231)
#si mandamos dos cadenas de texto, se concatenan
sumTwoValues("5", "7")
sumTwoValues(1.2, 5.4)
print("--------------------------------------------")

#Ejemplo de una funcion que regresa un valor
def sumTwoValuesAndReturn(value1, value2):
    mySum = value1 + value2 
    return mySum

myResult = sumTwoValuesAndReturn(5, 10)
print("El valor de la suma es:", myResult)
print("--------------------------------------------")

#Ejemplo de una funcion que regresa varios valores
def print_name(name, surname):
    print(f"{name} {surname}")


print_name(surname = "Michel", name = "Gerardo")

#Ejemplo de una funcion que regresa varios valores
def print_name_with_default(name, surname, alias = "Sin alias"):
    print(f"{name} {surname} {alias}")

print_name_with_default("Gerardo", "Michel")
print_name_with_default("Gerardo", "Michel", "Gmichel")


def print_texts(*texts):
    for text in texts:
        print("Convertimos los textos en mayuscula: ",text.upper())

print_texts("Hola", "Mundo", "Python", "Es", "Genial")
