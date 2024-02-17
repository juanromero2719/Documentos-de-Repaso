# Utilizando Pascal Case

class Celular():

    # Método constructor
    def __init__(self, marca, modelo, camara):
    # Self es una forma de hacer referencia al mismo objeto
        self.marca = marca
        self.modelo = modelo
        self.camara = camara
    # Atributos - Propiedades de los elementos
        
    # Métodos - Funciones de los elementos
        
    def llamar(self):
        print(f" {self.modelo} esta llamando...")

    def cortar(self):
        print(f" {self.modelo} esta cortando...")

    # Las variables solo existen para la instancia

# Instanciar una clase = crear un objeto
    
celular1 = Celular(marca="Samsung", modelo="Galaxy S10", camara="12MP")
celular2 = Celular(marca="Apple", modelo="Iphone 11", camara="16MP")

#print(celular2.marca)
print(celular1.llamar())

# CLASE, CONSTRUCTOR, METODOS, SELF, INSTANCIA, ATRIBUTOS, PROPIEDADES, PASCAL CASE