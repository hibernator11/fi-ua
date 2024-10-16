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

def lee_estudiante():
    nombre = input("Nombre: ")
    grupo = input("Grupo (A,B o C): ")
    nota = float(input("Nota de examen: "))
    practica = input("Nota entregada (s/n): ")
       
    return Estudiante(nombre, grupo, nota, practica)

estudiante = lee_estudiante()
print(estudiante)
