#proceso:
n=int(input("Deme un número N PAR y POSITIVO: "))
a=[0]*n
b=[0]*n
c=[0]*n
print()

#Cargar
print("Cargar vectores")
for i in range(n):
    a[i]=int(input(f"A[{i}]= "))
for i in range(n):
    b[i]=int(input(f"B[{i}]= "))
print()

#Imprimir
print("imprimir vectores")
print()
print("Vector A")
print(end="| ")
for i in range(n):
    print(a[i],end=" | ")
print()
print("Vector B")
print(end="| ")

for i in range(n):
    print(b[i],end=" | ")
print()

#Vector resultante
y=0
for i in range(n):
    a[i]
    c[i]+=a[i]
    

    
#Imprimir Vector C
print("Vector C")
print(end="| ")
for i in range(n):
    print(c[i],end=" | ")






