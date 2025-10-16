# Metodo de biseccioin para encontrar raices en un intervalo [a,b]
import math
import numpy as np


def f(x):
    #return (pow(x,10)-1)
    #return ((9.81*x)/14)*(1-pow(math.e,(-14/x)*7))-35
    #return ((np.log(x)-(1-(1/x)))/(np.log(x)+((1-1/x)/(2/3))))-0.3
    return (x+1)/(x+4)-(0.25*x)

def biseccion(a,b,tolerancia):

    i = 0
    c = a
    error = 1

    if((f(a)*f(b))>0):
        print("No hay raiz en el intervalo")
        return

    cviejo = a

    while(True):
        c = (a+b)/2
        i= i + 1

        if((f(a)*f(c))>0):
            a = c
        else:
        #elif((f(a)*f(c))<0):
            b = c

        #else:
         #   break

        error = abs(c-cviejo)
        errorporcentual = (abs(c-cviejo)/abs(cviejo))*100

        errorestimado = (abs(c-cviejo))/(0.5*(c+cviejo))*100

        cviejo = c

        if(error < tolerancia):
            break

    print("la raiz es " + str(c))
    print("con un error porcentual de " + str(errorporcentual) + "%")
    print("con un error estimado de " + str(errorestimado))
    print("tardo " + str(i) + " repeticiones")
    return 0


def main():
    biseccion(1.75,3.2,0.01)

if __name__ == "__main__":
    main()