import usuarios.conexion as conexion
import datetime
import hashlib

connect = conexion.conectar()
datbase = connect[0]
cursor = connect[1]

class Usuario:
    
    def __init__(self,nombre,apellidos,email,password):
        super().__init__()
        self.name = nombre
        self.lastname = apellidos
        self.email = email
        self.password = password
    
    def registrar(self):
        #Cifrar contraseña
        cifrado = hashlib.sha256()
        #Necesitamos pasarlo en bite, por lo tanto usamos encode('utf8')
        cifrado.update(self.password.encode('utf8'))


        sql = "INSERT INTO usuarios VALUES(null, %s , %s , %s , %s , %s )"
        usuario = (self.name, self.lastname, self.email, cifrado.hexdigest(),datetime.datetime.now())
        try:
            cursor.execute(sql,usuario)
            database.commit()
            result = [cursor.rowcount,self]
        except:
            result = [0,self]

        return result

    def identificar(self):
        #Consulta para comprobar si existe el usuario
        sql = "SELECT * FROM usuarios WHERE email = %s AND password = %s"

        #Cifrar contraseña
        cifrado = hashlib.sha256()
        #Necesitamos pasarlo en bite, por lo tanto usamos encode('utf8')
        cifrado.update(self.password.encode('utf8'))

        #Datos para la consulta
        usuario = (self.email,cifrado.hexdigest())

        cursor.execute(sql,usuario)

        result = cursor.fetchone()

        return result


