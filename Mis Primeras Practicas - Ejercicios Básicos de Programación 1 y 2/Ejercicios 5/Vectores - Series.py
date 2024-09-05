"""Elabore un programa que calcule la siguiente serie s=1+ 1/2+ 1/3+...1/n
y guarde cada termino de un vector.

si n=4
tenemos termino 1 = 1/1 = 1
termino 2 = 1/2 = 0.5
termino 3 = 1/3 = 0.33

Esos terminos se guardan en un vector y luego mostrara una suma en serie"""

#Ejercicio 1:

print("Ejercicio 1:")
print()

n=int(input("Ingrese valor de n: "))
serie=[0]*n
tss=0.0
for i in range(n):
    serie[i]=1/(1+i)
    tss+=serie[i]
print("Vector termino de series")
for i in range(n):
    print(serie[i],end=" | ")
print()
print(f"Suma de series = {tss}")
print("*"*40)

#Ejercicio 2:

print()
"""Elabore un programa que calcule la siguiente serie:
s= 2x/2! - 3x^2/3! + 4x^3/4! - ......   Y guarde cada termino en un vector

Colocar los siguiestes valores:
Valor de x:3
Valor de n:3
Salida
Vector vector terminos de series
3.00  -4.50    4.50
Sumatoria de series"""

print("Ejercicio 2")
print()

x=int(input("Valor de x: "))
n=int(input("Valor de n: "))
ter= [0]*n
y=1
fact=2
s=0.0

for i in range(n):      
    ter[i]= (-1)**(y+1)*(y+1)*x**y/fact
    s+=ter[i]
    y+=1
    fact=fact*(y+1)
print("Vector terminos de series")
for i in range(n):
    print(ter[i],end=" | ")
print()
print(f"Sumatoria de series {s}")
print("*"*40)
