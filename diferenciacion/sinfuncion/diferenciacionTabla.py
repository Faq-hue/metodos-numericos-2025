import math
from lecturaDatos import leerMatrizPrincipal

def diferenciacion_tabla(archivo):
    # Leemos matriz de datos (x, y)
    matriz = leerMatrizPrincipal(archivo)

    # Separar en dos listas
    x = [fila[0] for fila in matriz]
    y = [fila[1] for fila in matriz]

    n = len(x)
    h = abs(x[1] - x[0])
    resultados = []

    print("\nDIFERENCIACIÓN DE UNA FUNCIÓN CON TABLA")

    # Verificar si los puntos son equiespaciados
    prueba = 1
    for i in range(n - 1):
        if abs(x[i + 1] - x[i]) != h:
            print("Los puntos no son equiespaciados")
            prueba = -1
            break

    if prueba == -1:
        return

    print("\nLos puntos son equiespaciados")
    print(f"h = {h}\n")

    while True:
        print("\nIngrese la opción deseada:")
        print("1. Derivación por derecha (hacia delante)")
        print("2. Derivación centrada")
        print("3. Derivación por izquierda (hacia atrás)")
        print("0. Salir")
        op = int(input("Opción: "))

        if op == 0:
            print("SALIDA!")
            break

        print("\n1. Derivada Primera")
        print("2. Derivada Segunda")
        print("3. Derivada Tercera")
        print("4. Derivada Cuarta")
        op1 = int(input("Opción: "))

        # ======= DERECHA =======
        if op == 1:
            if op1 == 1:
                print("\nDerivada primera por la DERECHA (error O(h))")
                for i in range(n - 1):
                    aprox = (y[i + 1] - y[i]) / h
                    print(f"x={x[i]:.4f}\t y'≈{aprox:.6f}")
                print("\nDerivada primera por la DERECHA (error O(h²))")
                for i in range(n - 2):
                    aprox = (-y[i + 2] + 4 * y[i + 1] - 3 * y[i]) / (2 * h)
                    print(f"x={x[i]:.4f}\t y'≈{aprox:.6f}")

            elif op1 == 2:
                print("\nDerivada segunda por la DERECHA (error O(h))")
                for i in range(n - 2):
                    aprox = (y[i + 2] - 2 * y[i + 1] + y[i]) / h**2
                    print(f"x={x[i]:.4f}\t y''≈{aprox:.6f}")
                print("\nDerivada segunda por la DERECHA (error O(h²))")
                for i in range(n - 3):
                    aprox = (-y[i + 3] + 4*y[i + 2] - 5*y[i + 1] + 2*y[i]) / h**2
                    print(f"x={x[i]:.4f}\t y''≈{aprox:.6f}")

        # ======= CENTRADA =======
        elif op == 2:
            if op1 == 1:
                print("\nDerivada primera CENTRADA (error O(h²))")
                for i in range(1, n - 1):
                    aprox = (y[i + 1] - y[i - 1]) / (2 * h)
                    print(f"x={x[i]:.4f}\t y'≈{aprox:.6f}")
                print("\nDerivada primera CENTRADA (error O(h⁴))")
                for i in range(2, n - 2):
                    aprox = (-y[i + 2] + 8*y[i + 1] - 8*y[i - 1] + y[i - 2]) / (12 * h)
                    print(f"x={x[i]:.4f}\t y'≈{aprox:.6f}")

            elif op1 == 2:
                print("\nDerivada segunda CENTRADA (error O(h²))")
                for i in range(1, n - 1):
                    aprox = (y[i + 1] - 2*y[i] + y[i - 1]) / h**2
                    print(f"x={x[i]:.4f}\t y''≈{aprox:.6f}")
                print("\nDerivada segunda CENTRADA (error O(h⁴))")
                for i in range(2, n - 2):
                    aprox = (-y[i + 2] + 16*y[i + 1] - 30*y[i] + 16*y[i - 1] - y[i - 2]) / (12*h**2)
                    print(f"x={x[i]:.4f}\t y''≈{aprox:.6f}")

        # ======= IZQUIERDA =======
        elif op == 3:
            if op1 == 1:
                print("\nDerivada primera IZQUIERDA (error O(h))")
                for i in range(1, n):
                    aprox = (y[i] - y[i - 1]) / h
                    print(f"x={x[i]:.4f}\t y'≈{aprox:.6f}")
                print("\nDerivada primera IZQUIERDA (error O(h²))")
                for i in range(2, n):
                    aprox = (3*y[i] - 4*y[i - 1] + y[i - 2]) / (2 * h)
                    print(f"x={x[i]:.4f}\t y'≈{aprox:.6f}")

            elif op1 == 2:
                print("\nDerivada segunda IZQUIERDA (error O(h))")
                for i in range(2, n):
                    aprox = (y[i] - 2*y[i - 1] + y[i - 2]) / h**2
                    print(f"x={x[i]:.4f}\t y''≈{aprox:.6f}")
                print("\nDerivada segunda IZQUIERDA (error O(h²))")
                for i in range(3, n):
                    aprox = (2*y[i] - 5*y[i - 1] + 4*y[i - 2] - y[i - 3]) / h**2
                    print(f"x={x[i]:.4f}\t y''≈{aprox:.6f}")

        else:
            print("Opción inválida.")


# ==== EJECUCIÓN ====
if __name__ == "__main__":
    archivo = input("Ingrese el nombre del archivo con los datos (por ejemplo datos.txt): ")
    diferenciacion_tabla(archivo)
