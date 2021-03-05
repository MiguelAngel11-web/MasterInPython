#Tkinter
#Modulo para crear interfaces graficas

from tkinter import *
import os

#Crear ventana raíz
ventana = Tk()

#Titulo de la ventana
ventana.title("Proyecto Compiladores")

#Comproborar si existe un archivo
ruta_icono = os.path.abspath("./assets/favicon.ico")

#Icono de la ventana
ventana.iconbitmap("./assets/favicon.ico")

#Cambio en el tamaño de la ventana 
ventana.geometry("950x600")

#Bloquear el tamaño de la ventana
ventana.resizable(0, 0)

#Arrancar y mostrar la ventana hasta que se cierre
ventana.mainloop()
