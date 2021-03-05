#Para usar los directorios usamos el os
import os

#Crear carpeta
if not os.path.isdir("./micarpeta"):
    os.mkdir("./micarpeta")
else:
    print("Ya existe el directorio")

#Eliminar carpeta
#os.rmdir("./micarpeta")

#Copiar carpetas
import shutil 
ruta_original = "./micarpeta"
ruta_nueva = "./micarpeta_copiada"

#shutil.copytree(ruta_original,ruta_nueva)

#os.rmdir("./micarpeta_copiada")

#Listar lo que tenga mi carpeta
print("Contenido de mi carpeta")

contendio = os.listdir("./micarpeta")

for fichero in contendio:
    print("Fichero: " + fichero)
