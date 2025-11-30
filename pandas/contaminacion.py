import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

print (Path(__file__).parent)

# Montamos la ruta correcta al fichero csv.
# Path(__file__).parent devuelve la ruta de ejecución del fichero
fichero = Path(__file__).parent / "../csv/co2_emmissions_by_state_2024.csv"
print("########################## fichero")
print("Fichero: " + str(fichero))

# Abrimos fichero
data = pd.read_csv(fichero, \
                   delimiter=',', skiprows=1, names=('YEAR','MONTH','STATE_NAME','STATE_CODE','CO2_QTY_TONNES','TF','NOTE'))

# comprobamos los tipos de datos almacenados
print("########################## tipos de datos")
print(data.dtypes)

# cambiamos el tipo de datos
data['CO2_QTY_TONNES'] = data['CO2_QTY_TONNES'].astype('int32')
print("########################## cambiamos tipo de datos")
print(data.dtypes) 

print("########################## imprimimos dataframe")
print(data)

print("########################## imprimimos primera fila")
print(data.iloc[0])

print("########################## imprimimos los datos de Albania para 2024")
print(data.loc[(data['YEAR']==2024) & (data['STATE_NAME']=='ALBANIA')].head())

print("########################## imprimimos de las primeras 6 filas, las columnas year y state_name")
print(data.loc[0:5, ['YEAR', 'STATE_NAME']])

print("########################## uso de condicionales")
print(data[(data['CO2_QTY_TONNES'] > 1000) & (data['CO2_QTY_TONNES'] < 6500)].head())

# creamos dataframe para datos de españa
data_es = data[data['STATE_NAME']=='SPAIN']
#print(data_es['CO2_QTY_TONNES'])

print("########################## imprimimos la curva de CO2 para España")
print(data_es)
data_es['CO2_QTY_TONNES'].plot(kind='line')
plt.show()

fichero_espanya = Path(__file__).parent / "datos-espanya.csv"
print("########################## guardamos en fichero")
print("Fichero: " + str(fichero_espanya))
data_es.to_csv(fichero_espanya,
               mode='w',
               index=True, 
               header=True, 
               #columns=['x', 'y'], 
               index_label='Index')

# uso de operadores
print("########################## uso de operadores")
print(data_es.head())
print(data_es.head(3))
print(data_es.tail())
print(data_es.tail(3))
print(data_es.head())
print("########################## calculamos el maximo de toneladas de C02 para España")
maxCO2 = data_es['CO2_QTY_TONNES'].max()
print(maxCO2)
print("########################## calculamos la suma de toneladas de C02 para España")
sumaCO2 = data_es['CO2_QTY_TONNES'].sum()
print(sumaCO2)
