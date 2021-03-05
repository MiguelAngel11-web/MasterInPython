from bd import BD

class Login(BD):

    def __init__(self):
        super().__init__()
        self.name = ""
        self.correo = ""
        self.result = ""
        
        self.database = BD()
        
       
    def comprobarUser(self):
        self.email = input("Introduce tu email:")
        while self.email == None or  self.email == '' or type(self.email) != str:
            self.email = input("Introduce tu email:")

        self.password = input("Introduce tu contraseña:")
        while self.password == None or  self.password == '' or type(self.password) != str:
            self.password = input("Introduce tu contraseña:")

        #Consulta
        select_stmt = "SELECT nombre,correo FROM users WHERE correo=%(email)s AND password=%(password)s"
    
        self.cursor.execute(select_stmt,{'email':self.email,'password':self.password}) 
        #Resultado de consulta
        self.result = self.cursor.fetchone()

        return self.result
