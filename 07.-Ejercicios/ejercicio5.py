""" 

Ejercicio 5.
Hacer un programa que muestre todos los numeros entre
dos numeros que diga el usuario.

"""

num1_user = int(input("Introduce el primero número: "))
num2_user = int(input("Introduce el segundo número: "))

if num1_user < num2_user:
    for contador in range (num1_user, num2_user):
        print(contador)
elif num1_user == num2_user :
    print("Rango no valido")
else:
    for contador in range (num2_user, num1_user):
        print(contador)
