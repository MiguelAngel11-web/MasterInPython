"""  
Tiene que pedir las calificaciones de 15 alumnos
y sacar por pantalla cuantos han aprobado y cuantos reprobaron
"""

contador = 1
aprobados = 0
reprobados = 0

for contador in range(1,16):
    calificacion = int(input(f"Que calificación tuvo el {contador} alumno: "))
    if(calificacion > 5):
        aprobados += 1
    else:
        reprobados +=1
    contador
else:
    print(f"Los alumnos aprobados en total son:{aprobados} \nLos alumnos reprobados en total son: {reprobados}")