""" 
Hacer un programa que muestre todos los numeros impares
entre dos numero que elija el usuario

"""

num1_user = int(input('Introdusca un número impar: '))
num2_user = int(input('Introdusca un segundo número impar: '))

if num2_user > num1_user:
    for contador in range (num1_user, num2_user):
        if contador % 2 != 0:
            print(contador)
else:
    print('No hay un número impar en los que has digitado')
