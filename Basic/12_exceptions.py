### Exception Handling ###

#El manejo de errores nos ayuda a controlar el flujo de nuestro programa
# cuando algo inesperado sucede, así evitamos que se cierre nuestro sistema

numberOne = 5
numberTwo = 1
#numberTwo = "1"

'''print(5 + "5")'''

# Para evitar que nuestro programa se cierre, podemos hacer una validación
# pero esto solo nos sirve para proteger este caso en específico
'''if type(numberTwo) == int:
    print(numberOne + numberTwo)
else:
    print("No se puede sumar un número con una cadena")'''

# Para manejar errores en Python utilizamos la estructura try/except
try:
    print(numberOne + numberTwo)
    print("No se produjo un error")
except:
    print("Se ha producido un error ")