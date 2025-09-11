# Metodo de Newton-Raphson para encontrar raices

import math

#aca pongo la funcion
def f(x):
    return pow(x,3)+4*pow(x,2)-10

#aca pongo la derivada exacta o dejo la primitiva como esta
def fd(x):
    return (f(x+0.001)-f(x))/0.001

def main():
    x0 = float(input("ingrese x0: "))
    tolerancia = float(input("ingrese tolerancia: "))
    i = 0
    error = 0

    while(True):
        i = i+1
        
        # compruebo si la derivada es demasiado pequeña
        if(abs(fd(x0))<0.00001):
            print("Derivada muy pequeña")
            return
        
        x1 = x0 - (f(x0)/fd(x0))

        error = abs(x1-x0)

        x0 = x1

        # salgo si el error es menor a la tolerancia o si hago 1000 o mas iteraciones
        if(error < tolerancia or i >= 1000):
            break

    print("x1: "+ str(x1) + " f(x1)= " + str(f(x1)) + " error= " + str(error) + " iteraciones: " + str(i))


if __name__ == "__main__":
    main()