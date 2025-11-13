import lecturaDatos
import copy
import math


def determinante(A, tol=1e-10):
    n = len(A)
    A = [fila[:] for fila in A]  # Copia para no modificar la original
    det = 1
    
    for i in range(n):
        # Pivoteo parcial
        max_row = max(range(i, n), key=lambda r: abs(A[r][i]))
        if abs(A[max_row][i]) < tol:
            return 0.0  # Matriz singular
        
        if max_row != i:
            A[i], A[max_row] = A[max_row], A[i]
            det *= -1  # Cambio de signo al intercambiar filas
        
        det *= A[i][i]
        
        # Eliminación
        for j in range(i+1, n):
            factor = A[j][i] / A[i][i]
            for k in range(i, n):
                A[j][k] -= factor * A[i][k]
    
    return det


def gauss_eliminacion(A, b, tol=1e-10):
    n = len(A)
       
    # Eliminación hacia adelante
    for i in range(n):
        # Pivoteo parcial
        max_row = max(range(i, n), key=lambda r: abs(A[r][i]))
                
        if abs(A[max_row][i]) < tol:
            raise ValueError("La matriz es singular o casi singular.")
        
        # Intercambiar filas
        if max_row != i:
            A[i], A[max_row] = A[max_row], A[i]
            b[i], b[max_row] = b[max_row], b[i]
        
        # Eliminación
        for j in range(i+1, n):
            factor = A[j][i] / A[i][i]
            for k in range(i, n):
                A[j][k] -= factor * A[i][k]
            b[j] -= factor * b[i]
    
    
    # Retrosustitución
    x = [0] * n
    for i in range(n-1, -1, -1):
        suma = sum(A[i][j] * x[j] for j in range(i+1, n))
        x[i] = (b[i] - suma) / A[i][i]
    
    return x

def construir_matriz_normal(x, y):
    """Genera la matriz y el vector del sistema normal para f(x)=a+b*x+c*e^x"""
    n = len(x)
    sum_x = sum(x)
    sum_x2 = sum(xi**2 for xi in x)
    sum_ex = sum(math.exp(xi) for xi in x)
    sum_xex = sum(xi * math.exp(xi) for xi in x)
    sum_e2x = sum(math.exp(2*xi) for xi in x)
    sum_y = sum(y)
    sum_xy = sum(xi * yi for xi, yi in zip(x, y))
    sum_yex = sum(yi * math.exp(xi) for xi, yi in zip(x, y))

    M = [
        [n, sum_x, sum_ex],
        [sum_x, sum_x2, sum_xex],
        [sum_ex, sum_xex, sum_e2x]
    ]
    r = [sum_y, sum_xy, sum_yex]
    return M, r

def evaluar_ajuste(x, y, coef):
    """Calcula residuos, SSE, RMSE y R2."""
    a, b, c = coef
    f = lambda xi: a + b*xi + c*math.exp(xi)
    y_hat = [f(xi) for xi in x]
    resid = [yi - yhi for yi, yhi in zip(y, y_hat)]
    SSE = sum(r**2 for r in resid)
    RMSE = math.sqrt(SSE / len(x))
    y_mean = sum(y)/len(y)
    SST = sum((yi - y_mean)**2 for yi in y)
    R2 = 1 - SSE/SST
    return resid, SSE, RMSE, R2

def main():
    '''
    A = lecturaDatos.leerMatrizPrincipal("../gauss/datos.dat")
    b = lecturaDatos.leerMatrizResultante("../gauss/datos2.dat")

    # Copias profundas
    A_copy1 = copy.deepcopy(A)
    A_copy2 = copy.deepcopy(A)
    b_copy = b[:]

    # Calcular determinante sin modificar A original
    det = determinante(A_copy1)
    #print(f"Determinante de la matriz: {det:.6f}")

    try:
        solucion = gauss_eliminacion(A_copy2, b_copy)
        print("Solución del sistema:")
        for i, val in enumerate(solucion):
            print(f"x{i+1} = {val:.6f}")
    except ValueError as e:
        print(e)
''' 
    #caso de que no me den los datos en forma de matriz normal
    # Leer datos de archivos
    x = lecturaDatos.leerMatrizResultante("datos.dat")
    y = lecturaDatos.leerMatrizResultante("datos2.dat")

    # Construir sistema normal
    M, r = construir_matriz_normal(x, y)

    # Resolver por eliminación gaussiana
    M_copy = copy.deepcopy(M)
    r_copy = r[:]
    coef = gauss_eliminacion(M_copy, r_copy)

    print("\nCoeficientes del ajuste:")
    print(f"a = {coef[0]:.6f}, b = {coef[1]:.6f}, c = {coef[2]:.6f}")

    # Evaluar ajuste
    resid, SSE, RMSE, R2 = evaluar_ajuste(x, y, coef)
    print("\nResiduos:", [round(r, 6) for r in resid])
    print(f"\nSSE = {SSE:.6f}")
    print(f"RMSE = {RMSE:.6f}")
    print(f"R² = {R2:.6f}")

    # Ejemplo: predecir valor
    x_nuevo = 1.8
    y_est = coef[0] + coef[1]*x_nuevo + coef[2]*math.exp(x_nuevo)
    print(f"\nPredicción para x={x_nuevo}: y_est = {y_est:.6f}")
    

if __name__ == "__main__":
    main()
