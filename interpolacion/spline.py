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

    # --- Crear tabla equiespaciada usando el spline ---
    num_puntos = int(input("\nCantidad de puntos equiespaciados que querés generar: "))
    x_eq = np.linspace(x[0], x[-1], num_puntos)
    y_eq = [evaluate_spline(coef, x, xi) for xi in x_eq]
    
    print("\nTabla equiespaciada generada:")
    for xi, yi in zip(x_eq, y_eq):
        print(f"{xi:.6f}\t{yi:.6f}")

    # --- Derivadas numéricas ---
    h = x_eq[1] - x_eq[0]
    deriv = [0.0]*len(x_eq)

    # Derivadas centradas
    for i in range(1, len(x_eq)-1):
        deriv[i] = (y_eq[i+1] - y_eq[i-1]) / (2*h)

    # Extremos (derivada del spline)
    def spline_deriv(coef, x_nodes, valor):
        for i in range(len(x_nodes)-1):
            if x_nodes[i] <= valor <= x_nodes[i+1]:
                a, b, c, d = coef[i]
                return b + 2*c*valor + 3*d*valor**2
        raise ValueError("Fuera del rango de interpolación")

    deriv[0] = spline_deriv(coef, x, x_eq[0])
    deriv[-1] = spline_deriv(coef, x, x_eq[-1])

    print("\nTabla con derivadas:")
    for xi, yi, di in zip(x_eq, y_eq, deriv):
        print(f"x={xi:.6f}\ty={yi:.6f}\ty'≈{di:.6f}")

    # --- Integrales ---
    trap = 0.0
    for i in range(len(x_eq)-1):
        trap += 0.5 * (y_eq[i] + y_eq[i+1]) * h

    simpson = None
    if (len(x_eq)-1) % 2 == 0:
        s = y_eq[0] + y_eq[-1]
        for i in range(1, len(x_eq)-1):
            s += 4*y_eq[i] if i % 2 == 1 else 2*y_eq[i]
        simpson = s * (h/3)

    print(f"\nIntegral Trapecio = {trap}")
    if simpson is not None:
        print(f"Integral Simpson 1/3 = {simpson}")

    # comparación con valor exacto ---
    I_exact = 2.0596753  # valor exacto dado en el enunciado

    # Calcular errores absolutos
    err_abs_trap = abs(trap - I_exact)
    #err_abs_simp = abs(simpson - I_exact)

    # Calcular errores porcentuales
    err_pct_trap = (err_abs_trap / abs(I_exact)) * 100
    #err_pct_simp = (err_abs_simp / abs(I_exact)) * 100

    # Determinar método más preciso
    #metodo_mejor = "Simpson 1/3" if err_abs_simp < err_abs_trap else "Trapecio"

    # Mostrar resultados
    print("\n=== Comparación con valor exacto ===")
    print(f"Valor exacto: {I_exact}")
    print(f"Trapecio -> Error abs: {err_abs_trap:.6f}, Error %: {err_pct_trap:.3f}%")
 #   print(f"Simpson -> Error abs: {err_abs_simp:.6f}, Error %: {err_pct_simp:.3f}%")
#    print(f"\nMétodo más preciso: {metodo_mejor}")
