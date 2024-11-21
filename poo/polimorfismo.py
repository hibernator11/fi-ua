class Animal:
    def __init__(self, especie, color, edad):
        self.especie = especie
        self.edad = edad
        self.color = color

    def reproducirSonido(self):
        # Método vacío
        pass

    def desplazamiento(self):
        # Método vacío
        pass

    def descripcion(self):
        print("Soy un Animal del tipo", type(self).__name__)

class Perro(Animal):
    def reproducirSonido(self):
        print("¡Guau guau!")
    def desplazamiento(self):
        print("Camino con 4 patas")

class Caballo(Animal):
    def reproducirSonido(self):
        print("¡hiiii, hiiii, hiiii!")
    def desplazamiento(self):
        print("Camino con 4 patas")

mi_perro = Perro('mamífero','blanco', 13)
mi_caballo = Caballo('mamífero', 'marrón', 10)

animales = []
animales.append(mi_perro)
animales.append(mi_caballo)

for animal in animales:
    animal.reproducirSonido()
