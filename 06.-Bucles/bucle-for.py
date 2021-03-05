"""
#For



for varibale in elemento_iterable(LISTA, RANGO, DUPLA, etc)
    BLOQUE DE INSTRUCCIONES

"""

contador = 0
resultado = 0

for contador in range(0,5):
    print("Vooy por el " + str(contador))

    #resultado = resultado + contador
    resultado += contador

print(f"El resultado es {resultado}")

#Ejemplo tablas de multiplicar
print("\n ################# Ejemplo #####################")

numero_usuario = int(input("¿De que número quieres la tabla?: "))

if numero_usuario <1:
    numero_usuario = 1

print(f"### Tabla de multiplicar del número {numero_usuario} ###")

for numero_tabla in range (1,11):
    
    if numero_usuario >= 11:
        print("Número prohibido")
        break

    print(f"{numero_usuario} x {numero_tabla} = {numero_usuario * numero_tabla} ")
else:
    print("Tabla finalizada")