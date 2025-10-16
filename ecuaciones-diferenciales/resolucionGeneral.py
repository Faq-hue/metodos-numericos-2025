import math

def f(x, y):
    """Ecuación diferencial: dy/dx = 3*sqrt(y)"""
    return 3 * math.sqrt(y)

def main():
    print("\nIngrese x0 (condición inicial) = ", end="")
    x0 = float(input())
    print("Ingrese y0 (condición inicial) = ", end="")
    y0 = float(input())
    print("Ingrese h = ", end="")
    h = float(input())

    x = x0
    y = y0

    print("\nMétodos")
    print("1. Método de Euler")
    print("2. Método del Punto Medio")
    print("3. Método de Heun")
    print("4. Método de Runge-Kutta de 4° Orden")
    op = int(input("Ingrese el método para resolver la ecuación diferencial: "))

    cant = 1
    while cant != 0:
        # Cálculo de pendientes (k)
        k1 = f(x, y)
        k2 = f(x + 0.5 * h, y + 0.5 * k1 * h)
        k3 = f(x + 0.5 * h, y + 0.5 * k2 * h)
        k4 = f(x + h, y + k3 * h)

        if op == 1:
            print("\nMétodo de Euler")
            result = y + h * k1
        elif op == 2:
            print("\nMétodo del Punto Medio")
            result = y + h * k2
        elif op == 3:
            print("\nMétodo de Heun")
            k2 = f(x + h, y + k1 * h)
            result = y + (h / 2) * (k1 + k2)
        elif op == 4:
            print("\nMétodo de Runge-Kutta de 4° Orden")
            result = y + (h / 6) * (k1 + 2*k2 + 2*k3 + k4)
        else:
            print("Opción inválida.")
            break

        x += h
        print(f"En [{x:.4f} ; {result:.6f}] → f(x,y) = {f(x, result):.6f}")

        y = result
        print("\n¿Otro punto? (si=1, no=0)")
        cant = int(input())

    print("\nFin del programa.")

if __name__ == "__main__":
    main()
