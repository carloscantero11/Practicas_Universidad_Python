#Datos:
solvente=""
tv=va=af=am=vc=vb=vn=0
mac=ff=tvoto=acmor=0
pc=pvn=paf=0.0
resp="S"
per="S"
band=1
#proceso:

while(resp=="S"):
       print("Colegios:")
       print("ABOGADOS")
       print("INGENIEROS")
       print("ARQUITECTOS")
       print("MEDICOS")
       print("ADMINISTRACION")
       colegio=input("Nombre del colegio (Escribirlo tal como sale en las opciones): ").upper()

       while(per=="S"):
              solvente=input("Responda con s/n si esta solvente: ").lower()
              if(solvente=="s"):
                     print()
                     print("Usted puede votar")
                     print()
                     voto=input("Haga su voto (A,B,C): ").upper()
                     tv+=1
                     if(voto=="A"):
                            va+=1
                            sexo=input("Diga su sexo 'F/M': ").upper()
                            if(sexo=="F"):
                                   af+=1
                            else:
                                   am+=1
                     elif(voto=="B"):
                            vb+=1
                     elif(voto=="C"):
                            vc+=1
                     else:
                            vn+=1

              else:
                     print("Usted esta moroso")
                     if(colegio=="INGENIEROS"):
                            sexo=input("Diga su sexo 'F/M': ").upper()
                     
                            if(sexo=="M"):
                                   mac+=1
                            else:
                                   ff+=1
                     else:
                            acmor+=1
              per=input("Desea vota por otro candidato'S/N': ").upper()
       
       if(va>vb)and(va>vc):
           gg="A"
           tvoto=va
           pc=va*100/tv
           paf=af*100/va
       elif(vb>va)and(vb>vc):
           gg="B"
           tvoto=vb
           pc=vb*100/tv
       elif(vc>va)and(vc>vb):
           gg="C"
           tvoto=vc
           pc=vc*100/tv
       else:
           print("NO HAY GANADOR")
           band=0
       if(band==1):
              print
              print("El ganador fue el candidato",gg)
              print("Votos:",tvoto,"  Porcentaje:",pc,"%")
              
       pvn=vn*100/tv
       print("Profesionales morosos:",acmor)
       print("Mujeres que votaron por el cantidato A:",paf)
       print("Hombres morosos:",mac)
       print("Votos nulos:",pvn)
       print("Colegio de",colegio)
       print()
       resp=input("Otro colegio desea hacer elecciones S/N: ").upper()

              
