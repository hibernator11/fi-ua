class Padre:
    def __init__(self):
        self.__atributo_privado = "Atributo privado"
    
    # No accesible desde el exterior
    def get_atributo_privado(self):
        return self.__atributo_privado

    # No accesible desde el exterior
    def __metodo_privado(self):
        print("Metodo privado")

    # Accesible desde el exterior
    def metodo_publico(self):
        # El método y atributo privados si son accesibles desde el interior de la clase
        self.__metodo_privado()
        print(self.__atributo_privado)
        
class Hija(Padre):
    def __init__(self):
        super().__init__()
        print(self.get_atributo_privado()) # ok
        #print(self.__atributo_privado) # Error

# ejemplos clase padre
prueba = Padre()
#prueba.__atributo_privado  # Error! El atributo no es accesible desde fuera
#prueba.__metodo_privado()  # Error! El método no es accesible desde fuera
prueba.metodo_publico()     # Ok!
print(prueba.get_atributo_privado()) # Ok!

# ejemplos clase hija
hija = Hija()   
