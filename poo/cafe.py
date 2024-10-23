class Cafe:
    # Constructor
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = float(precio)
    
    def comprueba_presupuesto(self, presupuesto):
        # Check if the budget is valid
        if not isinstance(presupuesto, (int, float)):
            print('Error, introduce un número por favor')
            exit()
        if presupuesto < 0: 
            print('Lo siento, no tienes dinero') 
            exit() 
    
    def devuelve_cambio(self, presupuesto):
        return presupuesto - self.precio

    def vender(self, presupuesto):
        self.comprueba_presupuesto(presupuesto)
        if presupuesto >= self.precio:
            print(f'Puedes comprar el cafe {self.nombre} ')
            if presupuesto == self.precio:
                print('Prespuesto justo. No hay cambio que devolver')
            else:
                print(f'Su cambio {self.devuelve_cambio(presupuesto)}')

            exit('¡Muchas gracias por su compra!')

pequeño = Cafe('Pequeño', 2)
medio = Cafe('Medio', 5)
grande = Cafe('Grande', 6)
 
try:
   presupuesto = float(input('¿Cuál es su presupuesto? '))
except ValueError:
   exit('Por favor, introduzca un número')
  
for cafe in [pequeño, medio, grande]:
   cafe.vender(presupuesto)
