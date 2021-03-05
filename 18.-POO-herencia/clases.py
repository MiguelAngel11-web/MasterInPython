#Hernecia es la posibilidad de compartr
#atributos y métodos entre clases
# y que diferentes clases hereden de otras


class Persona:
    """
 nombre
 apellidos
 altura
 edad """
    def  getNombre(self):
        return self.nombre
    
    def getApellidos(self):
        return self.apellidos

    def getAltura(self):
        return self.altura 
    
    def getEdad(self):
        return self.edad
    
    def setNombre(self,nombre):
        self.nombre = nombre

    def setApellidos(self,apellidos):
        self.apellidos = apellidos

    def setAltura(self,altura):
        self.altura = altura

    def setEdad(self,edad):
        self.edad = edad

    def hablar(self):
        return "Estoy hablando"

    def caminar(self):
        return "Estoy caminando"

    def dormir(self):
        return "Estoy durmiendo"

class Informatico(Persona):

    """lenguajes
    experiencia """

    def __init__(self):
        self.lenguajes = "HTML, CSS, JavaScript, PHP"
        self.experienca = 5
    
    def getLenguajes(self):
        return self.lenguajes
    
    def aprender(self,lenguajes):
        self.lenguajes = lenguajes
        return self.lenguajes
    
    def programar(self):
        return "Estoy programando"

    def reparando(self):
        return "He reparado tu PC"

class TecnicoRedes(Informatico):

    def __init__(self):
        #Para heredar el constructor de la clase Informatico
        super().__init__()
        self.audiatarRedes = "Experto"
        self.experiencaEnRedes = 15

    def auditoria(self):
        return "Estoy auditando una red" 
        