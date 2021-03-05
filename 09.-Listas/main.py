""" 
Las listas son los array.
Son colecciones o conjuntos de datos/valores, bajo un unico nombre.

Para acceder a ellos podemos usar un indice numerico.

"""

pelicula = "Batman"
#print(pelicula)
#Lista
#Definir lista
peliculas = ["Batman","Spiderman","El seño de los anillo"]
cantantes = list(("Mike","Jennifer Lopez","Juan"))#Aquí se hace con una dupla
#La dupla es una serie de datos que no pueden cambiar y se crea con doble paréntesis
years = list(range(2021,2050))#Podemos crear un rango de numeros
variada = ["Mike",30,98.7560,True,"Texto"]

""" print(peliculas)
print(cantantes)
print(years)
print(variada) """

#Indices
#Acceder a los elementos
print(peliculas[1])#Sacar elemento Spiderman
print(peliculas[-2])#Sacar elemento Spiderman, de forma que se acomodan 
#asi [-3,-2,-1] de nuestra lista peliculas.
#Sublistas
print(cantantes[1:3])#Sacar como en un rango de elementos
print(cantantes[1:])#Sacar elementos apartir de una posición
#Modificar valores en las listas
peliculas[1] = "Frontier"
print(peliculas)

#Añadir elementos a una lista
cantantes.append("Maluma")
cantantes.append("Rauw Alejandro")
print(cantantes)

#Recorrer listas

""" nueva_pelicula = ""
while nueva_pelicula != "parar":
    nueva_pelicula = input("Introduce una nueva pelicula: ")
    if nueva_pelicula != "parar":
        peliculas.append(nueva_pelicula)

print("\n********Listado de peliculas*******")
for pelicula in peliculas:
    print(f"{peliculas.index(pelicula)+1}. {pelicula}") """

#Lista multidimencionales, listas dentro de otras
print("\n ******Listado de contactos *******")
contactos = [
    [
        'Antonio',
        'anto@gmail.com'
    ],
    [
        'Mke',
        'mke@hotmail.com'
    ],
    [
        'Amorcin',
        'amorcin@iloveyou.com'

    ]
]

#print(contactos[1][1])
for contacto in contactos:
    for elemento in contacto:
        if contacto.index(elemento) == 0:
            print("Nombre: " + elemento)
        else:
            print("Correo: " + elemento)
    print("\n")
