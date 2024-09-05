import time
#Registrar las 4 premisas:

p1=input("Premisa 1: ")
p2=input("Premisa 2: ")
p3=input("Premisa 3: ")
p4=input("Premisa 4: ")

D1=D2=D3=""
#Operadores lógicos:
time.sleep(1)
print("")
print("Escoja con un número los operadores lógicos que desea utilizar:")
print("")
time.sleep(2)
C1=int(input("(1)CONJUNCIÓN{y}   (2)DISYUNCION{o}   (3)NEGACION{no}   (4)CONDICIONAL{Si entonces} : "))
if(C1==1):
    C1='y'
elif(C1==2):
    C1='o'
elif(C1==3):
    C1='y no se da el caso que'
elif(C1==4):
    D1='Si'
    C1='entonces'
else:
    print("")
print("")
time.sleep(0.5)
C2=int(input("(1)CONJUNCIÓN{y}   (2)DISYUNCION{o}   (3)NEGACION{no} : "))
if(C2==1):
    C2='y'
elif(C2==2):
    C2='o'
elif(C2==3):
    C2='y no se da el caso que'
else:
    print("")
time.sleep(0.5)

print("")
C3=int(input("(1)CONJUNCIÓN{y}   (2)DISYUNCION{o}   (3)NEGACION{no} : "))
if(C3==1):
    C3='y'
elif(C3==2):
    C3='o'
elif(C3==3):
    C3='y no se da el caso que'
else:
    print("")
time.sleep(0.5)
#imprimir:

time.sleep(1)
print("")
print("=======================================SOFTWARE QUE PERMITA REGISTRAR 4 PREMISAS=======================================")
time.sleep(1)
print("")
print(D1,p1,C1,p2,C2,p3,C3,p4)

