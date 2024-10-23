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


class Caballo(Animal):
    def __init__(self, especie, color, edad, precio):
        # Opcion 1
        # self.especie = especie
        # self.color = color
        # self.edad = edad
        # self.precio = precio

        # Opcion 2
        super().__init__(especie, color, edad)
        self.precio = precio
    def reproducirSonido(self):
        print("¡hiiii, hiiii, hiiii!")
    def desplazamiento(self):
        print("Camino con 4 patas")

mi_caballo = Caballo('mamífero', 'marrón', 10, 1000)
mi_caballo.reproducirSonido()
mi_caballo.descripcion()
