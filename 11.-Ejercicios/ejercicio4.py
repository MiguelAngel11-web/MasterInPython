"""  
Crear un script que tenga 4 varibales. 
Una lista, un string, un entero, un booleano
Y que imprima un mensaje según el tipo de dato de cada variable.
Usar funciones.
"""

""" def mensaje_variable(variable):
    texto = "Es una varible de tipo"
    if isinstance(variable,str):
        texto += " string: "+ str(variable)
        return texto
    elif  isinstance(variable,int):
        texto += " entera: " + str(variable)
        return texto
    elif  isinstance(variable,bool):
        texto += " booleana: " + str(variable)
        return texto
    elif  isinstance(variable,list):
        texto += " lista: " + str(variable)
        return texto



tipo_variable = mensaje_variable(cadena)
print(tipo_variable)
tipo_variable = mensaje_variable(entera)
print(tipo_variable)
tipo_variable = mensaje_variable(bandera)
print(tipo_variable)
tipo_variable = mensaje_variable(lista)
print(tipo_variable) """

#Como lo hizo el Vato
entera = 123
lista = [123,34,1,23]
cadena = "Soy cadena"
bandera = True

def comprobarTipado(dato,tipo):
    test = isinstance(dato,tipo)
    res = ""

    if test:
        res = f"El dato es del tipo: {type(dato)}"
    else:
        res = None
    
    return res

print(comprobarTipado(lista,list))
print(comprobarTipado(cadena,str))
print(comprobarTipado(entera,int))
print(comprobarTipado(bandera,bool))

