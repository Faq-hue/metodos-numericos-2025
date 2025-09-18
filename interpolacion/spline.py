import lecturaDatos

A = lecturaDatos.leerMatrizPrincipal("datos.dat")
b = lecturaDatos.leerMatrizResultante("datos2.dat")
   

n = len(A)
A = [fila[:] for fila in A]

k=0
while(k<n-1):
    j=0
    while(j<3):
        a(2*k,4*k+j) = 
