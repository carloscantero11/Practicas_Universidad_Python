"""
Una compañia de muebles de fabrica butacas mecedoras y sillas y cada una de
ellasde 3 modelos E (economico) M (medio) y L (lujo) cada mes produce
los modelos de butacas: E=20 M=15 y L=10. Modelos de mecedora: E=12 M=8
L=5. Modelos de sillas: E=18 M=20 L=12.
Representar una informacion en una matri y calcular la produccion de un año

            E   M  L
Butacas     20 15 10
Mecedoras   12  8  5
Sillas      18 20 12

"""

#Inicializamos variables
tipo = []
produccion_inicial = [[]]
modelo = []
sf = [0]*3
tipo = [0]*3
modelo = [0]*3
produccion_inicial = [[0]*3 for i in range(3)]
produccion_final = [[0]*3 for i in range(3)]
suma = [[0]*3 for i in range(3)]
produccion_periodo=0
produccion_mensual=0


#Entrada de datos
print("""Fabrica de butacas, mecedoras y sillas
  """)
for f in range(3):
    tipo[f]=input("Tipo de mueble %d: "%(f+1)).upper()
print()
print("""E (economico), M (medio) y L(lujo):""")
print()
for f in range(3):
    modelo[f]=input("Modelo %d: "%(f+1)).upper()
print()
for f in range(3):
    for c in range(3):
        produccion_inicial[f][c]=int(input(f"Producción de tipo {tipo[f]} Modelo {modelo[c]}: "))
        produccion_mensual+=produccion_inicial[f][c]
        sf[f]+=produccion_inicial[f][c]


#Encabezados columnas
print("\n Matriz producción inicial del mes")
print("                  Modelo")
print("Tipo       ", end="   ")
for f in range(3):
    print("{0:5}".format(modelo[f]),end="  ")
print("Total")


for f in range(3):
    print("{0:9}".format(tipo[f]),end="")
    for c in range(3):
        print("  {0:5d}".format(produccion_inicial[f][c]),end="")
    print("  {0:5d}".format(sf[f]),end="")
    print()
print("\nSu produccion total mensual es de:",produccion_mensual,"Muebles")

periodo=int(input("\nPara el calculo de la produccion en un año indique el valor de 1 a 12 meses: "))
sf=[0]*3
for f in range(3):
    for c in range(3):
        produccion_final[f][c]=produccion_final[f][c]+periodo*produccion_inicial[f][c]
        produccion_periodo+=produccion_final[f][c]
        sf[f]+=produccion_final[f][c]

print(f"\nMatriz producción segun la planificación de su periodo de {periodo} meses")
print("                Modelo")
print("Tipo         ",end="  ")
for f in range(3):
    print("{0:5}".format(modelo[f]), end="  ")
print()

for f in range(3):
    print("{0:9}".format(tipo[f]),end="")
    for c in range(3):
        print("  {0:5d}".format(produccion_final[f][c]),end="")
    print()
print()
print(f"Su producción total en el periodo de: {periodo} meses es de: {produccion_periodo} muebles")

for f in range(3):
    print("Total producción de", tipo[f], "es de:",sf[f])

print("\nFin del programa")
print()
r=input("Pausa")
print()

#Matriz traspuesta
print("Ejemplo de matriz traspuesta\nMatriz inicial")

for f in range(3):
    for c in range(3):
        print("  {0:4d}".format(produccion_inicial[f][c]), end="")
    print()
print("Traspuesta")
for c in range(3):
    for f in range(3):
        print("  {0:4d}".format(produccion_inicial[f][c]),end="")
    print()
for f in range(3):
    for c in range(3):
        suma[f][c]=produccion_inicial[f][c] + produccion_inicial[c][f]

print("\n Suma de la matriz inicial y su traspuesta")
for f in range(3):
    for c in range(3):
        print("  {0:4d}".format(suma[f][c]), end="")
    print()
