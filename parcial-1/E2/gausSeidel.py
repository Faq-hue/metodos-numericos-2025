import math
from lecturaDatos import leerMatrizPrincipal, leerMatrizResultante, imprimirMatrizPrincipal

def gauss_seidel(archivo_matriz, archivo_resultante):
    m, rows, columns = leerMatrizPrincipal(archivo_matriz)
    b = leerMatrizResultante(archivo_resultante)

    if not m or not b:
        print("Error al leer los datos")
        return

    if rows != columns:
        raise ValueError("La matriz debe ser cuadrada para aplicar Gauss-Seidel.")

    if len(b) != rows:
        raise ValueError("El vector resultante no coincide con la cantidad de filas de la matriz.")

    xv = [0.0] * rows
    xn = [0.0] * rows

    tolerance = int(input("Ingrese la cantidad de cifras decimales de exactitud: "))
    tolerance = 10 ** (-tolerance)

    error = float('inf')
    iterations = 0

    # Verificación de diagonalmente dominante
    for i in range(rows):
        suma = sum(abs(m[i][j]) for j in range(columns) if i != j)
        if abs(m[i][i]) <= suma:
            raise ValueError("La matriz no es diagonalmente dominante. Gauss-Seidel puede divergir.")

    # Iteraciones de Gauss-Seidel
    while error > tolerance and iterations < 10000:
        error = 0
        iterations += 1

        for i in range(rows):
            suma = 0
            for j in range(columns):
                if j != i:
                    # acá la diferencia con Jacobi: se usa xn[j] si ya fue actualizado en esta iteración
                    suma += m[i][j] * (xn[j] if j < i else xv[j])
            xn[i] = (b[i] - suma) / m[i][i]
            error += (xn[i] - xv[i]) ** 2
            xv[i] = xn[i]  # actualización inmediata

        error = math.sqrt(error)

        if iterations == 9999:
            print("Número máximo de iteraciones alcanzado")

    # Resultados finales
    print("Conjunto solución:")
    for i in range(rows):
        print(f"x{i+1} = {xn[i]:E}")
    print(f"Error: {error:E}\nIteraciones: {iterations}")

def main():
    gauss_seidel("datos.dat","datos2.dat")

if __name__ == "__main__":
    main()

