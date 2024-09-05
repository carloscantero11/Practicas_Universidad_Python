"""Vector resultante C intercalado"""

#Funciones:

def carga_vectores():
    for i in range(n):
        a[i]=int(input(f"A[{i}]= "))
    for i in range(n):
        b[i]=int(input(f"B[{i}]= "))
def imprimir_vectores():
    print()
    print("Vector A")
    for i in range(n):
        print(a[i],end="|")
    print()
    print("Vector B")
    for i in range(n):
       print(b[i],end="|")
def calculos_vectores():
    y=0
    for i in range(n):
        c[y]=a[i]
        y+=1
        c[y]=b[i]
        y+=1

#Proceso:

n=int(input("Deme el valor de n: "))
a=[]
a=[0]*n
b=[]
b=[0]*n
c=[]
c=[0]*n*2
carga_vectores()
imprimir_vectores()
calculos_vectores()
print()
print("Vector resultante C intercalado")
for i in range(n*2):
    print(c[i],end="|")
