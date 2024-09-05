#Carlos Cantero
#26.803.874
#Programción II
#Sección: 1031B

print("""2. Cargar un vector llamado Semana  que guarde  el número de  semanas en   un  Mes   Cualquiera   
(1 mes tiene 4 o 5 semanas) y una matriz llamada temperatura, en donde la estructura registrara la temperatura diaria (7 días) (Lunes, Martes, Miércoles, Jueves, Viernes, Sábado, Domingo) de una Supermercado, estos oscilan entre los 5 y 40 grados. Deberá llenar la matriz de forma aleatoria para el mes de Diciembre donde el primer día inicia en lunes y el último (31) se ubica en el miércoles. Se nos pide hacer lo siguiente:
       • Obtener la temperatura más alta y baja de la semana y que día se produjo (lunes, martes,     etc.).
       •  Promedio temperatura de la semana.
       • Temperatura más alta del mes y su día.

""")

import random
print("Programa:")
print()
#datos:
mes=input("Elija un mes: ").upper()
fila=[0]*5
col=[0]*7
matriz=[[0]*7 for i in range(5)]
matriz1=[[0]*7 for i in range(5)]
band=0
nom = mnom = ""
total = mtotal = 0

for i in range(5):
    fila[i]=i
print()
for i in range(7):
    col[i]=input(f"Escriba los dias de la semana: ").upper()
print()
for i in range(5):
    for j in range(7):
        matriz[i][j]=int(input(f"Temperatura del supermercado (min=5,max=40) ; |dia({j});semana({i})| : "))


print("\n                      ",mes)
print()
d="Sem/Dia"
print("{0:5}".format(d),end=" ")
for i in range(7):
    print("{0:5}".format(col[i]),end=" ")
print()
for i in range(4):
    print("{0:4}".format(fila[i]),end=" ")
    for j in range(7):
        print("{0:6}".format(matriz[i][j]),end="  ")
    print()
print()


for i in range(5):
    for j in range(7):
        matriz1[i][j]=random.randint(5,40)


print()
print("                       DICIEMBRE")
print()
d="Sem/Dia"
print("{0:5}".format(d),end=" ")
for i in range(7):
    print("{0:5}".format(col[i]),end=" ")
print()
for i in range(4):
    print("{0:4}".format(fila[i]),end=" ")
    for j in range(7):
        print("{0:6}".format(matriz1[i][j]),end="  ")
    print()
print()


