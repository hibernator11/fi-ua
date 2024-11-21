class Profesor: 
    def __init__(self, nombre, materia): 
        self.nombre = nombre 
        self.materia = materia 
    
    def descripcion(self): 
        return  f" {self.nombre} enseña {self.materia} ."
    
class Departamento: 
    def __init__(self, nombre): 
        self.nombre = nombre 
        self.profesores = []   # composicion

    def add_profesor(self, profesor): 
        self.profesores.append(profesor) 
    
    def get_detalles_departamento(self): 
        detalles = f"Departamento: {self.nombre} \n"
        detalles += "Profesores:\n" 
        
        for profesor in self.profesores: 
            detalles += f"- {profesor.descripcion()} \n" 
        return detalles    


# Creación de instancias de profesor
profesor1 = Profesor( "Gustavo Candela" , "Fundamentos de Informática" ) 
profesor2 = Profesor( "Juan Manuel Saez" , "Fundamentos de Informática" ) 
profesor3 = Profesor( "José Luis" , "Matemáticas" ) 

# Creación de un departamento y adición de profesores a él
departamentoCiencias = Departamento( "Matemáticas y Ciencias" ) 
departamentoCiencias.add_profesor(profesor1) 
departamentoCiencias.add_profesor(profesor2) 
departamentoCiencias.add_profesor(profesor3) 

# Visualización de detalles del departamento 
print (departamentoCiencias.get_detalles_departamento())
