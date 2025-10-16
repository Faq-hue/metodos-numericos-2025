#!/usr/bin/env python3
"""
polynomial_regression_con_lecturaDatos.py

Regresión polinómica por mínimos cuadrados
Usa lecturaDatos.py para leer los datos
"""

import numpy as np
import lecturaDatos

def build_normal_system(x, y, degree):
    n = len(x)
    m = np.zeros((degree+1, degree+1), dtype=float)
    b = np.zeros(degree+1, dtype=float)
    for i in range(degree+1):
        for j in range(degree+1):
            m[i,j] = np.sum(x ** (i+j))
        b[i] = np.sum((x ** i) * y)
    return m, b

def solve_normal_system(m, b):
    try:
        a = np.linalg.solve(m, b)
    except np.linalg.LinAlgError:
        a = np.linalg.lstsq(m, b, rcond=None)[0]
    return a

def format_polynomial(a):
    terms = []
    for i, coef in enumerate(a):
        if i == 0:
            terms.append(f"{coef:.6g}")
        else:
            sign = " + " if coef >= 0 else " - "
            val = abs(coef)
            terms.append(f"{sign}{val:.6g} X^{i}")
    return "".join(terms)

def compute_statistics(x, y, a):
    n = len(x)
    degree = len(a) - 1
    y_pred = sum(coef * (x ** i) for i, coef in enumerate(a))
    y_mean = np.mean(y)
    st = np.sum((y - y_mean) ** 2)
    sr = np.sum((y - y_pred) ** 2)
    syx = np.sqrt(sr / (n - (degree+1))) if n > degree+1 else float("nan")
    r2 = (st - sr) / st if st > 0 else 1.0
    r2 = max(r2, 0)  # evitar negativos por error numérico
    r = np.sqrt(r2)
    return sr, syx, st, r2, r

def main():
    # Leer datos usando lecturaDatos.py
    archivo = input("datos.dat").strip()
    matriz = lecturaDatos.leerMatrizPrincipal(archivo)
    if not matriz:
        print("No se pudieron leer datos.")
        return
    
    # separar x, y (suponemos 2 columnas)
    x = np.array([fila[0] for fila in matriz])
    y = np.array([fila[1] for fila in matriz])
    n = len(x)
    print(f"Puntos leídos: {n}")

    while True:
        try:
            grado = int(input("Ingrese el grado del polinomio deseado: "))
        except ValueError:
            print("Ingrese un número entero.")
            continue
        if n < grado+1:
            print("No hay suficientes puntos para ese grado.")
            continue
        break

    m, b = build_normal_system(x, y, grado)
    a = solve_normal_system(m, b)

    print("\nCoeficientes encontrados:")
    for i, coef in enumerate(a):
        print(f"a[{i}] = {coef:.12g}")

    print("\nPOLINOMIO:")
    print(format_polynomial(a))

    sr, syx, st, r2, r = compute_statistics(x, y, a)
    print("\nResultados estadísticos:")
    print(f"Error/Residuo (sr) = {sr:.6g}")
    print(f"Desviación estándar (syx) = {syx:.6g}")
    print(f"Error medio (st) = {st:.6g}")
    print(f"Coeficiente de determinación (R^2) = {r2:.6g}")
    print(f"Coeficiente de correlación (R) = {r:.6g}")

if __name__ == "__main__":
    main()
