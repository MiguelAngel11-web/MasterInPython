#Programación orientada a objetos (POO o OOP)
#Definir una clase (molde para crear más objetos de ese tipo)
#(coche) con caracteristicas

class Coche:

    #Atributos o propiedes (variables)
    #Caracteristicas del coche
    color = "Rojo"
    marca = "Ferrari"
    modelo = "Aventador"
    velocidad = 300
    caballaje = 500
    plazas = 2

    #Métodos, son acciones que hace el objeto (coche)(funciones)
    #Self es para acceder a todas los atributis y metodos de nuestra clase.
    def acelerar(self):
        self.velocidad += 1
    def frenar(self):
        self.velocidad -= 1
    def getVelocidad(self):
        return self.velocidad
    def setColor(self,color):
        self.color = color
    def getColor(self):
        return self.color
    def setModelo(self,modelo):
        self.modelo = modelo
    def getModelo(self):
        return self.modelo
#Fin definición clase

#Crear objetos / Instaciar la clase
coche = Coche()

print("**** Coche 1 ****")

coche.setColor("amarillo")
coche.setModelo("Murcielago")

print(coche.marca, coche.getModelo(),coche.getColor())
print("Velocidad actual: ",coche.getVelocidad())

coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.acelerar()

coche.frenar()

print("Velocidad actual: ",coche.getVelocidad())

#Crear más objetos
coche2 = Coche()
coche2.setColor("negro")
coche2.setModelo("Gallardo")

print("\n**** Coche 2 ****")
print(coche2.marca,coche2.getColor(),coche2.getModelo())





