class Coche:

    #Atributos o propiedes (variables)
    #Caracteristicas del coche
    color = "Rojo"
    marca = "Ferrari"
    modelo = "Aventador"
    velocidad = 300
    caballaje = 500
    plazas = 2

    #Publico
    soy_publico = "Hola, soy un atributo publico"
    #Privado
    __soy_privado = "Hola, soy un atributo privado"

    #Constructor
    def __init__(self,color,marca,modelo,velocidad,caballaje,plazas):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad
        self.caballaje = caballaje
        self.plazas = plazas

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
    def setMarca(self,marca):
        self.marca = marca
    def getMarca(self):
        return self.marca
    def getInfo(self):
        info = "---- Información del coche -----"
        info += "\n Color: " + self.getColor()
        info += "\n Marca: " + self.getMarca()
        info += "\n Modelo: " + self.getModelo()
        info += "\n Velocidad: " + str(self.getVelocidad())

        return info
    def getPrivado(self):
        return self.__soy_privado
#Fin definición clase