#  Ejercicio 5.5
"""
Una empresa quiere introducirse en la venta por teléfono, pero desea determinar cuáles son los
ingresos medios que supone esta nueva estrategia de ventas por teléfono con el fin de determinar
los futuros beneficios. Se sabe de estudios de otras empresas dedicadas a lo mismo, que:

* De las llamadas realizadas, el 55% de las llamadas contestan y aceptan, el 25% contestan y
no aceptan y el resto no contestan (no hay nadie en casa, contestador, teléfono erróneo,...).
* Las ventas difieren de si es un hombre o una mujer quien contesta.
* La probabilidad de que sea una mujer es del 55%.
* Las probabilidades de ventas están definidas de la siguiente manera:

Mujeres:
Nº de artículos 0 1 2 3 4 5
Probabilidad 0.04 0.16 0.30 0.25 0.20 0.05

Hombres:
Nº de artículos 0 1 2 3 4 5
Probabilidad 0.15 0.10 0.15 0.30 0.20 0.10

El precio medio del artículo es de 3000 pts, simule un día laboral donde pueden realizarse unas 20
llamadas.

Números aleatorios:
39-27-79-17-98-62-28-75-34-43-84-14-32-70-90-26-74-17-59-12-23-63-80-65-44-89-79-
82-01-18-86-55-59-26-96-31-74-54-90-95-61-62

"""
#Elaborado por: Carlos Cantero

#Modulos o Subprogramas

#Subprograma que determina si el cliente contesto la llamada o no
def llamadas(na):
    if(na < 55):    #Contestan y aceptan
        print(f"\nNúmero aleatorio: {na}\nContestan la llamada y aceptan.\n")
        return 1
    elif(na <80):   #Contestan y no aceptan
        print(f"\nNúmero aleatorio: {na}\nContestan la llamada y no aceptan.\n")
        return 2
    else:           #No constestan la llamada
        print(f"\nNúmero aleatorio: {na}\nNo contestan la llamada.\n")
        return 3

#Subprograma que determina el sexo del cliente
def sexo(na):
    if(na < 45):  #Hombre
        print(f"Número aleatorio: {na}\nLa llamada fue contestada por un hombre.\n")
        return 1
    else:         #Mujer
        print(f"Número aleatorio: {na}\nLa llamada fue contestada por una mujer.\n")
        return 2

#Subprograma que determina la cantidad de articulos que vendieron
def ventas(na,sexo):
    nart = int
    if(sexo==1):    #Hombres
        if(na < 15):    #0 Articulo
            nart = 0
        elif(na < 25):  #1 Articulo
            nart = 1
        elif(na < 40):  #2 Articulo
            nart = 2
        elif(na < 70):  #3 Articulo
            nart = 3
        elif(na < 90):  #4 Articulo
            nart = 4
        else:           #5 Articulo
            nart = 5

    else:    #Mujeres
        if(na < 4):     #0 Articulo
            nart = 0
        elif(na < 20):  #1 Articulo
            nart = 1
        elif(na < 50):  #2 Articulo
            nart = 2
        elif(na < 75):  #3 Articulo
            nart = 3
        elif(na < 95):  #4 Articulo
            nart = 4
        else:           #5 Articulo
            nart = 5
            
    print(f"Número aleatorio: {na}")
    print(f"Venta de articulos: {nart}")
    return nart
 
#Subprograma que determina las ganancias de la venta en la llamada
def ganancia(nart):
    r = int
    r = 3000 * nart
    print(f"\nGanancias de la venta: {r} pts\n")
    return r

#Subprograma que determina el ingreso medio de las ventas
def ingreso_medio(gan,num):
    pm = float
    pm = gan / num
    return pm

#Subprograma para recorrer las lista
def recorrido(indice,lista):
    indice+=1
    if(indice >= len(lista)):
        indice = 0
    return indice

#Subprograma Principal
def principal(lista):
    #Inicializamos variables
    i = 0
    num = 0
    total = 0
    p = 0.0

    for x in range(20):
        ll = 0   #llamadas()
        sex = 0  #sexo()
        v = 0    #ventas()
        beneficio = 0 #ganancia()
        num+=1
        
        print(f"------------------------Llamada {num}------------------------")
        
        ll = llamadas(lista[i])
        i = recorrido(i,lista)

        if(ll == 1):   #Contestan y aceptan
            sx = sexo(lista[i])
            i = recorrido(i,lista)

            if(sx == 1):   #Hombre
                v = ventas(lista[i],sexo)
                i = recorrido(i,lista)
                beneficio = ganancia(v)
            else:  #Mujer
                v = ventas(lista[i],sexo)
                i = recorrido(i,lista)
                beneficio = ganancia(v)

        elif(ll == 2): #Contestan y no aceptan
            continue
        else:    #No contestaron
            continue
        total += beneficio  #El total de las ganancias por llamada

    p = ingreso_medio(total,num)

    print(f"------------------------------------------------------\n\nIngresos medios: {p} pts")


#Inicio del programa
#Declaración de variables
#Variables de entrada
n = []

#Inicialización de variables
n = [39,27,79,17,98,62,28,75,34,43,84,14,32,70,90,26,74,17,59,12,23,63,80,65,44,89,79,82,1,18,86,55,59,26,96,31,74,54,90,95,61,62]

#Variables de salida
#Variables de proceso

#Procesamiento de datos
principal(n)















