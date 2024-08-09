iteraciones = 0
error = None

def main():
    
    res = secante(0, 1, 0.00001)
    
    print("Raiz: " + res)
    print("Iteraciones: " + iteraciones)
    
    return 0

def f(x):
    return 2*x

def errorAbs(viejo, nuevo):
    return abs((nuevo-viejo)/nuevo)*100

def secante(x0, x1, exactitud):
        
    while(error > exactitud):
        xi = x1-((f(x1)*(x0-x1))/(f(x0)-f(x1)))
        
        error = errorAbs(x1,xi)
        
        x0 = x1
        x1 = xi
        
        iteraciones = iteraciones + 1
    
    return x1

if __name__ == "__main__":
    main()