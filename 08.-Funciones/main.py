""" 
Palabra reservada:

def nombreDeMiFuncion(parametros):
    #Bloque de código o conjunto de instrucciones.

Si quiero invocarla

nombreDeMiFuncion(mi_parametro)
"""

#Ejemplo 1
print("########## Ejemplo 1 ##########")

def muestraNombre():
    print("Nombre1")
    print("Nombre2")
    print("Nombre3")
    print("Nombre4")
    print("Nombre5")
    print("Nombre6")
    print("\n")
#Invocar función 
#muestraNombre()

#Ejemplo 2 Parametros
print("########## Ejemplo 2 ##########")

def muestraNombre(nombre,edad):
    print(f"Tu nombre es: {nombre}")
    if (edad > 18):
        print("Eres mayor de edad!!")

""" nombre = input("Introduce tu nombre: ")
edad = int(input("Introduce tu edad: ")) """
#muestraNombre(nombre,edad)
#Ejemplo 3 Parametros
print("########## Ejemplo 3 ##########")

def tabla(numero):
    print(f"Tabla de multiplicar del {numero}")
    for contador in range(11):
        operacion = numero *contador
        print(f"{numero} X {contador} = {operacion}")
    print("\n")

""" numero = int(input("Introduce el número de la tabla de multiplicar: "))
tabla(numero) """

#Ejemplo 3.1
print("########## Ejemplo 3.1 ##########")
for numero_tabla in range(1,11):
    tabla(numero_tabla)

#Ejemplo 4 Parametros Opcionales
print("########## Ejemplo 4 ##########")

def getEmpleados(nombre,dni = None):
    print("--Empleado--")
    print(f"Nombre: {nombre}")

    if dni != None:
            print(f"DNI: {dni}")


""" nombre_E = input("Introduce tu nombre:")
numero = int(input("Introduce tu DNI: "))
getEmpleados(nombre_E) """

#Ejemplo 5 Return  
print("########## Ejemplo 5 ##########") 

def saludame(nombre):
    saludo = f"Hola, saludos {nombre}"

    return saludo

""" print(saludame("Mike")) """
#Ejemplo 6   
print("########## Ejemplo 6 ##########") 

def calculadora(num1,num2,basicas = True):
    suma = num1 + num2
    resta = num1 - num2
    multi = num1 * num2
    division = num1 / num2

    cadena = ""

    if basicas != False:
        cadena += "Suma: " + str(suma)
        cadena += "\nResta: " + str(resta)  
    else:
        cadena += "\nMultiplicasión: " + str(multi)
        cadena += "\nDivisión: " + str(division)

    return cadena

print(calculadora(2,3))

#Ejemplo 7   
print("########## Ejemplo 7 ##########") 

def getNombre(nom):
    text = f"El nombre es: {nom}"
    return text

def getApellidos(apellidos):
    text = f"El apellido es: {apellidos}"
    return text

def devuelveTodo(nom,apellidos):
    text = getNombre(nom) + "\n" +  getApellidos(apellidos)
    return text

print(devuelveTodo("Mike", "Castaneda"))

#Ejemplo 8 Función lambda es una función anonima.
#Solo para acciones cortas, se hace todo en una línea.
print("########## Ejemplo 8 ##########") 

dime_el_year = lambda year:f"El año es: {year * 50}"

print (dime_el_year(22022))




