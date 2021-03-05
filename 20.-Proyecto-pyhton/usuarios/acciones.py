import usuarios.usuario as modelo
import notas.acciones

class Acciones:

    def registro(self):
        print("\nOk!!! Vamos a registrate en el sistema...")
        nombre = input("¿Cuál es tu nombre?")
        apellidos = input("¿Cuál es tu apellido?")
        email = input("Introduce tu email: ")
        password = input("Introduce tu password: ")

        usuario = modelo.Usuario(nombre,apellidos,email,password)
        registro = usuario.registrar()

        if registro[0] >= 1:
            print(f"\nPerfecto {registro[1].name} te has registrado con el email {registro[1].email}")
        else:
            print("\nNo te has registrado exitosamente")

    def login(self):
        print("\nVale!!! Identificate en el sistema...")
        try:
            email = input("Introduce tu email: ")
            password = input("Introduce tu password: ")

            usuario = modelo.Usuario('','',email,password)
            login = usuario.identificar()

            if email == login[3]:
                print(f"Bienvenido {login[1]}, te has registrado en el sistema el {login[5]}")
                self.proximasAcciones(login)
        except Exception as e:
            #print(type(e))
            print(type(e).__name__)
            print("Ocurrio un error. Intentalo más tarde.")
    
    def proximasAcciones(self,usuario):
        print(""" 
        Acciones disponibles:
        -Crear notas
        -Mostrar notas
        -Eliminar nota
        -Salir
        """)

        accion = input("¿Qué quieres hacar?: ")

        hazEl = notas.acciones.Acciones()

        if accion.lower() == "crear" or accion.lower() == "c":
            hazEl.crear(usuario)
            self.proximasAcciones(usuario)
        elif accion.lower() == "mostrar" or accion.lower() == "m":
            hazEl.mostrar(usuario)
            self.proximasAcciones(usuario)
        elif accion.lower() == "eliminar" or accion.lower() == "e":
            hazEl.eliminarNota(usuario)
            self.proximasAcciones(usuario)
        elif accion.lower() == "salir" or accion.lower() == "s":
            exit()