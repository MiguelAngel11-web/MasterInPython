"""  
Proyecto Python MySQL:
-Abrir asistente
-Login o registro
-Si elegimos registro, creará un usuario en la bd
-Si elegimos login, identifica al usuario y nos preguntará
-Crear nota, mostrar notas, borrarlas
"""

from usuarios import acciones

print(""" 
Acciones disponibles

    -Login(l)
    -Registro(r)

""")

hazEl = acciones.Acciones()

accion = input("¿Que quieres hacer?:")

if  accion.lower() == 'registro' or accion.lower() == 'r':
    hazEl.registro()
elif  accion.lower() == 'login' or accion.lower() == 'l':
    hazEl.login()
