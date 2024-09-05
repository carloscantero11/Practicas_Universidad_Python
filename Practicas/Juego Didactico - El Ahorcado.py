
import time
n=input("¿Cómo te llamas?: ")
print("")
time.sleep(0.7)
print("Hola,",n+". Es hora de jugar!!!!!")
print("")
print("")
time.sleep(2.5)
print("==============================El Ahorcado===============================")
print("")
print("")
time.sleep(2)
print("Escriba con un número la opción que usted desea.")
time.sleep(2.5)
xd=int(input("(1)Comenzar el juego.   (2)Reglas del juego. : "))
print("")
print("")

time.sleep(1.3)
print("El juego comenzara en...")
print("")
time.sleep(1.5)
print("3")
print("")
time.sleep(1.5)
print("2")
print("")
time.sleep(1.5)
print("1")
print("")
time.sleep(1.5)
print("")

#Parte 1:

if(xd==1):   
    print("Comienza a adivinar")
    print("")
    print("")
    print("Primera partida")
    print("")
    time.sleep(1)
    palabra="galaxia"
    tupalabra=" "
    vidas=6
    while vidas > 0:
        fallas=0
        for letra in palabra:
            if letra in tupalabra:
                print(letra,end="")
            else:
                print("-",end="")
                fallas+=1
        if fallas==0:
            print("")
            print("")
            k=10
            print("Felicidades, has ganado,",k," puntos!!")
            break

        tuletra=input(" ¿Cuál letra eliges?: ")
        tupalabra+=tuletra

        if tuletra not in palabra:
            vidas-=1
            print("Te equivocaste :c")
            print("Te quedan ",+vidas," vidas")
        if vidas== 0:
            print("Has perdido!! :c")
    else:
        print("")
        k=0
        print("No acumulaste puntos. :C")


#Segunda partida:        

    time.sleep(1)
    print("")
    print("")
    print("Siguiente partida:")
    print("")
    print("")

    time.sleep(1)
    palabra="musica"
    tupalabra=" "
    vidas=6
    while vidas > 0:
        fallas=0
        for letra in palabra:
            if letra in tupalabra:
                print(letra,end="")
            else:
                print("-",end="")
                fallas+=1
        if fallas==0:
            print("")
            print("")
            s=10
            ss=k+s
            print("Felicidades, has ganado 10 puntos!!")
            print("")
            time.sleep(1)
            print("Sumas un total de,",ss,"puntos")
            break

        tuletra=input(" ¿Cuál letra eliges?: ")
        tupalabra+=tuletra

        if tuletra not in palabra:
            vidas-=1
            print("Te equivocaste :c")
            print("Te quedan ",+vidas," vidas")
        if vidas== 0:
            print("Has perdido!! :c")
    else:
        print("")
        s=0
        ss=s+k
        print("Sumas un total de",ss,"puntos")
        
#Tercera partida:

    time.sleep(1)
    print("")
    print("")
    print("Siguiente partida:")
    print("")
    print("")

    time.sleep(1)
    palabra="guitarra"
    tupalabra=" "
    vidas=6
    while vidas > 0:
        fallas=0
        for letra in palabra:
            if letra in tupalabra:
                print(letra,end="")
            else:
                print("-",end="")
                fallas+=1
        if fallas==0:
            print("")
            print("")
            
            print("Felicidades, has ganado 10 puntos!!")
            print("")
            time.sleep(1)
            c=10
            cc=k+s+c
            print("Sumas un total de,",cc,"puntos")
            break
        
        tuletra=input(" ¿Cuál letra eliges?: ")
        tupalabra+=tuletra

        if tuletra not in palabra:
            vidas-=1
            print("Te equivocaste :c")
            print("Te quedan ",+vidas," vidas")
        if vidas== 0:
            print("Has perdido!! :c")
    else:
        print("")
        c=0
        cc=k+s+c
        print("Sumas un total de",cc,"puntos")

#Cuarta partida:

    time.sleep(1)
    print("")
    print("")
    print("Siguiente partida:")
    print("")
    print("")

    time.sleep(1)
    palabra="estrella"
    tupalabra=" "
    vidas=6
    while vidas > 0:
        fallas=0
        for letra in palabra:
            if letra in tupalabra:
                print(letra,end="")
            else:
                print("-",end="")
                fallas+=1
        if fallas==0:
            print("")
            print("")
            m=10
            mm=c+k+s+m
            print("Felicidades, has ganado 10 puntos!!")
            print("")
            time.sleep(1)
            print("Sumas un total de,",mm,"puntos")
            break

        tuletra=input(" ¿Cuál letra eliges?: ")
        tupalabra+=tuletra

        if tuletra not in palabra:
            vidas-=1
            print("Te equivocaste :c")
            print("Te quedan ",+vidas," vidas")
        if vidas== 0:
            print("Has perdido!! :c")
    else:
        print("")
        m=0
        mm=c+k+s+m
        print("Sumas un total de",mm,"puntos")

