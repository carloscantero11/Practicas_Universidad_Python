# Realizar un programa que le permita a un vendedor imprimir su nombre y su total a cobrar sabiendo que recibe un 30% de
# comisión de 3 ventas distintas que realiza en el mes. Y su total a cobrar esta formado con esa comisión mas su salario
# básico.

#Variables:
nv=""
tc=sb=v1=v2=v3=0.0
#Entrada:
nc=str(input("Deme su nombre:"))
sb=float(input("Salario Básico:"))
v1=float(input("Venta 1:"))
v2=float(input("Venta 2:"))
v3=float(input("Venta 3:"))
#Proceso:
tc=sb+(v1+v2+v3)*0.30
print("Usted:",nc)
print("Cobra:",tc,"$")
