import pandas as pd
import numpy as np

# Creamos el array con los datos
numpy_array = np.array([[1000, 3000, 1500], 
                        [3000, 5500, 2800], 
                        [5000, 12000, 7890]])

# calculamos la suma 
r = np.sum(numpy_array)
print(r)

# si le decimos axis 0 calcula la suma por columna y obtenemos una array con 3 posiciones con las sumas
r = np.sum(numpy_array, 0)
print(r)

# si le decimos axis 1 calcula la suma por fila y obtenemos una array con 3 posiciones con las sumas
r = np.sum(numpy_array, 1)
print(r)
