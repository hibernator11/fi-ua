#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 26 16:14:36 2025

@author: gustavo
https://www.aprendemachinelearning.com/analisis-exploratorio-de-datos-pandas-python/
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#import statsmodels.api as sm
 
url = 'https://raw.githubusercontent.com/hibernator11/fi-ua/refs/heads/main/csv/countries-population.csv'
df_pop = pd.read_csv(url, sep=",")
print(df_pop.head(5))

print('Cantidad de Filas y columnas:',df_pop.shape)
print('Nombre columnas:',df_pop.columns)

df_pop_es = df_pop[df_pop["country"] == 'Spain' ]
print(df_pop_es.head())
df_pop_es.drop(['country'],axis=1)['population'].plot(kind='bar')


df_pop_ar = df_pop[(df_pop["country"] == 'Argentina')]


anios = df_pop_es['year'].unique()
pop_ar = df_pop_ar['population'].values
pop_es = df_pop_es['population'].values
 
df_plot = pd.DataFrame({'Argentina': pop_ar,
                    'Spain': pop_es}, 
                       index=anios)
df_plot.plot(kind='bar')


# Ahora filtremos todos los paises hispano-hablantes

url = 'https://raw.githubusercontent.com/hibernator11/fi-ua/refs/heads/main/csv/countries.csv'
df_countries = pd.read_csv(url, sep=";")
print(df_countries.head(5))

df_espanol = df_countries.replace(np.nan, '', regex=True)
df_espanol = df_espanol[ df_espanol['languages'].str.contains('es') ]
print(df_espanol)

df_espanol.set_index('alpha_3')[['population','area']].plot(kind='bar',rot=65,figsize=(20,10))
