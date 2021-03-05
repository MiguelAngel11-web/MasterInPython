"""  
Hacer un programa que tenga una lista de 8 numeros.
y haga lo siguiente:

- Recorrer la lista y mostrarla
- Hacer una función que recorra listas de numeros y devuleva un string
-ordenarla y mostrarla
- Mostrar su longitud
- Buscar algún elemento (que el usuario pida por el teclado)

"""
lista_num = [1,6,7,3,8,4,5,2]
#Punto 2
def getLista():
    res = ""
    for numero in lista_num:
        res += str(numero) + ", "
    
    return res

#Punto 1
print("***Recorrer la lista y mostrarla****")

lista_f = getLista()
print(lista_f)
#Punto 3
print("***Lista ordenada****")
lista_num.sort()
print(f"Lista ordenada: {lista_num}")
#Punto 4
print("***Mostrar su longitud****")
print(f"La longitud es: {len(lista_num)}")
#Punto 5
print("***Buscar algún elemento****")

try:
    search = int(input("Introduce un elemento a buscar [1-8]: "))
    #Validación
    correcto = isinstance(search,int)

    while not correcto or search <=0:
        search = int(input("Introduce un elemento a buscar [1-8]: "))
    else:
        print(f"Has introducido el {search}")


        if search in lista_num:
            print("Numero encontrado")
except:
    print("El número no está en la lista. Lo siento.")






