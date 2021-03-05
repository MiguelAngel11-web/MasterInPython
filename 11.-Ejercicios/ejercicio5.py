"""  
Crear una lista con el contenido de esta tabla
ACCION  AVENTURA            DEPORTES
GTA     ASSASSIN CREED      FIFA 21
COD     CRASH               PES 21
PUGB    PRINCE OF PERSIA    MOTO GP 21


Mostrar esta información ordenada 
"""

videogames = [
    {
        'categoria':'Acción',
        'games':['GTA','COD','PUGB']
    },
    {
        'categoria':'Aventura',
        'games':['Assassin Credd','Crash','Principe of Persia']
    },
    {
        'categoria':'Deportes',
        'games':['FIFA 21','PES 21','MotoGP 21']
    },

]

for game in videogames:
    print(game['categoria'])
    for elemento in game['games']:
        print(elemento)
    print("\n")


