import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

print (Path(__file__).parent)

# Montamos la ruta correcta al fichero csv.
# Path(__file__).parent devuelve la ruta de ejecución del fichero
fichero = Path(__file__).parent / "co2_emmissions_by_state_2024.csv"
print("########################## fichero")
print("Fichero: " + str(fichero))

# Si cambiamos :.0f por :.2f o por :.4f añade 0, 2 o 4 decimales 
pd.options.display.float_format = '{:.4f}'.format

# Abrimos fichero
data = pd.read_csv(fichero, \
                   delimiter=',', skiprows=1, names=('YEAR','MONTH','STATE_NAME','STATE_CODE','CO2_QTY_TONNES','TF','NOTE'))

# comprobamos los tipos de datos almacenados
print("########################## tipos de datos")
print(data)

