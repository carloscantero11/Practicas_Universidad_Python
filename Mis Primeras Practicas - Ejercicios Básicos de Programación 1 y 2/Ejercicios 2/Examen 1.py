"""1)Una tienda para realizar una venta a un cliente en
     específico debe pedir por teclado la cantidad de artículos
     comprados y su precio unitario de esta manera se consigue
     cual es el monto de la compra, posteriormente se le aplica
     un descuento según las siguientes políticas:

   - Para cantidad de artículos  de más de 500 unidades y monto
     de la compra menor o igual a 50000 tendrá un descuento del
     5% sobre elmonto de la compra.

   - Para cantidad de artículos  de más de 500 unidades y monto
     de la compra mayor  que 50000 y menor o igual a 100000
     tendrá un descuento del 8% sobre el monto de la compra.

   - Para cantidad de artículos  de más de 500 unidades y monto
     de la compra mayor a 100000 tendrá un descuento del 12%
     sobre el monto de la compra.
     
   - Si la venta no satisface ninguno de estos requerimientos el
     descuento será solo del 2%.

     Realizar un algoritmo que permita mostrar el nombre del
     cliente y el monto total a pagar por el cliente."""

#Versión 1.0
"""pu=x=ac=z=0.0
nc=str(input("Su nombre:"))
ac=float(input("Cuantos articulos compro:"))
pu=float(input("Precio de los articulos:"))
z=ac*pu
if(ac>500):
    if(5000<=pu):
        x=z*0.05
    elif(5000>pu<=10000):
        x=z*0.08
    elif(10000>pu):
        x=z*0.12
else:
    x=z*0.02
pt=z-x
print("El cliente",nc,"lleva",ac,"articulos")
print("Al precio",pu,"su monto total a pagar es:",pt)"""


#Declaramos Variables
art = 0
precio = compra = descuento = total = 0.0
name = ""

#Datos de Entrada:
name = input("Nombre del cliente: ")
art = int(input("Cantidad de articulos comprados: "))
precio = float(input("Precio unitario: "))

#Proceso
compra = art * precio
print(f"\nTotal de compra sin descuento: {compra} $")

if(art>500):
    if(compra<=50000):
        descuento = compra * 0.05
        
    elif(compra>=50000)and(compra<=100000):
        descuento = compra * 0.08

    elif(compra>100000):
        descuento = compra * 0.12

else:
    descuento = compra *0.02

total = compra - descuento

print("Descuento:",descuento,"$")

print("-------------------------------------------------------------")

print(f"""\nNombre del cliente:   {name}
Monto total a pagar:  {total} $""")

