cantates = ["Juan","JK-CD","Asdef","DASDA","asdfasf"]
numeros = [1,6,3,5,4,2]

#Ordenar
print(numeros)
numeros.sort()
print(numeros)

#Añadir elementos
cantates.append("Añadido")
cantates.insert(1,"David Bisbal")
print(cantates)

#Eliminar elementos
cantates.pop(5)#Por posición
cantates.remove("Juan")#Por elemento de la lista
print(cantates)

#Dar la vuelta a una lista
numeros.reverse()
print(numeros)

# Buscar dentro de una lista
print('JK-CD' in cantates)

#Contar elementos
print(len(cantates))

#Cuantas veces aparece un elemento en la lista
numeros.append(1)
print(numeros.count(1))

#Conseguir indice
print(cantates.index("JK-CD"))

#Unir listas
cantates.extend(numeros)
print(cantates)