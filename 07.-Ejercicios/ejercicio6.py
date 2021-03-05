""" 

Ejercicio 6.
Mostrar todas las tablas de multiplicar del 1 al 10.
Mostrando el titulo de la tabla y luego multiplicaciones del 1 al 10.

"""
numero_multi = 1

while numero_multi <= 10:
    print(f"##### Tabla del numero {numero_multi} ######")
    for contador in range(1,11):
        print(f"{numero_multi} x {contador} = {numero_multi * contador}")
    numero_multi += 1

""" 

Como lo hizo el Profesor 

for cabecera in range (1,11)
    print("##################")
    print("#### Tabla del numero {cabecera}####")
    print("##################")

    for numero in range (1,11)
        print(f"{numero} x {cabecera} = {numero * cabecera}")

    print("\n")

"""