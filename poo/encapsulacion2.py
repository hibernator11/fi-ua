Created on Tue Nov 25 16:36:16 2025

@author: gustavo
"""

class Prueba:
    
    def __init__(self):
        self.__atributo_privado = "Soy un atributo privado" # No accesible
    
    def getAtributoPrivado(self):
        return self.__atributo_privado
        
    
prueba = Prueba()
prueba.__atributo_privado = "puedo acceder"

print(prueba.__atributo_privado) # salida: puedo acceder
print(prueba.getAtributoPrivado())  # salida: Soy un atributo privado
