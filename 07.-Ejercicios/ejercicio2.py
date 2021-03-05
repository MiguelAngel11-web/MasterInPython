""" 

Ejercicio 2
    -Escribir un script que nos muestre por pantalla 
    todos los numeros pares del 1 al 120

"""
mostrar = str(0)

for numeros in range(1, 121):
    if numeros % 2 == 0:
        mostrar = mostrar + " , " + str(numeros)

print(mostrar)
