def f(x):
    return x

def main():
    sum = 0
    
    #valor inferior del intervalo
    a = 0

    #valor superior del intervalo
    b = 1

    #cantidad de intervalos
    n = 6

    h = (b-a)/n

    i = 1

    for i in n-1:
        x= a+i*h
        sum = sum +f(x) 

    aprox = (h/2)*(f(a)+f(b)+2*sum)
    print("La integral f(x) en el intervalo [" + str(a) + ";" + str(b) + "] es: " + str(aprox))
    
