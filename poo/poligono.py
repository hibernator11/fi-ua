class Poligono:
    def __init__(self, ancho, alto):
        self.nombre = 'Poligono'
        self.ancho = ancho
        self.alto = alto

    def tipo_poligono(self):
        return " El poligono es de tipo {0}".format(self.nombre)

class Rectangulo(Poligono):
    def __init__(self, ancho, height):
        super().__init__(ancho, height)
        self.nombre = 'Rectangulo'

    def area(self):
        return self.ancho * self.alto

rectangulo = Rectangulo(5, 10)
print(rectangulo.area)         # 50
print(rectangulo.tipo_poligono()) # El poligono es de tipo Rectangulo
