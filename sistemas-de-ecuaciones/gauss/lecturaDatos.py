filas = 0
max_columnas = 0

def leerMatrizPrincipal(archivo):
    print(archivo)
    try:
        with open(archivo, 'r') as f:
            lineas = f.readlines()
    except FileNotFoundError:
        print("No se puede abrir el archivo")
        return [], 0, 0

    matriz = []
    max_columnas = 0

    for linea in lineas:
        if linea.strip():
            numeros = [float(num) for num in linea.strip().split()]
            matriz.append(numeros)
            if len(numeros) > max_columnas:
                max_columnas = len(numeros)

    filas = len(matriz)
    
    #imprimirMatrizPrincipal(matriz)

    #gauss seidel y jacobi
    #return matriz, filas, max_columnas
    
    #eliminacion gaussiana
    return matriz


def imprimirMatrizPrincipal(matriz):
    for fila in matriz:
        print(" ".join(f"{num:.6f}" for num in fila))

def leerMatrizResultante(archivo):
    try:
        with open(archivo, 'r') as f:
            lineas = f.readlines()
    except FileNotFoundError:
        print("No se puede abrir el archivo")
        return []

    vector = []
    for linea in lineas:
        if linea.strip():
            numeros = [float(num) for num in linea.strip().split()]
            vector.extend(numeros)

    #imprimirMatrizPrincipal([vector])  # Imprimir como una fila para consistencia

    return vector

