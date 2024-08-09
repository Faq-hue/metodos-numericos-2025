def main():
    pasos = 0
    xp, error = None
    
    x = float(input("Ingrese el x inicial "))
    
    epsilon = float(input("Ingrese el epsilon "))
    
    while(error > epsilon):
        xp = (x - f(x) / derivada(x))
        
        if(derivada(xp) > 1):
            pasos =+ 1
            
            error = (abs(xp - x) / abs(xp)) #error absoluto
            
            #error porcentual = error exacto * 100 /raiz
            
            #error = pow((xp-x), 2)/ pow(x,2) #error relativo
            
            if(pasos == 10):
                print("No hay raices, elija otro intervalo o un error mas pequeño")
                exit
            
            x= xp
        else:
            print("Error de convergencia, inicie con un epsilon mayor")
            exit
            
    print("Raiz: " + str(x))
    print("Cantidad de pasos: " + str(pasos))
    print("Error: " + str(error))
    
    return 0
    
def f(x):
    return -x+2

def derivada(x):
    h = 0.000001
    return ((f(x+h) - f(x)) / h)

if __name__ == "__main__":
    main()