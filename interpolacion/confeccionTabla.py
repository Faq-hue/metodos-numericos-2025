import math

def tabla_equipasos(f, x_inicial, x_final, n):
    """
    Construye una tabla con n+1 puntos entre x_inicial y x_final.
    Los puntos estarán separados por un paso h = (x_final - x_inicial)/n.
    """
    h = (x_final - x_inicial) / n
    tabla = []

    for i in range(n + 1):
        x = x_inicial + i * h
        tabla.append((x, f(x)))

    return tabla


#funcion
def f(x):
    return math.sqrt(1 + x**2)

if __name__ == "__main__":
    tabla = tabla_equipasos(f, 0, 2, 10)
    print("Tabla de valores (x, f(x)):")
    for x, fx in tabla:
        print(f"x = {x:.4f}   f(x) = {fx:.6f}")
