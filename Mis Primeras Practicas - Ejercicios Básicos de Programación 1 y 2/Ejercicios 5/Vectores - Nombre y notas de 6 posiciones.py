#Variables:
notas=[0]*6
nombre=[0]*6
snota=ca=cr=mayor=me=pm=pme=0
pn=0.0
nomma=" "
#Proceso:
print("************Cargar Vectores************")
for i in range(6):
    nombre[i]=input(f"Nombre[{i}]: ")
mayor = notas[0]
for i in range(6):
    notas[i]=int(input(f"Notas[{i}]: "))
    snota+=notas[i]
    if(notas[i]>=10):
        ca+=1
    else:
        cr+=1
    if(i==0):
        me=notas[i]
        pme=i
    if(notas[i]<me):
        me=notas[i]
        pme=i
    if(notas[i]>mayor):
        mayor=notas[i]
        nomma=nombre[i]
        pm=i
print("Vector nombre:")
for i in range(6):
    print(nombre[i],end=" | ")
print()
print("Vector notas")
for i in range(6):
    print(notas[i],end=" | ")
print()
pn=snota/6
print(f"""promedio del curso: {pn} ptos
Aprobados: {ca}          Reprobados: {cr}
Mayor nota: {mayor}     Posición: {pm}     Alumna:{nomma}
Menor nota: {me}        Posición: {pme}""")
