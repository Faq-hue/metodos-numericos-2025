import math
from lecturaDatos import leerMatrizResultante

# --- Lectura de datos ---
x = leerMatrizResultante("datosX.txt")
y = leerMatrizResultante("datosY.txt")

n = len(x)

if n != len(y):
    raise ValueError("Los vectores x e y deben tener la misma longitud")

# --- Cálculo del trapecio para puntos NO equiespaciados ---
suma = 0
for i in range(n - 1):
    h = x[i + 1] - x[i]
    suma += (h / 2) * (y[i] + y[i + 1])

# --- Resultado ---
print(f"La integral f(x) con puntos NO EQUIDISTANTES en el intervalo [{x[0]}; {x[-1]}] es: {suma}")
print()
