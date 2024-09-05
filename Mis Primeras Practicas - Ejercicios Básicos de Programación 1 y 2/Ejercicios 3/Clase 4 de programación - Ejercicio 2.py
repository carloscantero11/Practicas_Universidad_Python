#promedio de 5 edades mayores=25 y menores=40
edad=se25y40=ce25y40=0
pe25y40=0.0
for i in range(1,6):
    edad=int(input("deme su edad:"))
    if(edad>=25)and(edad<=40):
        se25y40+=edad
        ce25y40+=1
if(ce25y40):
    pe25y40=se25y40/ce25y40
    print("el promedio entre 25 y 40 es=",pe25y40)
else:
    print("no hay edades") 
