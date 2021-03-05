import mysql.connector

def conectar():
    database = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='master_python'
    )

    cursor = database.cursor(buffered=True)

    return [database,cursor]