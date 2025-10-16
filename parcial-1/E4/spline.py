import numpy as np
import lecturaDatos

def natural_cubic_spline_coeffs(x, y, tol=1e-12):
    n = len(x)
    N = 4*(n-1)
    A = np.zeros((N, N), dtype=float)
    b = np.zeros(N, dtype=float)
    row = 0

    # Polinomios en extremos
    for i in range(n-1):
        xi = x[i]
        xi1 = x[i+1]
        col = 4*i
        A[row, col:col+4] = [1, xi, xi**2, xi**3]
        b[row] = y[i]
        row += 1

        A[row, col:col+4] = [1, xi1, xi1**2, xi1**3]
        b[row] = y[i+1]
        row += 1

    # Derivadas primeras
    for i in range(1, n-1):
        xi = x[i]
        col_prev = 4*(i-1)
        col_curr = 4*i
        A[row, col_prev:col_prev+4] = [0, 1, 2*xi, 3*xi**2]
        A[row, col_curr:col_curr+4] = [0, -1, -2*xi, -3*xi**2]
        row += 1

    # Derivadas segundas
    for i in range(1, n-1):
        xi = x[i]
        col_prev = 4*(i-1)
        col_curr = 4*i
        A[row, col_prev:col_prev+4] = [0, 0, 2, 6*xi]
        A[row, col_curr:col_curr+4] = [0, 0, -2, -6*xi]
        row += 1

    # Condiciones naturales
    xi = x[0]
    A[row, 0:4] = [0, 0, 2, 6*xi]
    row += 1

    xi = x[-1]
    col_last = 4*(n-2)
    A[row, col_last:col_last+4] = [0, 0, 2, 6*xi]
    row += 1

    assert row == N, f"Se llenaron {row} filas, se esperaba {N}"

    coef = np.linalg.solve(A, b)
    return coef.reshape((n-1, 4))


def evaluate_spline(coef, x_nodes, valor):
    for i in range(len(x_nodes)-1):
        if x_nodes[i] <= valor <= x_nodes[i+1]:
            a, b, c, d = coef[i]
            return a + b*valor + c*valor**2 + d*valor**3
    raise ValueError("El valor está fuera del rango de interpolación")


if __name__ == "__main__":
    archivo = "datos.dat"   # archivo con dos columnas: x y
    matriz = lecturaDatos.leerMatrizPrincipal(archivo)

    x = [fila[0] for fila in matriz]
    y = [fila[1] for fila in matriz]

    print("Puntos leídos:")
    lecturaDatos.imprimirMatrizPrincipal(matriz)

    coef = natural_cubic_spline_coeffs(x, y)
    print("\nCoeficientes [a, b, c, d] por intervalo:")
    for i, cfs in enumerate(coef):
        print(f"[{x[i]}, {x[i+1]}] -> {cfs}")

    valor = float(input("\nIngrese el valor que desea interpolar: "))
    resultado = evaluate_spline(coef, x, valor)
    print(f"\nX = {valor},   S(X) = {resultado}")
