""" 

"""

#Variable global
frase = "Esta es una prueba de frase en varible global"

def holaMundo():
    #Variable local
    frase = "Hola mundo"
    print(frase)
    #Dentro una varibale global
    #global variable_global
    variable_global = "Soy global"

holaMundo()
