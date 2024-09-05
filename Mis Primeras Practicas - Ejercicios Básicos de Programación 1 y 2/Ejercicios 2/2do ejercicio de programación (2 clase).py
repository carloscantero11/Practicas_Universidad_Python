#Realizar un programa que pida 2 números enteros y que los divida.
n1=int(input("Deme un número:"))
n2=int(input("deme otro número:"))
if(n2==0):
    print("No existe")
else:
    d=n1/n2
    print("División",d)
