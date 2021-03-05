nom = "Mike Casta"

#funciones generales
print(nom)
print(type(nom))
#Detectar el tipado
comprobar = isinstance(nom,str)

if comprobar:
    print("Esa variable es string")
else:
    print("No es un string")

if not isinstance(nom, float):
    print("No es un número flotante")

#Limpiar espacios
frase = "   mi content     "
print(frase.strip())

#Eliminar variables
year = 2021
print(year)
del year
#print(year)

#Comprobar varibales vacias
texto = "  ff  "
if len(texto) <= 0:
    print("La variables está vacía")
else:
    print("La variable tiene contendio: ", len(texto))
#Encontrar caractares
frase = "La vida es bella"
print(frase.find("vida"))

#Reemplazar palabras en un string
nueva_frase = frase.replace("vida","moto")
print(nueva_frase)

#Mayusculas y minisculas
print(nom)
print(nom.lower())
print(nom.upper())