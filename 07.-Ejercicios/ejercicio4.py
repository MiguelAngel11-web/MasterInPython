""" 
Ejercicio4.
Pedir dos numeros al usuario y hacer todas las operaciones básicas
de una calculadora y mostrarlo por pantalla.

"""

num1_user = int(input("Introduce un número: "))
num2_user = int(input("Introduce un segundo número: "))

print("######## OPERACIONES DE UNA CALCULADORA #########")
print("Suma:")
print(f"El resultado de la suma es: {num1_user + num2_user}")
print("Resta:")
print(f"El resultado de la resta es: {num1_user - num2_user}")
print("Multiplicación:")
print(f"El resultado de la multiplicación es: {num1_user * num2_user}")
print("División:")
print(f"El resultado de la división es: {num1_user / num2_user}")

