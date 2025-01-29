### Modules ###

# Los modulos son archivos que contienen funciones, clases y variables 
# que pueden ser importadas a otros archivos.
# Para importar un modulo utilizamos la palabra reservada import
import module
module.sumTotal(5, 5, 5)
module.mult(5, 5)


#para usar la funcion utilizamos o podemos acceder atraves de from
from module import sumTotal
sumTotal(5, 5, 5)


#hay modluos que ya vienen con python, como el modulo math
import math

print(math.pi)
print(math.pow(2, 3))
print(math.sqrt(9))

#podemos renombrar el modulo al importarlo
from math import pi as PI_value
print(PI_value)