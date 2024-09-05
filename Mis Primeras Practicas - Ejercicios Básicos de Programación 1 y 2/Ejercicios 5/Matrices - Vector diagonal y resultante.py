"""Elabore un programa en Pyton que cargue una matriz cuadrada de
4*4 de manera aleatoria y que calcule y muestre la matriz mayor y
menor de la matriz con su posición, un vector principal que guarde
elemntos diagonal principal, , un vector secuandario que guarde los
elementos diagonal secundaria, un vector resultante que guarde la
suma de la principal y secundaria, y de ese vector muestre la suma
de tods los digitos y cantidad de digitos pares"""

#Proceso:
import random

matriz=[[0]*4 for i in range(4)]
vdp=[0]*4
vds=[0]*4
vr=[0]*4
mayor=menor=pfma=pcma=pfme=pcme=sd=cdp=0

print("Carga de la matriz")
for f in range(4):
    for c in range(4):
        matriz[f][c]=random.randint(10,70)
mayor=matriz[0][0]
menor=matriz[0][0]
for f in range(4):
    for c in range(4):
        if(f==c):
            vdp[f]=matriz[f][c]
        if(f+c==3):
            vds[f]=matriz[f][c]
        vr[f]=vdp[f]+vds[f]
        if(matriz[f][c]>mayor):
            mayor=matriz[f][c]
            pfma=f
            pcma=c
        if(matriz[f][c]<menor):
            menor=matriz[f][c]
            pfme=f
            pcme=c
for f in range(4):
    aux=vr[f]
    while(aux!=0):
        dig=aux%10
        sd+=dig
        if(dig%2==0):
            cdp+=1
        aux//=10

print("Imprimir matriz")
print()

for f in range(4):
    print(end=" | ")
    for c in range(4):
        print(matriz[f][c],end=" | ")
    print()
print()
print(f"""Mayor de la matriz: {mayor}
Fila: {pfma}   Columna: {pcma}

Menor de la matriz: {menor}
Fila: {pfme}   Columna: {pcme}

Vector diagonal principal:""")
print(end="| ")
for f in range(4):
    print(vdp[f],end=" | ")
print()
print()
print("Vector diagonal secundaria:")
print(end="| ")
for f in range(4):
    print(vds[f],end=" | ")
print()
print()
print("Vector resultante:")
print(end="| ")
for f in range(4):
    print(vr[f],end=" | ")
print()
print()
print(f"""Suma total de digitos vector resultante: {sd}
Tiene: {cdp} digitos pares""")
