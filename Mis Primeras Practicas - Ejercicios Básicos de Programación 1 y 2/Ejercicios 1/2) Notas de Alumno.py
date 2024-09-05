#Un profesor desea imprimir el nombre de un alumno y su
#calificación final segunsegun lo siguiente:

#1)La nota del primer corte equivale al 55% del promedio
#  de 2 notas parciales.
#2)La nota del segundo corte equivale al 15% de un trabajo.
#3)La nota del tercer corte equivale al 30% de un examen final.

#Versión 1.0
"""#Inicializar variables:
na=""
nota1=nota2=nt=nef=cf=c1=c2=c3=0.0
#Entrada de datos
na=str(input("Deme su nombre:"))
nota1=float(input("Deme nota 1:"))
nota2=float(input("Deme nota 2:"))
nt=float(input("Indique nota trabajo:"))
nef=float(input("Introduzca nota de examen final:"))
#Proceso:
c1=(nota1+nota2)/2*0.55
c2=nt*0.15
c3=nef*0.30
cf=c1+c2+c3
print("El alumno",na)
print("Tiene calificacion de:"+str(cf))"""

#Versión 2.0

#Declaramos Variables
name = apellido = ""
nota1 = nota2 = nota3 = notaf = total= 0.0
corte1 = corte2 = corte3 = 0.0

#Entrada de datos:
name = input("Nombre del Alumno: ").capitalize()
apellido = input("Apellido del Alumno: ").capitalize()

print("\nNotas del 1er corte:")
nota1 = float(input("Nota del 1er parcial: "))
nota2 = float(input("Nota del 2do parcial: "))

print("\nNotas del 2do corte:")
nota3 = float(input("Nota del trabajo: "))

print("\nNotas del 3er corte:")
notaf = float(input("Nota del examen final: "))

#Proceso:

corte1 = ((nota1 + nota2)*0.55)/2
corte2 = nota3 * 0.15
corte3 = notaf * 0.30
total = corte1 + corte2 + corte3 

#Imprimir:
print("\n-----------------------------------------------------------")
print("\nNombre del alumno:",name,apellido)
print("\nCalificción final:",total)

