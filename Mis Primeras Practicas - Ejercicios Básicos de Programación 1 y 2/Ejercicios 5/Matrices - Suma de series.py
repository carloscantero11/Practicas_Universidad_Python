"""Determina la suma de la siguiente serie"""
#  S= 1 + 1/2 + 1/3 + 1/4 +...+ 1/n

"""Se debe cargar una matriz cuadrada de numeros aleatorios que
indicaran hasta donde se realizara la suma de esa serie. imprimir esa
matriz llamada suma de serie y muestre la suma por filas guardada en
un vector"""

import random

res=True
while res==True:
    n=int(input("Ingrese el tamaño de matriz numero de n*n: "))
    matriz=[0]
    matriz=[[0]*n for i in range(n)]
    ss=[[0]*n for i in range(n)]
    stt=0.0
    sf=[0]*n

    for i in range(n):
        for j in range(n):
            y=1
            st=0.0
            matriz[i][j]=random.randint(1,8)
            while(y<=matriz[i][j]):
                ss[i][j]+=1/(y)
                sf[i]+=1/(y)
                y+=1
            #stt+=st
    print("Matriz valor final serie")

    for i in range(n):
        print(end="| ")
        for j in range(n):
            print(matriz[i][j],end=" | ")
        print()
    print()
    
    print("Matriz suma termino de cada numero \nLa ultima es la suma de fila\n")
    for i in range(n):
        print(end="| ")
        for j in range(n):
            print("{0:2.2f}".format(ss[i][j]),end=" | ")
        print("{0:2.2f}".format(sf[i]))

    for i in range(n):
        for j in range(n):
            st+=ss[i][j]
    print("Suma de matriz termino {0:2.2f}".format(st))
    r="s"
    while(r=="s"):
        x=int(input("Pruebe el número de la matriz: "))
        j=1
        ps=0.0
        while(j<=x):
            ter=1/j
            ps+=ter
            j+=1
        print("{0:2.2f}".format(ps))
        r=input("Desea probar con otro numero de la matriz s/n: ").lower()

    res=input("Desea otra suma de serie s/n: ").lower()
    if(res=="s"):
        res=True
    else:
        res=False
