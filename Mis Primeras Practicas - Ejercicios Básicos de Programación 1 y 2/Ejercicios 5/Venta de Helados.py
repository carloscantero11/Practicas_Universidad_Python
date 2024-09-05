#Carlos Cantero  C.I: 26.803.874   #Sección: 1031B
#Ingenieria en computación

#Ejercicio 1

print("*****************Lista de precios*****************")
print("""
           Pequeño   Mediana  Familiar
Corriente    8$        7$       10$
Especial     10$       12$      13$
Super        12$       14$      16$
""")

print()
print()
precio=tprecio=0
fp=0
iva=0.0
total=0.0
res="s"
while(res=="s"):
    tipo=input("Tipo de helado (C ; E ; S): ").upper()
    tamaño=input("Tamaño del helado (P ; M ; F): ").upper()

                    
    if(tipo=="C")and(tamaño=="P"):
        precio=8
    if(tipo=="C")and(tamaño=="M"):
        precio=7
    if(tipo=="C")and(tamaño=="F"):
        precio=10
    if(tipo=="E")and(tamaño=="P"):
        precio=10
    if(tipo=="E")and(tamaño=="M"):
        precio=12
    if(tipo=="E")and(tamaño=="F"):
        precio=13
    if(tipo=="S")and(tamaño=="P"):
        precio=12
    if(tipo=="S")and(tamaño=="M"):
        precio=12
    if(tipo=="S")and(tamaño=="F"):
        precio=16
    tprecio+=precio
    res=input("¿Desea hacer otro pedido?   'S'(Sí)   'N'(No): ").lower()
    print()

print()
print("""Elija con un número la forma de pago
(1)  Efectivo               IVA: 16%
(2)  Pago electronico       IVA: 14%
""")
fp=int(input())

if(fp==1):
    iva=tprecio*0.16
else:
    iva=tprecio*0.14

total= tprecio+iva

print(f"""
Precio total de los helados:     {tprecio}
IVA:                             {iva}
Total de la compra:              {total}""")
