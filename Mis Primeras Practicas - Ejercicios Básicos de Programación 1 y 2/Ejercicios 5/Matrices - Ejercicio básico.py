#Matrices
import random
res="s"
while(res=="s"):
    n=int(input("Filas: "))
    m=int(input("Columnas: "))
    print()
    fila=[0]*n
    col=[0]*m
    notas=[[0]*m for i in range(n)]

    for i in range(n):
        fila[i]=input(f"Datos para la fila {i}: ").upper()
    print()
    for i in range(m):
        col[i]=input(f"Datos para la columna {i}: ").upper()
    print()


        
    for i in range(n):
        for j in range(m):
            notas[i][j]=random.randint(100,999)
    print()
    print("\a Matriz")
    print()
    print(end="| ")
    print("N", end= " | ")
    for i in range(n):
        print(" {0:2}".format(col[i]),end=" | ")
    print()
    
    for i in range(n):
        print(end="| ")
        print("{0:2}".format(fila[i]),end="")
        print(end="| ")
        for j in range(m):
            print("{0:2}".format(notas[i][j]),end=" | ")
        print()
    print()
    res=input("¿Desea otra matriz?   'S'(Sí)   'N'(No): ").lower()
    print()
