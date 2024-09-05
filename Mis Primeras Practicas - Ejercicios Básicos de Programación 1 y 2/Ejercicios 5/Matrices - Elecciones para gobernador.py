"""
Crear una aplicacion en Python que determine elganador de las
elecciones llevadas a cabo en un estado el cual tiene N candidatos
con Q municipios. Los nombres de los candidatos se almacenaran en
en una lista (vector) por filas y los vots obtenidos por cada
candidato en una lista de listas (matriz) toda la información sera
suministrada por teclado, por pantalla se debe mostrar los nombres de
los candidatos seguido los votos obtenidos por estos en cada
municipio, al final se debe mostrar quien gano las elecciones"""

#Inicializamos variables
candidatos=[]
votos=[[]]
filas = col = 0
valor = band = 0
nom = mnom = ""
total = mtotal = 0

#Determinamos la cantidad de filas y columnas
filas=int(input("Cantidad de candidatos: "))
col=int(input("Cantidad de municipios: "))
candidatos = [0]*filas
votos=[]
votos=[[0]*col for i in range(filas)]

#Entrada de datos
#Nombre de los candidatos
#Votos obtenidos por los candidaros en cada distrito

for f in range(filas):
    candidatos[f]=input("Nombre del candidato %d: "%(f+1))
    for c in range(col):
        votos[f][c]=int(input("Votos obtenidos por %d en el municipio %d: "%((f+1),(c+1))))
        
#Encabezados de columnas
print("\n           Municipios")
print("Candidato",end=" ")
for f in range(col):
    print("{0:4d}  ".format(f+1),end= "")
print()

#Mostra candidatos y votos obtenidos
for f in range(filas):
    print("{0:6}\t".format(candidatos[f]),end= "")
    total=0

    #Determinamos el ganador
    for c in range(col):
        total+=votos[f][c]
        print("  {0:4d}".format(votos[f][c]),end= "")
    if band==0:
        mnom=candidatos[f]
        mtotal=total
        band=1
    elif mtotal<total:
        mnom=candidatos[f]
        mtotal=total
    print()
print()
print()
print(f"""Gano la gobernación: {mnom}
Total de votos: {mtotal}""")
