from login import Login
from registro import Registro
from notas import  Notas
from  bd import BD
import datetime

class Asistente(BD):

    def __init__(self):
        super().__init__()
        self.res=""
        self.inicio()
    
    def entrar(self):  
            for user in self.res:
                self.name = user[0]
                self.correo = user[1]
                print(self.res)
                print(f"Bienvendio {self.name} has accedido con el correo {self.correo} a las {datetime.datetime.now().time()}\n")
                print("Acciones disponibles\n")
                print("\n-Crear nota\n \n-Mostrar notas\n \n-Eliminar nota\n \n-Salir\n")
                print("-------------------------")
                self.respuesta = input("¿Que quieres hacer hoy?: ")
                self.opcionesNotas
    
    def inicio(self):
        print("Bienvenido a mi aplicación\n")
        print("-------------------------")
        print("\n-Login\n \n-Registro\n")
        print("-------------------------")


        self.respuesta = input("¿Que quieres hacer hoy?: ")

        

        if self.respuesta.lower() == "l" or self.respuesta.lower() == "login":
            self.res = Login.comprobarUser(self)
            if self.res != None:
                self.entrar()
            
        if self.respuesta.lower() == "r" or self.respuesta.lower() == "registro":
            Registro.registrarNuevo(self)

        def opcionesNotas(self,opcion):
            if opcion == "crear" or opcion == "c":
                susefful = Notas.agregarNota(self)
                if susefful != None:
                    self.entrar

