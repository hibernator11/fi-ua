class Estudiante:
    def __init__(self, nombre, grupo, nota, practica):
        self.nombre = nombre
        self.grupo = grupo
        self.nota = nota
        self.practica = practica
    
    def __str__(self):
        return "Nombre: " + self.nombre + " " + \
               " Grupo: " + self.grupo + \
               " Nota: " + str(self.nota) + \
               " Práctica entregada: " + self.practica

    def copia(self):
        nuevo = Estudiante(self.nombre, self.grupo, self.nota, self.practica)
        return nuevo

def lee_estudiante():
    nombre = input("Nombre: ")
    grupo = input("Grupo (A,B o C): ")
    nota = float(input("Nota de examen: "))
    practica = input("Nota entregada (s/n): ")
       
    return Estudiante(nombre, grupo, nota, practica)

estudiante = lee_estudiante()
print(estudiante)

# si no hacemos una copia, modifica los valores
#copia = estudiante
#print(copia.nota)
#copia.nota = 9
#print(estudiante.nota)

# hacemos una copia y entonces no modifica la nota
copia = estudiante.copia()
print(copia.nota)
copia.nota = 9
print(estudiante.nota)

copia.nombre = "Pepe"
print(estudiante.nombre)
print(copia.nombre)
