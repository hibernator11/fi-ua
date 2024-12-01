import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

print (Path(__file__).parent)

# Montamos la ruta correcta al fichero csv.
# Path(__file__).parent devuelve la ruta de ejecución del fichero
fichero = Path(__file__).parent / "wikidata-paises.csv"
print("########################## fichero")
print("Fichero: " + str(fichero))


# Abrimos fichero
data = pd.read_csv(fichero, \
                   delimiter=',')

# comprobamos los tipos de datos almacenados
print("########################## tipos de datos")
print(data.dtypes)

print(data.head(10))
print(data.tail(10))
print("########################## ordenamos por habitantes")
print(data.sort_values(by='population', ascending=False))

print("########################## total de paises")
print(data['countryLabel'].count())

print("########################## recupera los países que tengan más de 1 millón de habitantes")
print(data[data['population'] > 1000000])

print("########################## recupera los países que tengan menos de 1 millón de habitantes")
print(data[data['population'] < 1000000])

print("########################## Recupera los 10 países con mayor número de habitantes")
ordenados = data.sort_values(by='population', ascending=False)
ordenados = ordenados.head(10)
print(ordenados)
ordenados.to_csv("habitantes.csv")
