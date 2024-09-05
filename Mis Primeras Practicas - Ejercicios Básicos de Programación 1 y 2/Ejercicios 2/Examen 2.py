"""
2)El  IVSS requiere clasificar a las personas que se jubilaran
  en el año 2017, existen tres tipos de jubilaciones: 
  por edad, por antigüedad joven y por antigüedad adulta.
  Las  cuales son:

a)Las personas adscritas a la jubilación por edad deben tener 60
  años o más y una antigüedad en su empleo de menos de 25 años.
b)Las personas adscritas a la jubilación por antigüedad joven
  deben tener menos de 60 años y una antigüedad en su empleo
  de 25 años o más.
c)Las personas adscritas a la jubilación por antigüedad adulta
  deben tener  60 años o más y una antigüedad en su empleo de
  25 años o más.
d)Las personas que tienen menos de 60 años y una antigüedad en
  su empleo menor de 25 años no tienen porque jubilarse.

NOTA: LA EDAD Y LA ANTIGÜEDAD DEBEN CALCULARSE

Imprimir: nombre, tipo de jubilación, empresa donde laboro, y en
caso de jubilarse sueldo a cobrar como jubilado, el que no se
jubila mantiene su sueldo.
"""

#Versión 1.0
"""
np=str(input("Deme su nombre:"))
e=int(input("Edad:"))
ep=int(input("Tiempo en su empleo:"))
el=str(input("Empresa donde laboro:"))

if(e>=60)and(ep<25):
    print("jubilación")
elif(e<60)and(ep<=25):
     print("jubilación joven")
elif(e>=60)and(ep>=25):
    print("jubilación adulta")
else:
    (e<60)or(ep<25)
    print("Nada de Jubilación")

print(np)
print("Laboro en:",el)
print("Cobrara una jubilación de 4000$")"""

#Versión 2.0

#Inicializamos Variables:
edad = time = 0
empresa = name = jubilacion = d =""
sueldo = sueldof = 0.0
v = False

#Datos de entrada:
name = input("Ingrese su nombre: ").capitalize()
edad = int(input("Ingrese su edad: "))
empresa = input("Empresa donde laboro: ").capitalize()
time = int(input("Antiguedad en su empleo: "))
sueldo = float(input("Sueldo: "))

#Proceso

if(edad>=60):
    if(time<25):
        jubilacion = "Jubilación por edad"
        v = True
    else:
        jubilacion = "Jubilación por antiguedad adulta"
        v = True
else:
    if(time>=25):
        jubilacion = "Jubilación por antiguedad joven"
        v = True
    else:
        jubilacion = "No tiene que jubilarse"

if(v==True):
    sueldof = float(input("Sueldo a cobrar como jubilado: "))
    c = sueldof
    d = "$"
else:
    c = "No tiene Sueldo como Jubilado"
    d = ""

#imprimir
print("\n-------------------------------------------------------------\n")        
print(f"Nombre:                     {name}")
print(f"Tipo de jubilación:         {jubilacion}")
print(f"Empresa donde laboro:       {empresa}")
print(f"Sueldo:                     {sueldo} $")
print(f"Sueldo como jubilado:       {c} {d}")

