""" 
Array ASOCIATIVO O JSON
Tipo de dato que alamacena un conjunto de datos.
En formato clave > valor.
Es parecido a un array o un objeto json.
"""

persona = {
    "nombre":"Victor",
    "apellidos":"Castaneda",
    "web":"nada.mx"
}

#print(persona["apellidos"])

#Lista con diccionarios
contactos = [
    {
        'nombre':'Mi',
        'email':'mi@gmail.com'
    },
    {
        'nombre':'Luis',
        'email':'luis@hotmail.com'
    },
    {
        'nombre':'Amore',
        'email':'amore@hotmail.com'
    }
]

contactos[0]['nombre'] = "Minombre"

print(contactos[0]['nombre'])
print('****Listado contactos****')

for contacto in contactos:
    print(f"Nombre del contácto: {contacto['nombre']}")
    print(f"Email del contácto: {contacto['email']}")
    print("\n")