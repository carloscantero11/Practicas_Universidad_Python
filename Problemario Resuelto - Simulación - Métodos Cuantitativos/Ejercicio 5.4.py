#  Ejercicio 5.4
"""Se desea saber el resultado economico de una campaña de
suscripción puerta a puerta; para ellose realiza un estudio de
simulación en base a información muestral obtenida de campañas
anteriores. El nº máximo de suscripciones que puede hacer una
persona que es visitada por el vendedor es de 4, pero la
probabilidad varía si es hombre o mujer. La distribución de
probabilidad del nº de suscripciones según el sexo del comprador
es el siguiente:

Mujeres:                            
Nº de artículos   1    2    3   4   
 Probabilidad    0.6  0.3  0.1  0

Hombres:
Nº de artículos   1    2    3    4
 Probabilidad    0.1  0.4  0.3  0.2

Cuando el vendedor/a visita a los clientes establecidos, en un
70% de los casos no hay nadie o no son recibidos. Cuando son
recibidos, un 80% de las veces abre un hombre y un 20% una mujer.
Cuando abre un hombre un 25% de las veces se consigue la venta,
pero este porcentaje es sólo el 15% si abre una mujer. El
beneficio por suscripción vendida es de 3.000 pts. Determinar el
beneficio total de la campaña simulando 15 visitas.

Números Aleatorios: 2-7-45-4-9-2-9-47-5-5-3-4-8-9-4-8-9-0-4-8-9-
7-5-8-3-4-9-8-7-4-5-8-5-3-8-2-2-47-8-9-4-7-8-9-8-8-1-3-26-5-9-8-
8-9-5-6-7-7-8-5-6-3-1-0-10-2-3-4-8-5-7-2-3-36-4-5-4-7-5-0-9-28-
2-7-31-0-9-29-3

"""

#Elaborado por: Carlos Cantero

#Modulos o Subprogramas
#Subprograma que realiza una equivalencia de 0 a 100 a otro de 0 a 50
def porcentaje(na):
    p = int
    p = na * 0.5
    return p

#Subprograma que determina si el vendedor fue recibido o no
def visitas(na):
    if(na < porcentaje(30)):   #El vendedor es recibido
        print(f"Número aleatorio: {na}\nEl vendedor es recibido.\n")
        return 1   
    else:      #El vendedor no fue recibido
        print(f"Número aleatorio: {na}\nEl vendedor no es recibido.\n")
        return 0

#Subprograma que determina el sexo del cliente
def sexo_cliente(na):
    sexo = int
    if(na < porcentaje(80)):        #Hombre
        print(f"Número aleatorio: {na}\nFue recibido por un hombre.\n")
        return 0
    else:                           #Mujer
        print(f"Número aleatorio: {na}\nFue recibido por una mujer.\n")
        return 1

#Subprograma que determina si se concreto la venta o no
def venta(na,sexo):
    if(sexo==0):    #Un hombre abrio la puerta
        if(na < porcentaje(25)):   #Se consiguio la venta
            print(f"Número aleatorio: {na}\nSe consiguio la venta.\n")
            return 0

        else:                      #No se consiguio la venta  
            print(f"Número aleatorio: {na}\nNo se consiguio la venta.\n")
            return 1
            
    else:           #Una mujer abrio la puerta
        if(na < porcentaje(15)):   #Se consiguio la venta
            print(f"Número aleatorio: {na}\nSe consiguio la venta.\n")
            return 0
        else:                      #No se consiguio la venta
            return 1

#Subprograma que determina cuantas subscriciones fueron vendidas
def suscripciones(na,sexo):
    nart = int
    if(sexo==0):      #Suscripción hombre
        if(na<porcentaje(10)):
            nart = 1
        elif(na<porcentaje(50)):
            nart = 2
        elif(na<porcentaje(80)):
            nart = 3
        else:
            nart = 4

    else:             #Suscripción mujer
        if(na<porcentaje(60)):
            nart = 1
        elif(na<porcentaje(90)):
            nart = 2
        elif(na<porcentaje(100)):
            nart = 3
        else:
            nart = 4
            
    print(f"Número aleatorio: {na}")
    print(f"Suscripciones vendidas: {nart}")
    return nart

#Subprograma que determina la ganancia o beneficio del vendedor
def ganancia(nart):
    r = int
    r = nart * 3000
    print(f"\nGanancia de la venta: {r} pts\n")
    return r

#Subprograma que recorre la lista
def recorrerLista(indice,lista):
    indice += 1
    
    if(indice >= len(lista)):
        indice = 0
    return indice

#Subprograma principal
def principal(lista):
    total_ganancia = 0
    sim = 1
    i = 0
    
    for x in range(15):
        #Inicializamos variables
        visita = 0
        sex = 0
        ventas = 0
        sub = 0
        beneficio = 0
        
        print(f"----------------------Simulación {sim}-----------------------\n")
        sim += 1
        
        visita = visitas(lista[i])
        i = recorrerLista(i,lista)

        if(visita == 1):      #Vendedor Recibido
            sex = sexo_cliente(lista[i])
            i = recorrerLista(i,lista)

            if(sex==0):     #Fue un hombre
                ventas = venta(lista[i],0)
                i = recorrerLista(i,lista)

                if(ventas == 0):     #subscripción hombre
                    sub = suscripciones(lista[i],0)
                    i = recorrerLista(i,lista)
                    beneficio = ganancia(sub)
                else:
                    continue
                
            else:              #Fue una mujer
                ventas = venta(lista[i],1)
                i = recorrerLista(i,lista)
                
                if(ventas == 0):     #subscripción mujer
                    sub = suscripciones(lista[i],1)
                    i = recorrerLista(i,lista)
                    beneficio = ganancia(sub)
                else:
                    continue
        else:
            continue
        total_ganancia += beneficio   #Ganancias totales

    print("--------------------------------------------------------")
    print(f"\nGanancia total: {total_ganancia} pts")

#Variable de entrada
n = []

#Delaración de Variables
#Variables de Salida

#Inicialización de variable
n = [2, 7, 45, 4, 9, 2, 9, 47, 5, 5, 3, 4, 8, 9, 4, 8, 9, 0, 4, 8, 9, 7, 5, 8, 3, 4, 9, 8, 7, 4, 5, 8, 5, 3, 8, 2, 2,47, 8, 9, 4, 7, 8, 9, 8, 8, 1, 3, 26, 5, 9, 8, 8, 9, 5, 6, 7, 7, 8, 5, 6, 3, 1, 0, 10, 2, 3, 4, 8, 5, 7, 2, 3, 36, 4, 5, 4, 7, 5, 0, 9, 28, 2, 7, 31, 0, 9, 29, 3]

#Inicio del programa 
principal(n)









