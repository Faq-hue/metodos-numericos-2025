import math

def f(x, y):
    """Ecuación diferencial: dy/dx = (1 + x)*sqrt(y)"""
    return (1 + x) * math.sqrt(y)

def y_exacta(x):
    """Solución analítica"""
    return (1 + x/2 + x**2/4)**2

def main():
    # Intervalo y condiciones iniciales
    x_min = 0.0
    x_max = 1.0
    y0 = 1.0
    h = 0.01  # paso
    N = int((x_max - x_min)/h)

    print(f"Integrando de x={x_min} a x={x_max} con h={h}, N={N} pasos")

    # Inicialización
    x = [0.0]*(N+1)
    y = [0.0]*(N+1)
    x[0] = x_min
    y[0] = y0

    # Método de Euler
    for j in range(1, N+1):
        x[j] = x_min + j*h
        y[j] = y[j-1] + h * f(x[j-1], y[j-1])

    # Mostrar tabla cada Δx = 0.2 (cada 20 pasos)
    print("\n  x\t\ty(Euler)\t\ty(exacta)\t\tError abs")
    print("--------------------------------------------------------")
    for j in range(0, N+1, 20):
        err = abs(y_exacta(x[j]) - y[j])
        print(f"{x[j]:.1f}\t\t{y[j]:.6f}\t\t{y_exacta(x[j]):.6f}\t\t{err:.6e}")

    # Guardar resultados en archivo
    with open("datos_euler.dat", "w") as f_out:
        for j in range(N+1):
            err = abs(y_exacta(x[j]) - y[j])
            f_out.write(f"{x[j]:.6f}\t{y[j]:.6f}\t{y_exacta(x[j]):.6f}\t{err:.6e}\n")

    print("\nResultados guardados en 'datos_euler.dat'.")

if __name__ == "__main__":
    main()
