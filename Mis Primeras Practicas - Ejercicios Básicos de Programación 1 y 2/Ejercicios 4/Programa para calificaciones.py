import time
band=0
pr=0
atpto=tpto=0.0
na=input("Deme su nombre: ").upper()
print("¿Cuantas materias son?")
v=int(input())
np=0
for i in range(1,v+1):
    sn,ca,cr=0,0,0
    m=input("Nombre de la materia: ").upper()
    print("¿Cuantas evaluaciones son?")
    d=int(input())
    print()
    for j in range(1,d+1):
        porc=int(input("Porcentaje de la nota "+str(j)+": "))
        n=int(input("Deme nota "+str(j)+": "))
        pr+=porc
        tpto=(n*porc)/100
        atpto+=tpto
        time.sleep(1)
        print("Porcentaje acumulado:",pr)
        print()
        time.sleep(1)
        if(n>=0)and(n<=20):
            sn+=n
            if(n>=10):
                ca+=1
            else:
                cr+=1
            if(band==0):
                mayor=n
                band=1
            if(n>mayor):
                mayor=n
            else:
                np+=1
        else:
            break

    time.sleep(2)
    print("*****************************Resultados****************************")
    time.sleep(2)
    print()
    print("Alumn@:",na)
    time.sleep(1)
    print("Materia:",m)
    time.sleep(1)
    print("Promedio:",atpto)
    time.sleep(1)
    print("Aprobo:",ca,"Materia(s)")
    time.sleep(1)
    print("Reprobo:",cr,"Materia(s)")
    time.sleep(1)
    print("Mayor nota:",mayor)
    time.sleep(4)
    print()
    print()
    print()
