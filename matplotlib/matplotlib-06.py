#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 18:45:36 2024

@author: gustavo
"""

import matplotlib.pyplot as plt

lista_x = []
lista_y = []

radio = 1
radios = []
rojo_verde_azul = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]  # Colores R, G y B
colores = []
for i in range(3):
    color = rojo_verde_azul[i]
    for j in range(3):
        lista_x.append(i)
        lista_y.append(j)
        print(i,j,radio,color)
        radios.append(radio)
        colores.append(color)
        radio *= 2
        

plt.scatter(lista_x, lista_y, s=radios, c=colores)
plt.show()
