#Capturar excepciones y manejar errores con código
#suceptible a fallos/errores

""" try:
    nombre = input("Introduce tu nombre: ")
    if len(nombre) > 1:
        nombre_user = f"El nombre es {nombre}"

    print(nombre_user)

except:
    print("Ha ocurrido un error.Intentalo de nuevo.")
else:
    print("Todo a funcionado correctamente")
finally:
    print("Fin de la iteración.") """

#Manejar multiples excepciones
""" try:
    numero = int(input("Dime el número para elevarlo al cuadrado: "))

    print("El cuadrado es: " +  str(numero*numero))
except TypeError:
    print("Debes meter sólo valores enteros en tu código.")
except ValueError:
    print("Introduce un número correcto.")
except Exception as e:
    print("Ha ocurrido un error: ", type(e).__name__) """

#Excepciones personalizadas
try:
    nombre = input("Introduce tu nombre: ")
    edad = int(input("Introduce tu edad: "))

    if edad < 5 or edad > 110:
        raise ValueError("La edad introducida no es real")
    elif  len(nombre) <=1:
        raise  ValueError("El nombre no está completo")
    else:
        print("Bienvenido mi amigo.")
except ValueError:
    print("Introduce los datos correctamente.")
except Exception as e:
    print("Existe un error")
