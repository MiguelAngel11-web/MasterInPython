""" 
Ejercicio 3:
Escribir un programa que muestre los cuadrados, de los 60 primeros numeros naturales. Resolver con for y while
"""

#While
contador = 1
resultado = 0

print("############ CON WHILE #############")
while contador <=60:
    resultado = contador * contador
    print(resultado)
    contador += 1

print("############ CON FOR #############")
resultado = 0
for numeros in range(61):
    resultado = numeros * numeros
    print(resultado)