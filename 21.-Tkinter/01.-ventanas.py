#Tkinter
#Modulo para crear interfaces graficas

import tkinter as tk
import os

class Programa:
    
    def __init__(self):
        super().__init__()
        self.title = "Proyecto Compiladores"
        self.icon = os.path.abspath("./assets/favicon.ico")
        self.icon_alt = "./assets/favicon.ico"
        self.size = "770x470"
        self.resizable = False
    def cargar(self):
        #Crear ventana raíz
        self.ventana = tk.Tk()


        #Titulo de la ventana
        self.ventana.title(self.title)

        #Comproborar si existe un archivo
        #ruta_icono = os.path.abspath(self.icon)

        #if not os.path.lsfile(ruta_icono):
            #Icono de la ventana
            #ventana.iconbitmap(self.icon_alt)


        #Mostrar tecxto en el programa
        #texto = Label(ventana,text = ruta_icono)
        #texto.pack()


        #Segunda opción
        #ventana.iconbitmap(ruta_icono)


        #Cambio en el tamaño de la ventana 
        self.ventana.geometry(self.size)

        #Bloquear el tamaño de la ventana
        if self.resizable:
            self.ventana.resizable(1, 1)#Ancho, alto
        else:
            self.ventana.resizable(0,0)

        


    def addTexto(self,dato):
        texto = tk.Label(self.ventana, text = dato)
        texto.pack()


    def mostrar(self):
        #Arrancar y mostrar la ventana hasta que se cierre
        self.ventana.mainloop()

#Instaciar mi programa
app = Programa()
app.cargar()
app.addTexto("Hola soy mi amorcito <3")
app.mostrar()   
