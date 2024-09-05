n=int(input("Tamaño del vector: "))
a=[0]*n
b=[0]*n
c=[0]*n
mayor=pos=0
print("Cargar vectores")
for i in range(n):
    a[i]=int(input(f"A[{i}]= "))
for i in range(n):
    b[i]=int(input(f"B[{i}]= "))
for i in range(n):
    c[i]=a[i]+b[i]

print("Vector A")
for i in range(n):
    print(a[i],end="|")
print()
print("Vector B")
for i in range(n):
    print(b[i],end="|")
print()
print("Vector C")
mayot=c[0]
for i in range(n):
    print(c[i],end="|")
    if(c[i]>mayor):
        mayor=c[i]
        pos=i
print()
print("Mayor=",mayor,"y posición=",pos)
