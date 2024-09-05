#Suma de Matrices
import random
n=int(input("Fila: "))
m=int(input("Columna: "))

matriz=[]
matriz=[[0]*m for i in range(n)]
matriz1=[[0]*m for i in range(n)]
suma=[[0]*m for i in range(n)]
sfila=[0]*n

for i in range(n):
    for j in range(m):
        matriz[i][j]= random.randint(1,9)

        matriz1[i][j]= random.randint(1,9)   #Random.uniform
        suma[i][j]=matriz[i][j]+matriz1[i][j]#Es solo para decimales
        sfila[i]+=suma[i][j]

print("matriz 1")
for i in range(n):
    print(end="| ")
    for j in range(m):
        print(matriz[i][j],end=" | ")
    print()

print("matriz 2")
for i in range(n):
    print(end="| ")
    for j in range(m):
        print(matriz1[i][j],end=" | ")
    print()
    
print("Matriz suma y Total de la fila")
for i in range(n):
    print(end="| ")
    for j in range(m):
        print(suma[i][j],end=" | ")
    print(sfila[i])
