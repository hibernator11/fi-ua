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

class Abeja(Animal):
    def reproducirSonido(self):
        print("¡Bzzzz!")
    def desplazamiento(self):
        print("Vuelo")

    # Nuevo método
    def picar(self):
        print("Picar!")


print(Perro.__bases__)
print(Animal.__subclasses__())

perro1 = Perro('mamifero', 'marron', 7)
perro1.descripcion()


mi_perro = Perro('mamífero','blanco', 13)
mi_caballo = Caballo('mamífero', 'marrón', 10)
mi_abeja = Abeja('insecto', 'amarillo', 2)
mi_perro.reproducirSonido()
mi_caballo.reproducirSonido()
mi_caballo.descripcion()
mi_abeja.descripcion()
mi_abeja.picar()
