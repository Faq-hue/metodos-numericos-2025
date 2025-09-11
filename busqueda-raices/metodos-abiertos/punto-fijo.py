#Metodo de punto fijo para localizacion de puntos fijos
import math

# aca va la funcion con + x
def g(x):
    #return math.sqrt((10-math.pow(x,3))/(4))
    return math.sqrt(4-x)

# aca va la funcion se deriva sola
def gd(x):
    return (g(x+0.001)-g(x))/0.001

def main():
    x0 = float(input("ingresa x0: "))
    tolerancia = float(input("ingresa la tolerancia: "))
    i = 0
    error = 0

    while(True):
        i = i+1

        # se verifica la convergencia
        if(abs(gd(x0))>= 1):
            print("El metodo no converge")
            return
        
        x1 = g(x0)

        error = abs(x1-x0)

        x0 = x1

        if(error < tolerancia):
            break
    
    print("x1: " + str(x1) + " error: " + str(error) + " iteraciones: " + str(i))

if __name__ == "__main__":
    main()