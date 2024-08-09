

def main():
    errorAbsoluto = 0
    a = float(input("ingrese el parametro a del intervalo "))
    b = float(input("ingrese el parametro b del intervalo "))
    tolerancia = float(input("ingrese el error minimo "))
    
    if(f(a) * f(b) > 0):
        print("no hay raices o tiene raices pares")
        return 0
        
    anterior = 0
    
    iteracion = 0
    
    errorAbsoluto = (b-a)/2
    
    c = 1000
    
    while(errorAbsoluto > tolerancia):
        iteracion = iteracion +1
        #c = float(puntoMedioRegulaFalsi(a,b))
        c = float(puntoMedioBiseccion(a,b))
        
        if(f(a) * f(c) > 0):
            a = c
        elif(f(b) * f(c) > 0):
            b = c
        else:
            break
        
        errorAbsoluto = abs(c - anterior)
        anterior = c

    print("la raiz es:" + str(c) +" y en " + str(iteracion) + " iteraciones")    
    return 0

def f(x):
    x = float(x)
    return (-2)+(7*x)-(5*pow(x,2))+(6*pow(x,3))
    #return pow(x,10) - 1

def puntoMedioBiseccion(a, b):
    return ((a+b)/2)

def puntoMedioRegulaFalsi(a,b):
    return (a*f(b) - b*f(a))/(f(b)-f(a))

if __name__ == "__main__":
    main()