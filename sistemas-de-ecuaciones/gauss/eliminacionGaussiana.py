import lecturaDatos
import copy

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


def main():
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

if __name__ == "__main__":
    main()
