""" 

#Bucle WHILE
Esctrucutra de control que itera o repite la ejecucción de una serie de instrucciones tantas veces como sea necesario,
hasta que deje de cumplirse la condición

while condición:
    bloque de instrucciones
    actualización del contador

"""

contador = 1

while contador <= 100:
    print(f"Estoy en el número {contador}")
    contador += 1

print("---------------------")
muestrame = str(0)
contador = 1

while contador <= 100:
    muestrame = muestrame + " , " + str(contador)
    contador += 1

print(muestrame)


#Ejemplo tablas de multiplicar
print("\n ################# Ejemplo #####################")

numero_usuario = int(input("¿De que número quieres la tabla?: "))

if numero_usuario <1:
    numero_usuario = 1

print(f"### Tabla de multiplicar del número {numero_usuario} ###")

contador = 1

while contador <= 10:
     print(f"{numero_usuario} x {contador} = {numero_usuario * contador} ")
     contador += 1
else:
    print("Tabla finalizada")