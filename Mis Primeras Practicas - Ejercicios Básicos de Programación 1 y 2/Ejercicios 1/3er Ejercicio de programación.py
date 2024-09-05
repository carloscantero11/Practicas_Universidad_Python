# Realizar un programa que imprima el nombre de un cliente, el articulo que lleva él, monto del IVA y su total a pagar
# segun lo siguiente:
# El cliente se puede llevar cierta cantidad de articulos de un mismo tipo del cual se conoce su precio unitario. Con esa
# informacion se calcula el monto de la compra parcial. La tienda ofrece un 20% de descuento sobre el monto de la compra
# parcial. Por ley a la compra con descuento se le calcula lo correspondiente al IVA.

#Variables:
nc=ta=" "
ca=pu=map=d=iva=st=tp=0.0
#Entrada:
nc=str(input("Deme su nombre:"))
ta=str(input("Tipo de articulo:"))
ca=float(input("Cantidad de articulos:"))
pu=float(input("Precio unitario:"))
#Proceso:
map=ca*pu
d=map*0.20
st=map-d
iva=st*0.16
tp=st+iva
print(("El cliente:")+str(nc))
print("lleva:",ta)
print("El IVA es:",iva,"Bs")
print("Y va a pagar:",tp,"bs")
