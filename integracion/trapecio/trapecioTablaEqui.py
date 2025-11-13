import math
from lecturaDatos import leerMatrizPrincipal, leerMatrizResultante

# --- Lectura de datos ---
# Suponiendo que los archivos contienen columnas:
# datosX.txt → valores de x
# datosY.txt → valores de y

x = leerMatrizResultante("datosX.dat")   # o leerMatrizPrincipal si están en matriz
y = leerMatrizResultante("datosY.dat")

n = len(x)

if n != len(y):
    raise ValueError("Los vectores x e y deben tener la misma longitud")

# --- Controlar que los puntos estén equiespaciados ---
h = x[1] - x[0]

for i in range(1, n - 1):
    if abs((x[i + 1] - x[i]) - h) > 1e-6:
        raise ValueError("Los puntos no están equiespaciados")

# --- Cálculo de la integral por el método del trapecio ---
suma = 0
for i in range(1, n - 1):
    suma += y[i]

aprox = (h / 2) * ((y[0] + y[-1]) + 2 * suma)

# --- Resultado ---
print(f"La integral f(x) con puntos EQUIDISTANTES en el intervalo [{x[0]}; {x[-1]}] es: {aprox}")
print()
