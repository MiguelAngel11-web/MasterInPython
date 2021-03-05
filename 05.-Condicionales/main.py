"""
#Condicional IF
Si se cumple está condición :
    Ejecutrar instrcciones
Sino
    Ejecutar instrucciones

if condición:
    instrucciones
else:
    otras instrucciones

#Operadores de comparación
== igual
!= diferente de 
< menor que
> mayor que
<= menor o igual que
>= mayor o igual que

#Operadores logicos
and y
or o
! negación
not no

"""

#Ejemplo 1
print("########### Ejemplo 1 #############")

#color = "verde"
color = input("¿Cual es mi color favorito?")

if color == "rojo":
    print("¡Enhorabuena!")
    print("El color es ROJO")
else:
    print("El color no es correcto")

#Ejemplo 2
print("\n########### Ejemplo 2 #############")

anio = input("¿Que año es?")
anio = int(anio)

if anio >= 2021:
    print("Estamos en 2021")
else:
    print("Es un año diferente a 2021")

#Ejemplo 3
print("\n########### Ejemplo 3 #############")
#nombre = int(input("Dime tu nombre: "))
nombre = input("Dime tu nombre: ")
ciudad = input("Dime tu ciudad: ")
edad = int(input("Dime tu edad: ")) #Numero entero

mayoria_edad = 18

if edad >= mayoria_edad:
    #instruccioness
    print(f"{nombre} SI es mayor edad")

    if ciudad != "Mexico":
        print(f"{nombre} es Mexicano y de {ciudad}")
    else:
        print(f"{nombre} NO es Mexicano")
    

else:
    print(f"{nombre} NO es mayor de edad")

#Ejemplo 4
print("\n########### Ejemplo 4 #############")

dia = int(input("Intruduce el número del día de la semana: "))

"""
if dia == 1:
    print("Es lunes")
else:
    if dia == 2:
        print("Es martes")
    else:
        if dia == 3:
            print("Es miercoles")
        else:
            if dia == 4:
                print("Es jueves")
            else:
                if dia == 5:
                    print("Es viernes")
                else:
                    print("Es fin de semana")
"""

if dia == 1:
    print("Es lunes")
elif dia == 2:
    print("Es martes")
elif dia == 3:
    print("Es miércoles")
elif dia == 4:
    print("Es jueves")
elif dia == 5:
    print("Es viernes")
else:
    print("Es fin de semana")

#Ejemplo 5
print("\n########### Ejemplo 5 #############")

edad_minima = 18

edad_maxima = 65

edad_oficial = int(input("¿Estas en edad de trabajar?. Introduce tu edad: "))

if edad_oficial >= 18 and edad_oficial <= 65:
    print("Está en edad de trabajar!!!")
else:
    print("No está en edad de trabajar")

#Ejemplo 6
print("\n########### Ejemplo 6 #############")

pais = "Austraila"

if pais == "Mexico" or pais == "España" or pais == "Colombia":
    print(f"{pais} es un país habla hispana")
else:
    print(f"{pais} NO es un país habla hispana")

#Ejemplo 7
print("\n########### Ejemplo 7 #############")

pais = "España"

if not (pais == "Mexico" or pais == "España" or pais == "Colombia"):
    print(f"{pais} NO es un país habla hispana")
else:
    print(f"{pais} SI es un país habla hispana")

#Ejemplo 8
print("\n########### Ejemplo 8 #############")

pais = "España"

if pais != "Mexico" and pais != "España" and pais != "Colombia":
    print(f"{pais} NO es un país habla hispana")
else:
    print(f"{pais} SI es un país habla hispana")

    



