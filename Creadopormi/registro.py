from bd import BD

class Registro(BD):
    
    def  __init__(self):
        super().__init__()
        self.database = BD()
    
    def registrarNuevo(self):
        self.nombre = input("Introduce tu nombre:")
        while self.nombre == None or  self.nombre == '':
            self.nombre = input("Introduce tu nombre:")

        self.email = input("Introduce tu email:")
        while self.email == None or  self.email == '':
            self.email = input("Introduce tu email:")

        self.password = input("Introduce tu contraseña:")
        while self.password == None or  self.password == '':
            self.password = input("Introduce tu contraseña:")
        insert_stmt = (
        "INSERT INTO users (id, nombre, correo, password) "
        "VALUES ('null', %s, %s, %s)")
        data = (self.nombre, self.email, self.password)
      
        res = self.cursor.execute(insert_stmt,data)

        self.database.commit()
        return res

        

