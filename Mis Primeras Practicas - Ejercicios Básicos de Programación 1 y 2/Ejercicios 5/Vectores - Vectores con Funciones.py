"""Elabore un programa en phyton que cargue un vector de tamaño N
que cacule el promedio del vector, cuantos estan por encima del
promedio y la suma de menores al promedio.

Nota: Usar funciones definidas por el usuario.

Probar estos datos n=7
                     |12|5|20|14|8|13|12|
"""

#Definir funciones:

def leern(v,n):  #Subprograma que lee los elementos de un vector
    for i in range(n):
        v[i]=int(input(f"v[{i}]: "))
    return v
def escribirn(v,n):  #Subprograma para escribir los elementos del número
    for i in range(n):
        print(v[i],end="|")
    print()
def promedion(v,n): #Subprograma para determinar el promedio de los
    global p        #números el conjunto
    suma=int
    i=int
    suma=0
    for i in range(n):
        suma=suma+v[i]
        p=suma/n
    return p

#subprograma para determinar la cantidad de números mayotes al promedio
#de los números del conjunto

def cantidad_mayor(v,n):
    cant = int
    i=int
    cant=0
    for i in range(n):
        if v[i]>p:
            cant+=1
    return cant
def suma_menores(v,n): #La suma de números menores al promedio de los
    men=int            #números del conjunto
    i=int
    men=0
    for i in range(n):
        if v[i]<p:
            men+=v[i]
    return men

#Declaracion de variables:

v=[]
n=int
promedio=float
n=int(input("Ingrese la cantidad de números del conjunto: "))
v=[0]*n
v=leern(v,n)
print()
print("Vector números")
print()
escribirn(v,n)
promedio=promedion(v,n)
cant=cantidad_mayor(v,n)
suma=suma_menores(v,n)
print()
print("Resultados:")
print()
print(f"""El promedio de los números del vecor es: {promedio}
La cantidad de números mayores al promedio: {cant}
La suma de números menores al promedio: {suma}""")