#Quinta partida:

    time.sleep(1)
    print("")
    print("")
    print("Ultima partida:")
    print("")
    print("")

    time.sleep(1)
    palabra="luna"
    tupalabra=" "
    vidas=6
    while vidas > 0:
        fallas=0
        for letra in palabra:
            if letra in tupalabra:
                print(letra,end="")
            else:
                print("-",end="")
                fallas+=1
        if fallas==0:
            print("")
            print("")
            y=10
            x=m+c+k+s+y
            print("Felicidades, has ganado 10 puntos!!")
            print("")
            time.sleep(1)
            if(x==50):
                time.sleep(1.2)
                print("FELICIDADES!!!! HAS GANADO EL JUEGO CON UN TOTAL DE 50 PUNTOS")
            if(x<50):
                time.sleep(1.2)
                print("FELICIDADES!!!! Terminaste el juego con un total de,",x,"puntos")
            break

        tuletra=input(" ¿Cuál letra eliges?: ")
        tupalabra+=tuletra

        if tuletra not in palabra:
            vidas-=1
            print("Te equivocaste :c")
            print("Te quedan ",+vidas," vidas")
        if vidas== 0:
            print("Has perdido!! :c")
    else:
        print("")
        y=0
        x=m+c+k+s+y
        time.sleep(1.2)
        print("FELICIDADES!!!! Terminaste el juego con un total de,",x,"puntos")


#Parte 2:
        
if(xd==2):
    time.sleep(1)
    print("============================Reglas del juego============================")
    print("")
    time.sleep(1)
    print("- El Juego: ")
    print("")
    time.sleep(1)
    print("    El objetivo de este juego es descubrir una palabra adivinando las letras")
    time.sleep(1)
    print("que la componen. A cada ronda, el jugador o jugadores escogerán simultáneamente")
    time.sleep(1)
    print("una letra que crea que pueda formar parte de la palabra. Si la palabra contiene")
    time.sleep(1)
    print("la letra escogida, se mostrará en qué posición está la palabra. En el caso de que la ")
    time.sleep(1)
    print("letra no exista en la palabra, perderá una vida. El jugador solo tendra 6 vidas.")
    time.sleep(1)
    print("Si este pierde todas sus vidas, el jugador perderá  la partida.")
    print("")
    time.sleep(15)
    print("- La Puntuación:")
    time.sleep(1)
    print("")
    print("    El juego del Ahorcado consiste de 5 partidas, cada una con una palabra para")
    time.sleep(1)
    print("descubrir. Cada partida ganada, valdrá 10 puntos.")
    print("")
    time.sleep(7)
    print("- Objetivo:")
    time.sleep(1)
    print("")
    print("    Vence el juego, quien haya acumulado el mayor número de puntos en las 5 partidas.")
    print("")
    print("")
    time.sleep(6)
    
    xdd=str(input("Escriba SI para iniciar: "))
    
    print("")
    print("")
    time.sleep(1.3)
    print("El juego comenzara en...")
    print("")
    time.sleep(1.5)
    print("3")
    print("")
    time.sleep(1.5)
    print("2")
    print("")
    time.sleep(1.5)
    print("1")
    print("")
    time.sleep(1.5)
    print("")
    
#Primera partida:
      
    print("Comienza a adivinar")
    print("")
    print("")
    print("Primera partida")
    print("")
    time.sleep(1)
    palabra="galaxia"
    tupalabra=" "
    vidas=6
    while vidas > 0:
        fallas=0
        for letra in palabra:
            if letra in tupalabra:
                print(letra,end="")
            else:
                print("-",end="")
                fallas+=1
        if fallas==0:
            print("")
            print("")
            k=10
            print("Felicidades, has ganado,",k," puntos!!")
            break

        tuletra=input(" ¿Cuál letra eliges?: ")
        tupalabra+=tuletra

        if tuletra not in palabra:
            vidas-=1
            print("Te equivocaste :c")
            print("Te quedan ",+vidas," vidas")
        if vidas== 0:
            print("Has perdido!! :c")
    else:
        print("")
        k=0
        print("No acumulaste puntos. :C")


