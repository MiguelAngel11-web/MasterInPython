from io import open
#Agregamos esta libreria para la ruta absoluta
import pathlib
#Para copiar, renombrar y eleminar archivos
import shutil 

#Abrir archvio

"""
De esta forma te mostrara un error y note abrira el archivo 
archivo = open("14.-Sitema-archivos/fichero_texto.txt","a+") 
En cambio si hacemos lo siguiente te creara el archivo
archivo = open("fichero_texto.txt","a+") 
"""

#Hay una forma para que siempre te cree el archivo, sea la forma que este
#esto es con una ruta absoluta del archivo que queremos acceder.
#Lo ponemos en str ya que originalmente nos lo trae como WindowsPath
#Lo que ocasiona un error de concatenación
ruta = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
archivo = open(ruta,"a+")

#Escirbir dentro del archivo abierto
archivo.write("****Soy un texto metido desde Python****\n")

#Cerrar artchivo
archivo.close()

#Leer archivo r=read
archivo_lectura = open(ruta,"r")
#Leer contenido 
#contendio = archivo_lectura.read()

#Sacar todo el contenido
#print(contendio)
#Sacar caracter por caracter
""" for elemento in contendio:
    print(elemento) """
#Leer linea por linea, leer contenido y guardarlo en lista.
# Esta lee una sola linea: lista = archivo_lectura.readline()
lista = archivo_lectura.readlines()#para todas las lineas

for elemento in lista:
    #if not elemento.isnumeric():
    lista_frase = elemento.split()#Para crear una lista con los elementos de cada linea
    print("Hola:",lista_frase)
    #print("- " +  elemento)
    #elemento.center(100) Para centrar el string, ela rgumento sería el espacio que quiseramos para centrar

archivo_lectura.close()

#Copiar archivo
#ruta_nueva = str(pathlib.Path().absolute()) + "/fichero_copiado.txt"
#Con una ruta alternativa
#ruta_alternativa = "../07.-Ejercicios/texto.txt"
#También la podemos hacer con la ruta absoluta
#ruta_alternativa = str(pathlib.Path().absolute()) + "/../07.-Ejercicios/texto-alternativo.txt"
#shutil.copyfile(ruta,ruta_nueva)
#shutil.copyfile(ruta,ruta_alternativa)

#Mover archivos
""" ruta_nueva = str(pathlib.Path().absolute()) + "/fichero_copiado_NUEVO.txt"
shutil.move(ruta,ruta_nueva) """

#Eliminar archivos
""" import os
ruta_nueva = str(pathlib.Path().absolute()) + "/fichero_copiado_NUEVO.txt"
os.remove(ruta_nueva) """

#Comprobar si existe un dierectorio
import  os.path

#print(os.path.abspath("./"))
#También podemos acceder a la ruta anterior
#print(os.path.abspath("../"))

ruta_comprobar = os.path.abspath("./") + "/fichero_texto.txt"
#También lo podemos hacer con ruta relativa
ruta_comprobar_relativa = "./fichero_texto.txt"

if os.path.isfile(ruta_comprobar_relativa):
    print("El archivo existe")
else:
    print("El archivo no existe")




