import matplotlib.pyplot as plt
import numpy as np

# datos del precio medio del alquier por año
xpoints = np.array([2019, 2020, 2021, 2022, 2023, 2024])
ypoints = np.array([600, 800, 805, 830, 900, 910])

# grafica en forma de linea
plt.plot(xpoints,ypoints)
plt.show()

# grafica en forma de barras
plt.bar(xpoints,ypoints)
plt.show()

# grafico circular
mylabels = ["2019", "2020", "2021", "2022", "2023", "2024"]
plt.pie(ypoints, labels = mylabels)
plt.show() 
