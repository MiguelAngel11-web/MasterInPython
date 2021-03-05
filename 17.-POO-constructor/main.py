from coche import Coche

carro = Coche("Amarillo","Renaukt","Clio",150,200,4)
carro1 = Coche("Rojo","Seat","Panda",240,150,1)
carro2 = Coche("Azul","Nissan","Versa",200,100,3)
carro3 = Coche("Verde","Mercedes","Clase A",350,400,2)

print(carro.getInfo())
print(carro1.getInfo())
print(carro2.getInfo())
print(carro3.getInfo())

#Detectar tipado
if type(carro3) == Coche:
    print("Es un objeto correcto")
else:
    print("No es un objeto correcto")

#Visibilidad
print(carro.soy_publico)
print(carro.getPrivado())
