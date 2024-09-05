print("""En la sección se va a elegir un delegado del curso para lo cual
participan 3 alumnos (María, Pedro, Andrea). Determine quien gano
y con cuantos voto, porcentaje de votos nulos (los votos nulos son
cualquier persona distina a los competidores)""")
print()
#Variables:
vm=vp=va=vn=tvoto=tv=0
pvn=0.0
band=1
resp="S"
#Proceso
while(resp=="S"):
    print("Candidatos:")
    print("Maria")
    print("Pedro")
    print("Andrea")
    voto=input("Haga su voto: ").upper()
    tv+=1
    if(voto=="MARIA"):
        vm+=1
    elif(voto=="PEDRO"):
        vp+=1
    elif(voto=="ANDREA"):
        va+=1
    else:
        vn+=1
    resp=input("Otro alumno va a votar 'S/N': ").upper()
    
if(vm>vp)and(vm>va):
    gg="MARIA"
    tvoto=vm
elif(vp>vm)and(vp>va):
    gg="PEDRO"
    tvoto=vp
elif(va>vm)and(va>vp):
    gg="ANDREA"
    tvoto=va
else:
    print("NO HAY GANADOR")
    band=0
if(band==1):
    print("El delegado es:",gg)
    print("Votos:",tvoto)
pvn=vn*100/tv
print("Porcentaje de votos nulos:",pvn)
