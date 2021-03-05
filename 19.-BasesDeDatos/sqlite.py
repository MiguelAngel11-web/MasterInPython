#Importar modulo
import  sqlite3

#Conexión a base de datos
conexion = sqlite3.connect('./19-BasesDeDatos/pruebas.db')

#Crear cursor
cursor = conexion.cursor()

#Crear tabla
""" cursor.execute("CREATE TABLE IF NOT EXISTS productos(" +
"id INTEGER PRIMARY KEY AUTOINCREMENT,"+
"titulo VARCHAR(255),"+
"description TEXT,"+
"precio INT(255)"
")") """
#La manera de hacerlo en una sola linea
cursor.execute("""
CREATE TABLE IF NOT EXISTS productos(
    "id INTEGER PRIMARY KEY AUTOINCREMENT,
    "titulo VARCHAR(255),
    "description TEXT,
    "precio INT(255)
);
""")

#Guardar cambios
conexion.commit()

#Insertar datos
""" cursor.execute("INSERT INTO productos VALUES(null,'Primer prdoucto','Descripción de mi producto',550)")
conexion.commit() """

#Borrar regstros
cursor.execute("DELETE FROM productos")
conexion.commit()

#Insertar varios registros
productos = [
    ("Ordenador portatil","Buen PC",7000),
    ("Celular","Buen Phone",3000),
    ("Placa base","Buen placa base",4000),
    ("Tablet","Buena tablet",1000),
    ("Laptop portatil","Buena laptop",6000),
]
cursor.executemany("INSERT INTO productos VALUES(null,?,?,?)",productos)
conexion.commit()

#Update
cursor.execute("UPDATE productos SET precio=11100 WHERE precio=3000")

#Leer datos; listar datos
cursor.execute("SELECT * FROM productos WHERE precio >= 1000")

productos = cursor.fetchall()

for p in productos:
    print("Titulo:", p[1])
    print("Descripcion:", p[2])
    print("Precio",p[3])
    print("\n")
productos = cursor.fetchone()

cursor.execute("SELECT titulo FROM productos")
print(productos)

#Cerrar conexión
conexion.close()