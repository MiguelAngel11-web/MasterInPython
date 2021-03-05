""" 
Programa que comprube si una variable está vacia
y si esta vacia, rellenarla con texto en minisculas y mostrarlo
en mayusculas.


"""

texto = ""

if len(texto) <= 0:
    texto = "texto que será transformado"
    print(f"Texto original: {texto}")
    print(f"Upper case: {texto.upper()}")