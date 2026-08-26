import math

def f(x, y):
    #return (1 + x) * math.sqrt(y)
    return (4*x*y)/(1 + x**2)

def y_exacta(x):
    #return (1 + x/2 + x**2/4)**2
    return pow(1 + x**2, 2)

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
    x[1] = x_min + 1*h
    y[1] = y[1-1] + h * f(x[1-1], y[1-1])

    # Método nuevo
    for j in range(2, N+1):
        x[j] = x_min + j*h
        y[j] = y[j-1] + h * 2* (f(x[j-1], y[j-1])-f(x[j-2], y[j-2]))
        

    # Mostrar tabla cada Δx = 0.2 (cada 20 pasos)
    print("\n  x\t\ty(Nv)\t\ty(exacta)\t\tError abs")
    print("--------------------------------------------------------")
    for j in range(0, N+1, 20):
        err = abs(y_exacta(x[j]) - y[j])
        print(f"{x[j]:.1f}\t\t{y[j]:.10f}\t\t{y_exacta(x[j]):.10f}\t\t{err:.10e}")

    # Guardar resultados en archivo
    with open("datos_nuevo_metodo_euler.dat", "w") as f_out:
        for j in range(N+1):
            err = abs(y_exacta(x[j]) - y[j])
            f_out.write(f"{x[j]:.10f}\t{y[j]:.10f}\t{y_exacta(x[j]):.10f}\t{err:.10e}\n")

    print("\nResultados guardados en 'datos_nuevo_metodo_euler.dat'.")

if __name__ == "__main__":
    main()
