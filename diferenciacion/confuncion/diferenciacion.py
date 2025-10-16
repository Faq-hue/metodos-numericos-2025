import math

def f(x):
    return -0.1*x**4 - 0.15*x**3 - 0.5*x**2 - 0.25*x + 1.2

print("\nDIFERENCIACIÓN DE UNA FUNCIÓN")
x = float(input("Ingrese punto a derivar: "))
h = float(input("Ingrese h: "))

while True:
    print("\nOPCIONES")
    print("1. Derivación por derecha (hacia delante)")
    print("2. Derivación centrada")
    print("3. Derivación por izquierda (hacia atrás)")
    print("0. Para salir")
    op = int(input("Opción: "))

    if op == 0:
        print("SALIDA!")
        break

    print("\nOPCIONES")
    print("1. Derivada Primera")
    print("2. Derivada Segunda")
    print("3. Derivada Tercera")
    print("4. Derivada Cuarta")
    op1 = int(input("Opción: "))

    # --- Derivación por derecha ---
    if op == 1:
        if op1 == 1:
            aprox = (f(x+h)-f(x))/h
            print(f"\nLa derivada primera por la DERECHA de f({x})={aprox}, error O({h})")
            aprox = (-f(x+2*h)+4*f(x+h)-3*f(x))/(2*h)
            print(f"La derivada primera por la DERECHA de f({x})={aprox}, error O({h}²)")
        elif op1 == 2:
            aprox = (f(x+2*h)-2*f(x+h)+f(x))/h**2
            print(f"\nLa derivada segunda por la DERECHA de f({x})={aprox}, error O({h})")
            aprox = (-f(x+3*h)+4*f(x+2*h)-5*f(x+h)+2*f(x))/h**2
            print(f"La derivada segunda por la DERECHA de f({x})={aprox}, error O({h}²)")
        elif op1 == 3:
            aprox = (f(x+3*h)-3*f(x+2*h)+3*f(x+h)-f(x))/h**3
            print(f"\nLa derivada tercera por la DERECHA de f({x})={aprox}, error O({h})")
            aprox = (-3*f(x+4*h)+14*f(x+3*h)-24*f(x+2*h)+18*f(x+h)-5*f(x))/(2*h**3)
            print(f"La derivada tercera por la DERECHA de f({x})={aprox}, error O({h}²)")
        elif op1 == 4:
            aprox = (f(x+4*h)-4*f(x+3*h)+6*f(x+2*h)-4*f(x+h)+f(x))/h**4
            print(f"\nLa derivada cuarta por la DERECHA de f({x})={aprox}, error O({h})")
            aprox = (-2*f(x+5*h)+11*f(x+4*h)-24*f(x+3*h)+26*f(x+2*h)-14*f(x+h)+3*f(x))/h**4
            print(f"La derivada cuarta por la DERECHA de f({x})={aprox}, error O({h}²)")

    # --- Derivación centrada ---
    elif op == 2:
        if op1 == 1:
            aprox = (f(x+h)-f(x-h))/(2*h)
            print(f"\nLa derivada primera CENTRADA de f({x})={aprox}, error O(h²)")
            aprox = (-f(x+2*h)+8*f(x+h)-8*f(x-h)+f(x-2*h))/(12*h)
            print(f"La derivada primera CENTRADA de f({x})={aprox}, error O(h⁴)")
        elif op1 == 2:
            aprox = (f(x+h)-2*f(x)+f(x-h))/h**2
            print(f"\nLa derivada segunda CENTRADA de f({x})={aprox}, error O(h²)")
            aprox = (-f(x+2*h)+16*f(x+h)-30*f(x)+16*f(x-h)-f(x-2*h))/(12*h**2)
            print(f"La derivada segunda CENTRADA de f({x})={aprox}, error O(h⁴)")
        elif op1 == 3:
            aprox = (f(x+2*h)-2*f(x+h)+2*f(x-h)-f(x-2*h))/(2*h**3)
            print(f"\nLa derivada tercera CENTRADA de f({x})={aprox}, error O(h²)")
            aprox = (-f(x+3*h)+8*f(x+2*h)-13*f(x+h)+13*f(x-h)-8*f(x-2*h)+f(x-3*h))/(8*h**3)
            print(f"La derivada tercera CENTRADA de f({x})={aprox}, error O(h⁴)")
        elif op1 == 4:
            aprox = (f(x+2*h)-4*f(x+h)+6*f(x)-4*f(x-h)+f(x-2*h))/h**4
            print(f"\nLa derivada cuarta CENTRADA de f({x})={aprox}, error O(h²)")
            aprox = (-f(x+3*h)+12*f(x+2*h)+39*f(x+h)+56*f(x)-39*f(x-h)+12*f(x-2*h)+f(x-3*h))/(6*h**4)
            print(f"La derivada cuarta CENTRADA de f({x})={aprox}, error O(h⁴)")

    # --- Derivación por izquierda ---
    elif op == 3:
        if op1 == 1:
            aprox = (f(x)-f(x-h))/h
            print(f"\nLa derivada primera por la IZQUIERDA de f({x})={aprox}, error O(h)")
            aprox = (3*f(x)-4*f(x-h)+f(x-2*h))/(2*h)
            print(f"La derivada primera por la IZQUIERDA de f({x})={aprox}, error O(h²)")
        elif op1 == 2:
            aprox = (f(x)-2*f(x-h)+f(x-2*h))/h**2
            print(f"\nLa derivada segunda por la IZQUIERDA de f({x})={aprox}, error O(h)")
            aprox = (2*f(x)-5*f(x-h)+4*f(x-2*h)-f(x-3*h))/h**2
            print(f"La derivada segunda por la IZQUIERDA de f({x})={aprox}, error O(h²)")
        elif op1 == 3:
            aprox = (f(x)-3*f(x-h)+3*f(x-2*h)-f(x-3*h))/h**3
            print(f"\nLa derivada tercera por la IZQUIERDA de f({x})={aprox}, error O(h)")
            aprox = (5*f(x)-18*f(x-h)+24*f(x-2*h)-14*f(x-3*h)+3*f(x-4*h))/(2*h**3)
            print(f"La derivada tercera por la IZQUIERDA de f({x})={aprox}, error O(h²)")
        elif op1 == 4:
            aprox = (f(x)-4*f(x-h)+6*f(x-2*h)-4*f(x-3*h)+f(x-4*h))/h**4
            print(f"\nLa derivada cuarta por la IZQUIERDA de f({x})={aprox}, error O(h)")
            aprox = (3*f(x)-14*f(x-h)+26*f(x-2*h)-24*f(x-3*h)+11*f(x-4*h)-2*f(x-5*h))/h**4
            print(f"La derivada cuarta por la IZQUIERDA de f({x})={aprox}, error O(h²)")
