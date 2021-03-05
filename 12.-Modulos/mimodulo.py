
def holaMundo(nombre):
    return f"Hola {nombre}"

def calculadora(num1,num2,basicas = True):
    suma = num1 + num2
    resta = num1 - num2
    multi = num1 * num2
    division = num1 / num2

    cadena = ""

    if basicas != False:
        cadena += "Suma: " + str(suma)
        cadena += "\nResta: " + str(resta)  
    else:
        cadena += "\nMultiplicasión: " + str(multi)
        cadena += "\nDivisión: " + str(division)

    return cadena