import math
import lecturaDatos as ld

import math

# ---------- Funciones de lectura ----------
def leerMatrizPrincipal(archivo):
    try:
        with open(archivo, 'r') as f:
            lineas = f.readlines()
    except FileNotFoundError:
        print("No se puede abrir el archivo")
        return [], 0, 0

    matriz = []
    max_columnas = 0

    for linea in lineas:
        if linea.strip():
            numeros = [float(num) for num in linea.strip().split()]
            matriz.append(numeros)
            if len(numeros) > max_columnas:
                max_columnas = len(numeros)

    filas = len(matriz)
    return matriz, filas, max_columnas


def imprimirMatrizPrincipal(matriz):
    for fila in matriz:
        print(" ".join(f"{num:.6f}" for num in fila))


def leerMatrizResultante(archivo):
    try:
        with open(archivo, 'r') as f:
            lineas = f.readlines()
    except FileNotFoundError:
        print("No se puede abrir el archivo")
        return []

    vector = []
    for linea in lineas:
        if linea.strip():
            numeros = [float(num) for num in linea.strip().split()]
            vector.extend(numeros)
    return vector


# ---------- Método de Jacobi ----------
def jacobi(archivo_matriz, archivo_resultante):
    m, rows, columns = leerMatrizPrincipal(archivo_matriz)
    b = leerMatrizResultante(archivo_resultante)

    if not m or not b:
        print("Error al leer los datos")
        return

    if rows != columns:
        raise ValueError("La matriz debe ser cuadrada para aplicar Jacobi.")

    if len(b) != rows:
        raise ValueError("El vector resultante no coincide con la cantidad de filas de la matriz.")

    xv = [0.0] * rows
    xn = [0.0] * rows

    tolerance = int(input("Ingrese la cantidad de cifras decimales de error: "))
    tolerance = 10 ** (-tolerance)

    error = float('inf')
    iterations = 0

    # Verificación de diagonalmente dominante
    for i in range(rows):
        suma = sum(abs(m[i][j]) for j in range(columns) if i != j)
        if abs(m[i][i]) <= suma:
            raise ValueError("La matriz no es diagonalmente dominante. Jacobi puede divergir.")

    # Iteraciones de Jacobi
    while error > tolerance and iterations < 10000:
        error = 0
        iterations += 1
        for i in range(rows):
            suma = sum(m[i][j] * xv[j] for j in range(columns) if i != j)
            if m[i][i] == 0:
                raise ZeroDivisionError(f"Elemento diagonal nulo en fila {i+1}, Jacobi no es aplicable.")
            xn[i] = (b[i] - suma) / m[i][i]
            error += (xn[i] - xv[i]) ** 2
        error = math.sqrt(error)

        # Depuración opcional
        if iterations % 50 == 0:
            print(f"Iter {iterations}: {xn}, error={error}")

        xv = xn.copy()

    if iterations >= 10000:
        print("Número máximo de iteraciones alcanzado sin convergencia")
    else:
        print("Conjunto solución:")
        for i in range(rows):
            print(f"x{i+1} = {xn[i]:E}")
        print(f"Error: {error:E}\nIteraciones: {iterations}")

def main():
    jacobi("datos.dat","datos2.dat")

if __name__ == "__main__":
    main()
