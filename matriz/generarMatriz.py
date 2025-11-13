import math

def construir_matriz_normal(x, y):
    """
    Construye la matriz normal y el vector del sistema de mínimos cuadrados
    para el modelo f(x) = a + b*x + c*e^x.
    
    Parámetros:
        x, y : listas o arrays de datos
    Devuelve:
        M : matriz 3x3 (ecuaciones normales)
        r : vector 3x1 (términos independientes)
    """
    n = len(x)
    sum_x = sum(x)
    sum_x2 = sum(xi**2 for xi in x)
    sum_ex = sum(math.exp(xi) for xi in x)
    sum_xex = sum(xi * math.exp(xi) for xi in x)
    sum_e2x = sum(math.exp(2*xi) for xi in x)
    sum_y = sum(y)
    sum_xy = sum(xi * yi for xi, yi in zip(x, y))
    sum_yex = sum(yi * math.exp(xi) for xi, yi in zip(x, y))

    # Matriz del sistema (3x3)
    M = [
        [n, sum_x, sum_ex],
        [sum_x, sum_x2, sum_xex],
        [sum_ex, sum_xex, sum_e2x]
    ]

    # Vector del sistema (3x1)
    r = [sum_y, sum_xy, sum_yex]

    return M, r


# Ejemplo de uso con tus datos
x = [0.2, 0.6, 0.8, 1.1, 1.5, 1.6, 2.1, 2.3, 2.5, 3.0]
y = [2.71, 3.92, 4.79, 6.22, 8.48, 9.15, 13.40, 15.58, 18.17, 27.08]

M, r = construir_matriz_normal(x, y)

print("Matriz normal (3x3):")
for fila in M:
    print([round(val, 6) for val in fila])

print("\nVector derecho:")
print([round(val, 6) for val in r])
