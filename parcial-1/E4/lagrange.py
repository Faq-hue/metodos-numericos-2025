import numpy as np
import lecturaDatos as ld   # importamos tu archivo

def interpolacion_polinomial(x, y):
    n = len(x)
    errorMinimo = 1e-6

    # Construcción de la matriz del sistema
    m = np.zeros((n, n))
    b = np.zeros(n)

    for i in range(n):
        m[i][0] = 1.0
        for j in range(1, n):
            m[i][j] = x[i]**j
        b[i] = y[i]

    # Eliminación Gaussiana con pivoteo parcial
    for i in range(n - 1):
        if abs(m[i][i]) < errorMinimo:
            cambio = False
            for j in range(i + 1, n):
                if abs(m[j][i]) > errorMinimo:
                    m[[i, j]] = m[[j, i]]
                    b[i], b[j] = b[j], b[i]
                    cambio = True
                    break
            if not cambio:
                print("El sistema es singular, no se puede resolver")
                return None

        for j in range(i + 1, n):
            f = -m[j][i] / m[i][i]
            m[j, i:] += f * m[i, i:]
            b[j] += f * b[i]

    print("\nMatriz triangular superior:")
    for i in range(n):
        print(m[i], "--->", b[i])

    # Sustitución regresiva
    a = np.zeros(n)
    a[n - 1] = b[n - 1] / m[n - 1][n - 1]
    print("\n----- Soluciones -----")
    print(f"a[{n-1}] = {a[n-1]}")

    for i in range(n - 2, -1, -1):
        suma = b[i] - np.dot(m[i, i+1:], a[i+1:])
        a[i] = suma / m[i][i]
        print(f"a[{i}] = {a[i]}")

    print("\nPolinomio P(x):")
    polinomio = " + ".join([f"{a[i]:.4f}" if i == 0 else f"{a[i]:.4f}*x^{i}" for i in range(n)])
    print("P(x) =", polinomio)

    return a


if __name__ == "__main__":
    # Leer datos desde archivos
    matriz = ld.leerMatrizPrincipal("datos.dat")   # cada fila = valores de x
    vector = ld.leerMatrizResultante("datos2.dat")  # vector con valores de y

    # Convertimos la matriz a lista simple (suponemos que es una sola columna en x.txt)
    x = [fila[0] for fila in matriz]
    y = vector

    # Ejecutar interpolación
    coef = interpolacion_polinomial(x, y)

    # Evaluar el polinomio en un valor ingresado
    valorX = float(input("\nIngrese el valor de X: "))
    resultado = sum(coef[i] * (valorX**i) for i in range(len(coef)))
    print("El resultado es:", resultado)
