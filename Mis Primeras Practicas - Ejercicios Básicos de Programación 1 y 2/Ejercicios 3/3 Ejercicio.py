#Un alumno quiere imprimir su nombre, el promedio de su "n"
#notas cuantas aprobo y cuantas reprobo, si paso o no la materia.

#Versión 1.0
"""
na=" "
ca=cr=snotas=n=0
pnota=0
na=str(input("Dame su nombre:"))
n=int(input("Cuantas notas son:"))
for x in range (1,n+1):
    nx=int(input("Cuanto saco en las evaluaciones:"))
    snota=nx
    if(nx>=10):
        ca+=1
    elif(nx<10):
        cr+=1
pnota=snota/n
print("el alumno",na,"tiene un promedio de",pnota)
print("aprobo",ca,"reprobo",cr)
"""

#Versión 2.0

#Inicializamos Variables:
name = pasar = ""
promedio = nota = snota = 0.0
n = reprobar = aprobar = 0

#Entrada de datos:
name = input("Nombre del alumno: ")
n = int(input("Nro. de notas del Alumno: "))
print()

for i in range(1,n+1):
    nota = float(input("Nota "+str(i)+": "))
    snota += nota

    if(nota>=9.5):
        aprobar += 1
    else:
        reprobar += 1

#Proceso:
promedio = snota/n

if(promedio>=9.5):
    pasar = "APROBO la materia"
else:
    pasar = "REPROBO la materia" 
    

#Imprimir Resultados:
print("\n========================Resultados========================")
print("\nNombre del alumno:",name)
print("Promedio de las",n,"notas: {0:3.2f}".format(promedio))
print("Cantidad de notas aprobadas:",aprobar)
print("Cantidad de notas reprobadas:",reprobar)
print(f"\nEl alumno {name} {pasar} con un promedio de {promedio}")


    
