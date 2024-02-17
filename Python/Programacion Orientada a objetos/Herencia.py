# Arte de heredar metodos y atributos de una clase superior

class Persona():

    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

class Empleado(Persona)