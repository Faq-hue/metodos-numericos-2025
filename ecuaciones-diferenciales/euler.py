import math

def f(x, y):
    """Función diferencial: dy/dx = cos(x) + log(1 + x²)"""
    #return math.cos(x) + math.log(1 + x**2)
    return (1+x)*math.sqrt(y)

def main():
    # Entrada de datos
    x_min = float(input("Ingrese el valor del límite inferior del intervalo de integración: "))
    x_max = float(input("Ingrese el valor del límite superior del intervalo de integración: "))
    N = int(input("Ingrese el número de puntos: "))

    print(f"x_min={x_min}, x_max={x_max}, N={N}")

    h = 0.1
    print(f"h={h:.12f}")

    y0 = float(input("Ingrese el dato inicial y0: "))
    print(f"y0={y0}")

    # Inicialización de listas
    x = [0.0] * (N + 1)
    y = [0.0] * (N + 1)

    x[0] = x_min
    y[0] = y0

    # Método de Euler explícito
    for j in range(1, N + 1):
        x[j] = x_min + j * h
        y[j] = y[j - 1] + h * f(x[j - 1], y[j - 1])

    # Escritura de resultados en archivo
    with open("datos.dat", "w") as file:
        for j in range(N + 1):
            file.write(f"{x[j]:.12f}  {y[j]:.12f}\n")

    print("\nResultados guardados en 'datos.dat'.")

    I_real = 1.2345  # <-- cambiá por el valor exacto conocido
    error_abs = abs(I_real - integral)
    error_porcentual = abs(error_abs / I_real) * 100
    
    print(f"Error absoluto: {error_abs:.6f}")
    print(f"Error porcentual: {error_porcentual:.3f}%")


if __name__ == "__main__":
    main()
