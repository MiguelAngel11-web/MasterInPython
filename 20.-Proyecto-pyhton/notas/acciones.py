import  notas.nota as modelo

class Acciones:

    def crear(self,usuario):
        print(f"Ok {usuario[1]} vamos a crear una nueva nota")
        
        titulo = input("Introduce el titulo de tu nota: ")
        descripcion = input("Descripción de tu nota:")

        nota = modelo.Nota(usuario[0],titulo, descripcion)

        guardar = nota.guardar()

        if guardar[0] >= 1:
            print(f"Perfecto has guarado tu nota con el titulo: {nota.titulo}")
        else:
            print(f"No se a guardado la nota {usuario[1]}. Lo siento")

    def mostrar(self,usuario):
        print(f"\nVale {usuario[1]} .Aquí están tus notas")

        nota = modelo.Nota(usuario[0])

        lista_notas = nota.listar()

        for nota in lista_notas:
            print("\n*************************")
            print(nota[2])
            print(nota[3])
            print("*************************")
    def eliminarNota(self,usuario):
        print(f"\nOkey {usuario[1]} borraremos notas.")

        titulo = input("Introduce el tiulo de la nota a borrar: ")

        nota = modelo.Nota(usuario[0],titulo)

        eliminar = nota.eliminar()

        if eliminar[0] >= 1:
            print(f"Hemos borrado la nota: {nota.titulo}")
        else:
            print("No se a borrado la nota. Prueba luego.")