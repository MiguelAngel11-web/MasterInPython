""" 
Hacer un programa que pida numeros indefinidamente
hasta que matere el numero 111
"""

num_indefinido = int(input("Teclea un número: "))

while(num_indefinido != 111):
    num_indefinido = int(input("Teclea un número: "))
else:
    print(f"Has escogido el número maestro {num_indefinido}")

