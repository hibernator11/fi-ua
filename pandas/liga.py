import pandas as pd

goleadores = [
    {"nombre": "Gustavo Candela", "anyo": 2024, "goles": 5},
    {"nombre": "Luisa Perez", "anyo": 2024, "goles": 3},
    {"nombre": "Luis Fernández", "anyo": 2024, "goles": 15},
    {"nombre": "Laura Pérez", "anyo": 2024, "goles": 7},
]
df = pd.DataFrame(goleadores)
print(df)

print(df["goles"].max())
print(df[df["goles"] == df["goles"].max()])
print(df["goles"].sum())
