import math

# ================================
# Métodos de diferencias finitas
# ================================

def diferencia_progresiva(f, x, h=0.1):
    return (f(x + h) - f(x)) / h

def diferencia_regresiva(f, x, h=0.1):
    return (f(x) - f(x - h)) / h

def diferencia_central(f, x, h=0.1):
    return (f(x + h) - f(x - h)) / (2 * h)


# ================================
# Función a evaluar
# ================================
def f(x):
    return math.exp(math.sqrt(1+x))*math.log(1+2*x**2)

# Derivada exacta para comparar
def f_derivada(x):
    return x / math.sqrt(1 + x**2)


# ================================
# Ejecución principal
# ================================
if __name__ == "__main__":
    x = 0.25

    h = 0.1

    print("=== DERIVACIÓN NUMÉRICA ===")
    print(f"Evaluando en x = {x} con h = {h}\n")

    df_prog = diferencia_progresiva(f, x, h)
    df_reg  = diferencia_regresiva(f, x, h)
    df_cent = diferencia_central(f, x, h)

    df_exacta = f_derivada(x)



    print(f"Diferencia progresiva : {df_prog}")
    print(f"Diferencia regresiva  : {df_reg}")
    print(f"Diferencia central    : {df_cent}")
    print(f"Derivada exacta       : {df_exacta}\n")

    print("=== ERRORES ===")
    print(f"Error progresivo: {abs(df_prog - df_exacta)}")
    print(f"Error regresivo : {abs(df_reg - df_exacta)}")
    print(f"Error central   : {abs(df_cent - df_exacta)}")
