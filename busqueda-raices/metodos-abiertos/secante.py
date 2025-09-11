# Metodo de la secante para encontrar raices

# defino la funcion
def f(x):
    return x

def main():
    x0 = float(input("Ingresa x0: "))
    x1 = float(input("Ingresa x1: "))
    tolerancia = float(input("Ingresa tolerancia: "))

    i,error = 0

    while(True):
        i = i+1
        
        x2 = x1-((f(x1)*(x1-x0))/(f(x1)-f(x0)))

        error = abs(x2-x1)

        x0 = x1

        x1 = x2

        if(error < tolerancia or i >= 1000):
            break

        print("x2: "+ str(x2) +  " error= " + str(error) + " iteraciones: " + str(i))
