import mysql.connector

#Conexión

database = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="master_python"
)
#¿La conexión ha sido correcta?
#print (database)

#Cursor
cursor = database.cursor(buffered=True)#Se coloca buffered = true para que nos deje hacer más consultas y todas las operaciones que necesitemos de la base de datos

#Crear base de datos
""" cursor.execute("CREATE DATABASE IF NOT EXISTS  master_python")

cursor.execute("SHOW DATABASES")

for bd in cursor:
    print(bd) """

#Crear tablas
cursor.execute(""" 
CREATE TABLE IF NOT EXISTS vehiculos(
    id int(10) auto_increment not null,
    marca varchar(40) not null,
    modelo varchar(40) not null,
    precio float(10,2) not null,
    CONSTRAINT pk_vehiculo PRIMARY KEY(id)
)

""")

""" cursor.execute("SHOW TABLES")
 
for table in cursor:
    print(table) """

#Insertar datos

""" cursor.execute("INSERT INTO vehiculos VALUES (null,'Oper','Astra',18500)")
coches = [
    ('Seat','Ibiza',5000),
    ('Renault','Clio',15000),
    ('Mercedes','Saxo',5000),
    ('Nissan','Versa',5000),
    ('Chevrolet','Spark',5000)
] """

#cursor.executemany("INSERT INTO vehiculos VALUES (null, %s, %s,%s)",coches)

#Seleccionar elementos de nuestra tabla
#cursor.execute("SELECT * FROM vehiculos")#Para todos los datos

#Para datos especificos 
# cursor.execute("SELECT marca,precio FROM vehiculos")
cursor.execute("SELECT * FROM vehiculos WHERE precio <= 5000 AND marca = 'Seat'")

result = cursor.fetchall()

for coche in result:
    #print(coche)
    #Sacar marca y precios
    print(coche[1],coche[3]) 

cursor.execute("SELECT * FROM vehiculos ")

coche = cursor.fetchone()
print(coche)

#Para guardar cambios en la base de datos
#database.commit()

#borrar registros

#cursor.execute("DELETE FROM vehiculos WHERE marca = 'Seat'")
#database.commit()

#print(cursor.rowcount,"borrados!!!")

#Actualizar registros
cursor.execute("UPDATE vehiculos SET modelo='LEON' WHERE marca='Oper'") 
database.commit()

print(cursor.rowcount,"actualizado!!!")