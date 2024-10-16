class Persona:
    def __init__(self, nombre, dni, edad):
        self.nombre = nombre
        self.dni = dni
        self.edad = edad
      
    def iniciales(self):
        cadena = ''
        for caracter in self.nombre:
           if (caracter >= 'A' and caracter<='Z'):
               cadena = cadena +  caracter + ". "
        return cadena

    def __str__(self):
        cadena = "Nombre: {0}\n".format(self.nombre)
        cadena = cadena + "DNI: {0}\n".format(self.dni)
        cadena = cadena + "Edad: {0}".format(self.edad)
        return cadena    

persona = Persona("Gustavo Candela", "12345678l", "20") 
print(persona)
print(persona.iniciales())
