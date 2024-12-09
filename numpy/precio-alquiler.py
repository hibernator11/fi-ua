import pandas as pd
import numpy as np

# Creamos el array con los datos
numpy_array = np.array([[100, 101, 105, 105, 105, 110], 
                        [401, 402, 403, 403, 403, 403], 
                        [150, 150, 150, 155, 155, 155]])

# calculamos la media total
r = np.mean(numpy_array)
print(r)

# si le decimos axis 0 calcula la media por columna y obtenemos una array con 6 posiciones con las medias
r = np.mean(numpy_array, 0)
print(r)

# si le decimos axis 1 calcula la media por fila y obtenemos una array con 3 posiciones con las medias
r = np.mean(numpy_array, 1)
print(r)

# definimos las columnas
columnas = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio']

# Creamos el DataFrame con las columnas y los datos
df = pd.DataFrame(data=numpy_array, columns=columnas)

# Mostramos por pantalla
print(df)
