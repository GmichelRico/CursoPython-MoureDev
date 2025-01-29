### Loops ###

myCondition = 0

#El while lo podemos ver como un if infinito
while myCondition < 10: 

    print("Estamos en el numero:", myCondition)
    myCondition += 2
else: #es opcional 
    print("Mi condicion es mayor o igual a 10")

print("La ejecusion continua.")


#creamos otro while

while myCondition < 20:
    myCondition += 1
    if myCondition == 15:
        print("Mi condicion es 5, se detiene la ejecución")
        break #termina el loop, si se cumple esta condicion
    print("Mi condicion es menor o igual que 20:", myCondition)

print("La ejecusión continúa.")


#For Nos sirve para iterar un listado de elementos
myList = [35, 24, 62, 52, 30, 30, 17]

for element in myList: #se repite hasta que se terminen los elementos de la lista
    #Mandamos a imprimir nuestros elementos.
    print("Elemento:", element)


myTuple = (35, 24, "Brasil", "Moure", 35, "Gmichel")
for element in myTuple:
    print("Elemento:", element)

mySet = {"Brais", "Moure", "Gmichel", 35, 24}
for element in mySet:
    print("Elemento:", element)

#Diccionarios guardan elementos donde hay clave y valor
MyDict = {"Nombre": "Gerardo Michel", "Apellido": "Rico", "Edad": 30}

for key in MyDict:
    print("Key:", key, "|", "Valor:", MyDict[key])


for element in MyDict:
    print("Imprme nuestro elemento:", element)
    if element == "Edad":
        break
else: 
    print("El bucle for para diccionario ha terminado")

print("La ejecusión continúa.")