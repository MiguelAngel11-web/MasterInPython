#Lo recomendable es tener las funciones hasta arriba
def mi_function():
    #print("Hola mundo")
    return "Hola mundo" + nombre #Siempre poner las variables ya definidas antes de usarlas.

def mi_segunda_function():
    #print("hOLA QUEQ TAL")
    return "Hola que tal" + apellidos
nombre = "Mike"
apellidos = "Casta"

print("Hola Mundo")
print(f"Bienvenido {nombre}")
#Es mejor pasarle los parametros y que la función se encarge de lo demás
print(mi_function())
print(mi_segunda_function())
#Lo recomendable es que siempre devolvamos el valor en la función