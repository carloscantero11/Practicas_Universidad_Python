#Realizar un programa para el siguiente caso:
#Un cliente se dirige a una tienda de alguiler de vehiculos, la cual ofrece los siguientes vehiculos:
#Toyota = 50.000bs Diario
#Fiesta = 30.000bs Diario
#Aveo = 25.000bs Diario
#La tienda ofrece un descuento sobre el monto del alquiler parcial de un 10% siempre y cuando si el vehiculo fue aquilado por
#más de 7 días.
#Imprimir nombre del cliente, nombre del vehiculo, por cuantos dias lo va a llevar y cuanto va a pagar

#Variables:
tv=Map=da=0
nc=vehiculo=""
d=mp=0.0
#Entrada:
nc=str(input("Nombre del cliente:"))
tv=int(input("1)Toyota:50.000bs 2)Fiesta:30.000bs 3)Aveo:25.000bs:"))
da=int(input("Deme días de alquiler:"))
if(tv==1):
    vehiculo="Toyota"
    Map=50000*da
elif(tv==2):
    Vehiculo="Fiesta"
    Map=30000*da
elif(tv==3):
    Vehiculo="Aveo"
    Map=25000*da
if(da>7):
    d=Map*0.10
else:
    d=0
mp=Map-d
print("El cliente",nc,"lleva un",Vehiculo)
print("por",da,"días y va a pagar",mp,"bs")
