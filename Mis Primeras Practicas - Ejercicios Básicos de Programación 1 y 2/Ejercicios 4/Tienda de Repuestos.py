#Desarrolle un programa en Python que permita contabilizar las
#ventas de una tienda de repuestos para vehiculos
#Considere 5 productos: Bateria, bobina, bujias, arranque,
#disco de frenos. 
#Determine:

#1. Promedio de ventas de productos
#2. Cantidad total de ventas por productos
#3. Monto total por color del vehiculo
#4. Monto total de ventas.

#Datos:

print("")
print("Tienda de Repuesdos María Gabriela")
print("")
b=int(input("Cantidad de baterias vendidas: "))
bv=int(input("Precio de baterias: "))
bo=int(input("Cantidad de bobinas vendidos: "))
bov=int(input("Precio de bobinas: "))
bu=int(input("Cantidad de bujias vendidos: "))
buv=int(input("Precio de bujias: "))
a=int(input("Cantidad de arranques vendidos:"))
av=int(input("Precio de arranques: "))
d=int(input("Cantidad de disos de Freno vendidos: "))
dv=int(input("Precio de discos de frenos: "))
print("")
print("")

#Condiciones:

print("Elija con un número el color del vehiculo:")
print("")
c=int(input("(1)Negro.  (2)Blanco.  (3)Azul.  (4)Rojo.  (5)Dorado.  (6)Gris. : "))

if(c==1):
    f=int(input("Cantidad total por el color negro: "))
    n="negro"
if(c==2):
    f=int(input("Cantidad total por el color blanco: "))
    n="blanco"
if(c==3):
    f=int(input("Cantidad total por el color azul: "))
    n="azul"
if(c==4):
    f=int(input("Cantidad total por el color rojo: "))
    n="rojo"
if(c==5):
    f=int(input("Cantidad total por el color dorado: "))
    n="dorado"
if(c==6):
    f=int(input("Cantidad total por el color gris: "))
    n="gris"

#Procedimiento y resultado:
    
print("")
print("")
print("Resultados:")
print("")

A=b*bv
B=bo*bov
C=bu*buv
D=a*av
E=d*dv
pt=(A+B+C+D+E)/5
ct=b+bo+bu+a+d
mt=(A+B+C+D+E)

print(("Promedio total de ventas:"),pt,"$")
print(("Cantidad total de ventas por productos:"),ct)
print(("La cantidad total por el color"),n,("es:"),f)
print(("Monto total de ventas:"),mt,"$")
