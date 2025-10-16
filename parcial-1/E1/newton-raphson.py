# Metodo de Newton-Raphson para encontrar raices

import math

#aca pongo la funcion
def f(x):
    #return pow(x,3)+4*pow(x,2)-10
    #return (x*(16-2*x)*(10-2*x))-100
    #return x*math.cosh(12/x)-x-5
    #return 10*pow(x,2)-(pow(x,3)/3)-850.66
    return ((x+1)/(x+4))-(0.25*x)

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
        errorporc = (abs(x1-x0))/(0.5*(x1+x0))*100

        x0 = x1

        # salgo si el error es menor a la tolerancia o si hago 1000 o mas iteraciones
        if(error < tolerancia or i >= 1000):
            break

    print("x1: "+ str(x1))
    print(" f(x1)= " + str(f(x1)))
    print(" error estimado = " + str(error)) 
    print("error porcentual= "+str(errorporc) + "%")
    print(" iteraciones: " + str(i))


if __name__ == "__main__":
    main()