import mysql.connector



class BD:
    def __init__(self):
        super().__init__()
        #Conexión
        self.database = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="proyecto_python"
        )
        self.cursor = self.database.cursor(buffered=True)
        self.cursor.execute("CREATE DATABASE IF NOT EXISTS  proyecto_python")
        self.cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS users(
            id int(10) auto_increment not null,
            nombre varchar(80) not null,
            correo varchar(70) not null,
            password varchar(40) not null,
            CONSTRAINT pk_vehiculo PRIMARY KEY(id)
        )""")
        self.cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS notas(
            id int(10) auto_increment not null,
            titulo varchar(80) not null,
            contenido text not null,
            CONSTRAINT pk_vehiculo PRIMARY KEY(id)
        )""")

        self.database.commit()

