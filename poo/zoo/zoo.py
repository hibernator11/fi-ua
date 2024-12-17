import numpy as np

class Zoo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.animales = []
        return 
    
    def addAnimal(self, animal):
        self.animales.append(animal)
        return 
    
    def removeAnimal(self, animal):
        count = 0
        for a in self.animales:
            if a.nombre == animal.nombre:
                del(self.animales[count])
                return
            count=count+1
        return
    
    def test_de_vuelo(self):
        print("Test de vuelo")
        for animal in zoo.animales:
            print(animal.volar())
        print("#############")
        return
    
    def describeZoo(self):
        print("Animales del zoo: " + self.nombre)
        for animal in zoo.animales:
            print(animal)
        print("#############")
        return
    
    def guardar(self):
        f = open("zoo.txt", "w") 
        for animal in zoo.animales:
            f.write(animal.describe() + "\n")
        f.close()

    def edadMedia(self):
        edad_lista = []
        for a in self.animales:
            edad_lista.append(a.edad)
        #print(edad_lista)
        array_edad = np.array(edad_lista)
        return np.mean(array_edad)
    
    def edadMax(self):
        edad_lista = []
        for a in self.animales:
            edad_lista.append(a.edad)
        #print(edad_lista)
        array_edad = np.array(edad_lista)
        return np.max(array_edad)

class Animal:
    def __init__(self, edad, color, nombre):
        self.edad = edad
        self.color = color
        self.nombre = nombre
        return 
    
    def __str__(self):
        return self.nombre + " " + str(self.edad) + " " + self.color

class Loro(Animal):
    def __init__(self, edad, color, nombre, comida):
        self.comida = comida
        super().__init__(edad, color, nombre)
        return 

    def volar(self):
        return "El loro " + self.nombre  + " puede volar"

    def nadar(self):
        return "El loro " + self.nombre  + " no puedo nadar"
    
    def comer(self):
        return "El loro " + self.nombre  + " come " + self.comida
    
    def __str__(self):
        return self.nombre + " " + self.comida
    
    def describe(self):
        return self.nombre + " " + self.comida

class Pinguino(Animal):
    def __init__(self, edad, color, nombre, zona):
        self.zona = zona
        super().__init__(edad, color, nombre)
        return 

    def volar(self):
        return "El pingüino " + self.nombre  + " no puede volar"

    def nadar(self):
        return "El pingüino " + self.nombre  + " puede nadar"

    def __str__(self):
        return self.nombre + " " + self.zona
    
    def describe(self):
        return self.nombre + " " + self.zona

# instancias
loro = Loro(10, "rojo", "Pepe", "fruta")
loro1 = Loro(14, "naranja", "Juan", "fruta")
loro2 = Loro(8, "amarillo", "Andres", "fruta")
pinguino = Pinguino(5, "blanco", "Luis", "Sudáfrica")
pinguino1 = Pinguino(6, "negro", "Alfredo", "Antártida")

zoo = Zoo("Zoo de Alicante")
zoo.addAnimal(loro)
zoo.addAnimal(loro1)
zoo.addAnimal(loro2)
zoo.addAnimal(pinguino)
zoo.addAnimal(pinguino1)
zoo.describeZoo()
zoo.test_de_vuelo()
print("Edad media de los animales del zoo:" + str(zoo.edadMedia()))
print("Edad maxima de los animales del zoo:" + str(zoo.edadMax()))

# test borrado
zoo.removeAnimal(loro)

zoo.guardar()

