import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

print (Path(__file__).parent)

# Montamos la ruta correcta al fichero csv.
# Path(__file__).parent devuelve la ruta de ejecución del fichero
fichero = Path(__file__).parent / "2024_Accidentalidad_1000.csv"
print("########################## fichero")
print("Fichero: " + str(fichero))


# Abrimos fichero
data = pd.read_csv(fichero, \
                   delimiter=';')

# comprobamos los tipos de datos almacenados
print("########################## tipos de datos")
print(data.dtypes)

print(data.head(10))
print(data.tail(10))
print(data['tipo_vehiculo'].unique())
print(data[data['tipo_vehiculo']=="Bicicleta"])
print(data[(data['estado_meteorológico']=="Lluvia débil") & (data['rango_edad'] =='De 35 a 39 años')])
print(data[(data['estado_meteorológico']=="Despejado") & (data['tipo_vehiculo'] =='Turismo') & (data['tipo_accidente'] =='Colisión lateral')])
