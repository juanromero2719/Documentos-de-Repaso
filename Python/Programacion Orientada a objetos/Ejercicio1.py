# Crear una clase llamada estudiante
# Crear atributos nombre, edad y grado
# Crear un metoido que imprima "El estudiante nombre esta estudiando"
# Crear un objeto Estudiante y usar el metodo estudiar()
# Pedir datos

class Estudiante():

    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado

    def estudiar(self):
        print(f"El estudiante {self.nombre} esta estudiando")


nombre = input("Ingrese el nombre del estudiante: ")
edad = int(input("Ingrese la edad del estudiante: "))
grado = input("Ingrese el grado del estudiante: ")

Estudiante1 = Estudiante(nombre, edad, grado)

print(f""" 
        El estudiante {Estudiante1.nombre} \n
        tiene {Estudiante1.edad} años \n
        y esta en el grado {Estudiante1.grado}

    """)

while True:
    estudiar = input()
    if estudiar.lower() == "estudiar":
        Estudiante1.estudiar()