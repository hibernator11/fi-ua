class Prueba:
    atributo_publico = "Soy un atributo publico"   # Accesible desde el exterior
    __atributo_privado = "Soy un atributo privado" # No accesible

    # No accesible desde el exterior
    def __metodo_privado(self):
        print("Metodo privado")

    # Accesible desde el exterior
    def metodo_publico(self):
        # El método si es accesible desde el interior
        self.__metodo_privado()

prueba = Prueba()
#prueba.__atributo_privado  # Error! El atributo no es accesible
#prueba.__metodo_privado()  # Error! El método no es accesible
prueba.atributo_publico     # Ok!
prueba.metodo_publico()     # Ok!
