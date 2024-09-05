#Inicializamos variables

precio = [0] * 20
sucursal = [[0]*3 for i in range(4)]
cantidad = [[0]*3 for i in range(4)]
cantidad_total = total2 = mayor = 0
totalempresa = totalsucursal = 0.0
l=1

#Entrada de datos

for i in range(3):  #Precio de Articulos
    precio[i] = float(input("Precio de articulo %d: "%(i+1)))

print()


for i in range(4):   #Cantidad de articulos por sucursal
    print("\nSucursal",(i+1),"\n")
    for j in range(3):
        cantidad[i][j] = int(input("Cantidad de articulo %d: "%(j+1)))
        cantidad_total += cantidad[i][j]

#(1)Cantidad total
print()
print("Cantidad total de de cada articulo:", cantidad_total)  
print()

for i in range(3):     #Cantidad de articulos en la sucursal 2
    total2 += cantidad[1][j]
    
#(2)La cantidad de artículos en la sucursal 2.
print("La cantidad de artículos en la sucursal 2:",total2)
print()

#La cantidad del articulo 3 en la sucursal 1.

print("La cantidad del articulo 3 en la sucursal 1:",cantidad[0][2])

for i in range(4):           #Total de cada sucursal, la empresa y mayor recaudacion
    for j in range(3):
        totalsucursal += (cantidad[i][j] * precio[i])
        
    print(f"Recaudacion total de sucursal {l}:", totalsucursal)
    l+=1
    if(totalsucursal > mayor):
        mayor = totalsucursal
        mmayor = i+1

    totalempresa += totalsucursal
    totalsucursal *= 0

print(f"\nTotal de la Empresa: {totalempresa} \n")
print(f"La sucursal de mayor recaudación: {mmayor}")
