from bd import BD

class Notas(BD):

    def __init__(self):
        super().__init__()
        self.database = BD()
    
    def agregarNota(self):
        titulo = input("Introduce el titulo de la nota: ")
        while TypeError:
            titulo = input("Introduce el titulo de la nota: ")

        contenido = input("Introduce el contendio de la nota: ")
        while TypeError:
            contenido = input("Introduce el contendio de la nota: ")
        
        insert_stmt = (
        "INSERT INTO notas (id, titulo, contenido) "
        "VALUES ('null', %s, %s)")
        data = (titulo, contenido)
      
        self.cursor.execute(insert_stmt,data)

        exito = self.cursor.rowcount

        self.database.commit()

        return exito