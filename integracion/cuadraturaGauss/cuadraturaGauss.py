import math

# === Definición de la función a integrar ===
def f(x):
    # f(x) = (2 - x^3) * (x - 3)^2
    return (2 - (x ** 3)) * ((x - 3) ** 2)

# === Cambio de variable para Gauss-Legendre ===
def g(x, a, b):
    return f(((b - a) / 2) * x + (b + a) / 2)

# === Programa principal ===
def main():
    print("Valor inferior del intervalo: ", end="")
    a = float(input())
    print("Valor superior del intervalo: ", end="")
    b = float(input())

    dx = (b - a) / 2

    while True:
        n = int(input("Cantidad de puntos [o 0 (cero) para salir]: "))

        if n == 0:
            print("\nSalida.")
            break

        aprox = 0.0
        w = []
        x = []

        if n == 2:
            print("\nCuadratura de Gauss con 2 puntos")
            w = [1, 1]
            x = [-math.sqrt(1 / 3), math.sqrt(1 / 3)]

        elif n == 3:
            print("\nCuadratura de Gauss con 3 puntos")
            w = [5/9, 8/9, 5/9]
            x = [-math.sqrt(3/5), 0.0, math.sqrt(3/5)]

        elif n == 4:
            print("\nCuadratura de Gauss con 4 puntos")
            w = [
                (18 - math.sqrt(30)) / 36,
                (18 + math.sqrt(30)) / 36,
                (18 + math.sqrt(30)) / 36,
                (18 - math.sqrt(30)) / 36
            ]
            x = [
                -math.sqrt((3 + 2 * math.sqrt(6/5)) / 7),
                -math.sqrt((3 - 2 * math.sqrt(6/5)) / 7),
                math.sqrt((3 - 2 * math.sqrt(6/5)) / 7),
                math.sqrt((3 + 2 * math.sqrt(6/5)) / 7)
            ]

        elif n == 5:
            print("\nCuadratura de Gauss con 5 puntos")
            w = [
                (322 - 13 * math.sqrt(70)) / 900,
                (322 + 13 * math.sqrt(70)) / 900,
                128 / 225,
                (322 + 13 * math.sqrt(70)) / 900,
                (322 - 13 * math.sqrt(70)) / 900
            ]
            x = [-0.906179846, -0.538469310, 0.0, 0.538469310, 0.906179846]

        elif n == 6:
            print("\nCuadratura de Gauss con 6 puntos")
            w = [
                0.1713244924,
                0.3607615730,
                0.4679139346,
                0.4679139346,
                0.3607615730,
                0.1713244924
            ]
            x = [
                -0.9324695142,
                -0.6612093865,
                -0.2386191861,
                0.2386191861,
                0.6612093865,
                0.9324695142
            ]

        else:
            print("Número de puntos no válido (usar 2, 3, 4, 5 o 6).")
            continue

        # Cálculo de la cuadratura
        aprox = sum(w[i] * g(x[i], a, b) for i in range(len(w))) * dx

        print(f"\nLa integral f(x) en el intervalo [{a}; {b}] es: {aprox:.6f}\n")

if __name__ == "__main__":
    main()
