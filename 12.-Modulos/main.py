"""  
Modulos: Son funcionalidades ya hechas para reutilizar.
En python hay muchos modulos, que lo puedes consultar aquí:
https://docs.python.org/3/py-modindex.html

Podemos conseguir modulos que ya vienen en el lenguaje.
Modulos en internet, también podemos crear nuestros modulos.
"""
#Importar modulo propio
#import mimodulo Para todo el modulo
#Solo importar una función
#from mimodulo import  holaMundo
#Extraemos todos los métodos de mi modulo
from mimodulo import * 

""" print(mimodulo.holaMundo("Mike"))
print(mimodulo.calculadora(1,2)) """

print(holaMundo("Mike"))

#Modulo de fechas
import datetime

print(datetime.date.today())

fecha_completa = datetime.datetime.now()

print(fecha_completa)
print(fecha_completa.year)
print(fecha_completa.month)
print(fecha_completa.day)

fecha_personalizada = fecha_completa.strftime("%d/%m/%Y, %H:%M:%S")
print(fecha_personalizada)

print(datetime.datetime.now().timestamp())
print(datetime.datetime.now().time())

#Modulo matematicas
import math

print("Raíz cuadrada de 10: ",math.sqrt(10))
print("Número PI: ",float(math.pi))
print("Redondear hacia arriba: ",math.ceil(4.631231241))
print("Redondear hacia abajo: ",math.floor(4.631231241))

#Modulo random
import random

print("Número aletoria entre 1 al 15: ", random.randint(1,15))