#Segunda partida:        

    time.sleep(1)
    print("")
    print("")
    print("Siguiente partida:")
    print("")
    print("")

    time.sleep(1)
    palabra="musica"
    tupalabra=" "
    vidas=6
    while vidas > 0:
        fallas=0
        for letra in palabra:
            if letra in tupalabra:
                print(letra,end="")
            else:
                print("-",end="")
                fallas+=1
        if fallas==0:
            print("")
            print("")
            s=10
            ss=k+s
            print("Felicidades, has ganado 10 puntos!!")
            print("")
            time.sleep(1)
            print("Sumas un total de,",ss,"puntos")
            break

        tuletra=input(" ¿Cuál letra eliges?: ")
        tupalabra+=tuletra

        if tuletra not in palabra:
            vidas-=1
            print("Te equivocaste :c")
            print("Te quedan ",+vidas," vidas")
        if vidas== 0:
            print("Has perdido!! :c")
    else:
        print("")
        s=0
        ss=s+k
        print("Sumas un total de",ss,"puntos")
        
#Tercera partida:

    time.sleep(1)
    print("")
    print("")
    print("Siguiente partida:")
    print("")
    print("")

    time.sleep(1)
    palabra="guitarra"
    tupalabra=" "
    vidas=6
    while vidas > 0:
        fallas=0
        for letra in palabra:
            if letra in tupalabra:
                print(letra,end="")
            else:
                print("-",end="")
                fallas+=1
        if fallas==0:
            print("")
            print("")
            
            print("Felicidades, has ganado 10 puntos!!")
            print("")
            time.sleep(1)
            c=10
            cc=k+s+c
            print("Sumas un total de,",cc,"puntos")
            break
        
        tuletra=input(" ¿Cuál letra eliges?: ")
        tupalabra+=tuletra

        if tuletra not in palabra:
            vidas-=1
            print("Te equivocaste :c")
            print("Te quedan ",+vidas," vidas")
        if vidas== 0:
            print("Has perdido!! :c")
    else:
        print("")
        c=0
        cc=k+s+c
        print("Sumas un total de",cc,"puntos")

#Cuarta partida:

    time.sleep(1)
    print("") 
    print("")
    print("Siguiente partida:")
    print("")
    print("")

    time.sleep(1)
    palabra="estrella"
    tupalabra=" "
    vidas=6
    while vidas > 0:
        fallas=0
        for letra in palabra:
            if letra in tupalabra:
                print(letra,end="")
            else:
                print("-",end="")
                fallas+=1
        if fallas==0:
            print("")
            print("")
            m=10
            mm=c+k+s+m
            print("Felicidades, has ganado 10 puntos!!")
            print("")
            time.sleep(1)
            print("Sumas un total de,",mm,"puntos")
            break

        tuletra=input(" ¿Cuál letra eliges?: ")
        tupalabra+=tuletra

        if tuletra not in palabra:
            vidas-=1
            print("Te equivocaste :c")
            print("Te quedan ",+vidas," vidas")
        if vidas== 0:
            print("Has perdido!! :c")
    else:
        print("")
        m=0
        mm=c+k+s+m
        print("Sumas un total de",mm,"puntos")

#Quinta partida:

    time.sleep(1)
    print("")
    print("")
    print("Ultima partida:")
    print("")
    print("")

    time.sleep(1)
    palabra="luna"
    tupalabra=" "
    vidas=6
    while vidas > 0:
        fallas=0
        for letra in palabra:
            if letra in tupalabra:
                print(letra,end="")
            else:
                print("-",end="")
                fallas+=1
        if fallas==0:
            print("")
            print("")
            y=10
            x=m+c+k+s+y
            print("Felicidades, has ganado 10 puntos!!")
            print("")
            time.sleep(1)
            if(x==50):
                time.sleep(1.2)
                print("FELICIDADES!!!! HAS GANADO EL JUEGO CON UN TOTAL DE 50 PUNTOS")
            if(x<50):
                time.sleep(1.2)
                print("FELICIDADES!!!! Terminaste el juego con un total de,",x,"puntos")
            break

        tuletra=input(" ¿Cuál letra eliges?: ")
        tupalabra+=tuletra

        if tuletra not in palabra:
            vidas-=1
            print("Te equivocaste :c")
            print("Te quedan ",+vidas," vidas")
        if vidas== 0:
            print("Has perdido!! :c")
    else:
        print("")
        y=0
        x=m+c+k+s+y
        time.sleep(1.2)
        print("FELICIDADES!!!! Terminaste el juego con un total de,",x,"puntos")
