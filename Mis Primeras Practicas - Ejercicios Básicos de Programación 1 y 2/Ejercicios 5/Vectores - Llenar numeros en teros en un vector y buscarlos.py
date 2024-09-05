"""1) Realizar un programa que permita llenar un vector con 10 números
enteros positivos y los muestre.

2) Al programa anterior agregar el código necesario para que valide que los
números introducidos sean enteros entre 50 y 175.

3) Agregue, al ejercicio anterior, el fragmento de código que permita al
usuario una vez introducidos los 10 números consultar si en el vector se
encuentra almacenado un X. Usar busqueda secuencial"""

#Ejercicio:
import random
vec1=[0]*10
vec2=[0]*10
cant=0
for i in range(10):
    vec1[i]=random.randint(1,200)
    if(vec1[i]>=50)and(vec1[i]<=175):
        vec2[cant]=vec1[i]
        cant+=1
print("Vector 1")
print(end="| ")
for i in range(10):
    print(vec1[i],end=" | ")
print()
print()
print("Vector 2")
print(end="| ")
for i in range(cant):
    print(vec2[i],end=" | ")
print()
print()
print("Otra manera:")
print()
vec3=[0]*10
vec4=[0]*10
band=0
cant1=0
for i in range(10):
    num=int(input("Deme un número positivo: "))
    if(num>0):
        vec3[i]=num
    else:
        num=int(input("El número debe ser positivo: "))
        if(num>0):
            vec3[i]=num
        else:
            print("Buen papi, por bruja se daño el programa")
            band=1
            break
    if(vec3[i]>=50)and(vec3[i]<=175):
        vec4[cant1]=vec3[i]
        cant1+=1
print()
if band==0:
    print("Vector 3")
    print(end="| ")
    for i in range(10):
        print(vec3[i],end=" | ")
    print()
    if(cant1!=0):
        print("Vector 4")
        print(end="| ")
        for i in range(cant1):
            print(vec4[i],end=" | ")
    else:
        print("No hay valores en el intervalo 50 y 175")
    print()

print()
print("Busqueda de un vector:")
print()
x=int(input("Deme valor a buscar en el vector: "))
for i in range(10):
    if(x==vec3[i]):
        print(x,"Esta en la posición:",i)
