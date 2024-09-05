"""Elabore un programa que guarde la serie de la suma s= 1 + 1/2 + 1/3 +...
Y que muestre un vector llamado termino que se guarde en cada posición el
resultado que lo imprima y que adicionalmente muestre la suma de la serie"""

#Ejercicio 1:
print("Ejercicio 1")
print()
n=int(input("Tamaño del vector: "))
ter=[]
termino=[0]*n
ss=ter=0.0
for i in range(n):
    ter=1/(i+1)
    termino[i]=ter
    ss+=termino[i]
print("Vector termino")
print(end="| ")
for i in range(n):
    print(termino[i],end=" | ")
print()
print(f"Suma de serie = {ss}")
print()

#Funciones
print("Ahora con Funciones")
print()

def sumatoria():
    for i in range(n):
        global ss
        ter=1/(1+i)
        termino[i]=ter
        ss+=termino[i]
def mostrar():
    print(end="| ")
    for i in range(n):
        print(termino[i],end=" | ")
    print()
n=int(input("Tamaño del vector: "))
ter=[]
termino=[0]*n
ss=ter=0.0
print("Vector termino")
sumatoria()
mostrar()
print(f"Suma de series: {ss}")

#Ejercicio 2:
print()
print("Ejercicio 2")
print()
import random
print("""Elabore  un programa que cargue un número de forma aleatoria
entre 2 y 8, y que se guarde en un vetor llamado factorial""")
print()

factorial=[0]*7
aux=[0]*7

for i in range(7):
    n=random.randint(2,8)
    fact=1
    print("El número elegido es el = ",n)
    for j in range(n):
        fact=fact*(j+1)
    factorial[i]=fact
    for j in range(n):
        aux[i]=n
        factorial[i]=fact
    print(f"""Número = {n}
Factorial = {factorial[i]}""")
    print()
print()
print("Otra salidad del vector:")
print()
print("Vector valor de n")
print(end="| ")
for j in range(7):
    print(aux[j],end=" | ")
print()
print("Vecto r factorial")
print(end="| ")
for j in range(7):
    print(factorial[j],end=" | ")
