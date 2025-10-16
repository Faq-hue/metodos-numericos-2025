import math
import sys
from lecturaDatos import leerMatrizPrincipal

def integrar_simpson(archivo):
    # Leer datos desde archivo
    matriz = leerMatrizPrincipal(archivo)

    # Separar columnas en listas x e y
    x = [fila[0] for fila in matriz]
    y = [fila[1] for fila in matriz]
    n = len(x)

    if n < 3:
        print("No hay suficientes puntos para aplicar Simpson.")
        return

    # Verificar equiespaciado
    h = x[1] - x[0]
    for i in range(1, n - 1):
        if abs((x[i + 1] - x[i]) - h) > 1e-10:
            print("Los puntos no están equiespaciados.")
            return

    # Verificar que el número de puntos sea impar (n-1 intervalos pares)
    if n % 2 == 0:
        print("No se puede aplicar el método de Simpson. Usar Trapecio o interpolar para más puntos.")
        sys.exit(0)

    # Sumas
    sum_imp = 0.0  # suma de los valores con índice impar
    sum_par = 0.0  # suma de los valores con índice par

    for i in range(1, n - 1, 2):  # índices impares
        sum_imp += y[i]

    for i in range(2, n - 2, 2):  # índices pares
        sum_par += y[i]

    # Regla de Simpson compuesta
    aprox = (h / 3) * ((y[0] + y[n - 1]) + 4 * sum_imp + 2 * sum_par)

    print(f"La integral f(x) en el intervalo [{x[0]}; {x[n - 1]}] es: {aprox:.6f}\n")


if __name__ == "__main__":
    archivo = input("Ingrese el nombre del archivo con los datos (por ejemplo datos.txt): ")
    integrar_simpson(archivo)
