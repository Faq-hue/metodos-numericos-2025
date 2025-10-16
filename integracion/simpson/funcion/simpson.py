import math

def f(x):
    # f(x) = (4x - 5)^3
    return (4 * x - 5) ** 3

def main():
    # Entradas
    a = float(input("Valor inferior del intervalo: "))
    b = float(input("Valor superior del intervalo: "))

    # Validar cantidad de intervalos (debe ser par)
    while True:
        n = int(input("Cantidad de intervalos/segmentos (debe ser par): "))
        if n % 2 == 0:
            break
        print("La cantidad de intervalos debe ser par. Intente nuevamente.")

    # Paso
    h = (b - a) / n

    # Sumas
    sum_imp = 0.0  # Suma de índices impares
    sum_par = 0.0  # Suma de índices pares

    # Suma de términos impares
    for i in range(1, n, 2):  # 1, 3, 5, ...
        x = a + i * h
        sum_imp += f(x)

    # Suma de términos pares
    for i in range(2, n-1, 2):  # 2, 4, 6, ...
        x = a + i * h
        sum_par += f(x)

    # Regla de Simpson 1/3 compuesta
    aprox = (h / 3) * (f(a) + f(b) + 4 * sum_imp + 2 * sum_par)

    print(f"\nLa integral de f(x) en el intervalo [{a}; {b}] es: {aprox:.6f}\n")

if __name__ == "__main__":
    main()
