#Crear variables y asignar valores
texto = "Máster en Python"
texto2 = "Mi segunda variable"
numero = 45
decimal = 4.5

#Mostrar variables
print(texto)
print(texto2)
print(numero)
print(decimal)


print("----------------------------------")
#Sustituir valores de algunas variables
numero = 2
decimal = 67.5

print(numero)
print(decimal)

print("----------------------------------")
#Concatenación
nombre = "Mike"
ape = "Castañeda"
#Otra forma de concatenar
web = f"sinweb.com {nombre}"

print(nombre + " " + ape + " - " + web)
print(f"{nombre} {ape} - {web}")
print("Hola me llamo {} {} y mi web es: {}".format(nombre,ape,web))