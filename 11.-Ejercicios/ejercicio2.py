"""  
Escribir un programa que añada valores a una lista
mientras que su longitud sea menor a 120 y luego mostrar la lista
Plus: usar while y for

"""

lista_aleatoria = []
#Con For
print("***Con For ****")
elemento = input("Elemento a insertar a la lista: ")
lista_aleatoria.append(elemento)

for data in lista_aleatoria:
    if len(lista_aleatoria) <= 120:
        elemento = input("Elemento a insertar a la lista: ")
        if elemento != "-s":
            lista_aleatoria.append(elemento)
        else:
            break


print(lista_aleatoria)

print("***Con While****")
segunda_lista=[]
elemento2 = input("Elemento a insertar a la lista: ")
segunda_lista.append(elemento)

while len(segunda_lista) <= 120:
    elemento2 = input("Elemento a insertar a la lista: ")
    if elemento2 != "-s":
        segunda_lista.append(elemento2)
    else:
        break
print(segunda_lista)