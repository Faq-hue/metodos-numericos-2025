def main():
    iteracion = 0
    
    a = float(input("Ingrese el valor inicial "))
    errorMinimo = float(input("Ingrese el valor del error esperado (e) "))
    
    error = errorMinimo +1
    
    x = a
    
    while(error > errorMinimo):
        iteracion = iteracion + 1
        
        if(abs(derivada(x))>1):
            print("El metodo no converge porque la derivada de g(x) en a es mayor o igual a 1")
            exit
        
        x1 = g(x)
        
        error = abs(x-x1)
        
        x = x1
        
        print("Iteracion: " + str(iteracion))
        print("Error: " + str(error))
        
    print("Raiz: " + x)
    
    return 0

def f(x):
    return 3*x

def g(x):
    return 2*x

def derivada(x):
    h = 0.00001
    return (g(x+h)-g(x))/h

if __name__ == "__main__":
    main()