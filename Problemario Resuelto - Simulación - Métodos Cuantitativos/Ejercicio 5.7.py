#  Ejercicio 5.7
"""
Una empresa desea introducirse en el comercio electrónico (viá internet). Para ello quiere conocer
el número de artículos que vende en un día cualquiera por esta vía de comercialización. Los datos
de los que se dispone son que el 65% de la población tiene acceso a internet. De ese 65%, el
55% son hombres y el 45% son mujeres y el nº de artículos que compran a través del comercio
electrónico tiene la siguiente distribución

Hombres
nº Articulos     0      1      2    3 o más
Prob.           0.45   0.35   0.15   0.05

Mujeres
nº Articulos     0      1      2    3 o más
Prob.           0.25   0.55   0.15   0.05

Realice 30 simulaciones de para estimar la venta en un día cualquiera

Nº aleatorios: 64-48-80-14-28-40-63-40-71-57-72-38-65-74-59-29-75-54-91-83-89-70-10-
91-80-77-11-95-10-23-18-74-91-10-26-31-46-92-11-25-52-18-64-80-18-70-49-11-01-63-
21-08-14-42-84-31-17-80-32-72-27-38-75-24-55-55-03-95-63-52-42-31-39-10
"""

#Elaborado por: Carlos Cantero


#Modulos o subprogramas
#Subprograma que recorre la lista permitiendo su reinicio
def recorrerlista(indice,lista):
    indice += 1
    if(indice >= len(lista)):
        indice = 0
    return indice

#Subprograma que determina si el cliente tiene internet o no
def internet(na):
    if(na < 65):   #El cliente tiene internet
        print(f"\nNúmero aleatorio: {na}\nEl cliente tiene internet.\n")
        return 0
    else:        #El cliente no tiene internet
        print(f"\nNúmero aleatorio: {na}\nEl cliente no tiene internet.\n")
        return 1

#Subprograma que determina el sexo del cliente
def sexo_cliente(na):
    if(na < 55):    #Hombre
        print(f"Número aleatorio: {na}\nEl cliente es un hombre.\n")
        return 0
    else:           #Mujer
        print(f"Número aleatorio: {na}\nEl cliente es una mujer.\n")
        return 1

#Subprograma que determina las cantidad de articulos que se vendieron
def ventas(na,sexo):
    nart = int   #Numero de articulos
    
    if(sexo == 0):   #Hombre
        if(na < 45):
            nart = 0
        elif(na < 80):
            nart = 1
        elif(na < 95):
            nart = 2
        else:
            nart = 3

    else:   #Mujer
        if(na < 25):
            nart = 0
        elif(na < 80):
            nart = 1
        elif(na < 95):
            nart = 2
        else:
            nart = 3

    print(f"Número aleatorio: {na}\nNúmero de articulos vendidos: {nart}\n")
    return nart
    
    
#Subprograma principal
def principal(lista):
    num = 0  
    i = 0
    dventa = 0

    for x in range(30):
        num+=1 
        inter = 0
        s = 0
        v = 0
        
        print(f"-------------------------Simulación {num}-------------------------")
        
        inter = internet(lista[i])
        i = recorrerlista(i,lista)
        if(inter == 0):   #El cliente tiene internet
            s = sexo_cliente(lista[i])
            i = recorrerlista(i,lista)

            if(s == 0):   #El cliente es hombre
                v = ventas(lista[i],s)
                i = recorrerlista(i,lista)

            else:   #El cliente es mujer
                v = ventas(lista[i],s)
                i = recorrerlista(i,lista)
        
        else: #El cliente no tiene internet
            continue

        dventa += v
        
    print("---------------------------------------------------------------")
    print(f"\nTotal de articulos vendidos al día: {dventa}\n")
    print("------------------------Fin del Programa-----------------------")



#Inicio del programa
#Variable de entrada
n = []

#Variables de proceso
#Variables de salida

#Inicializamos variables
n = [4, 48, 80, 14, 28, 40, 63, 40, 71, 57, 72, 38, 65, 74, 59, 29, 75, 54, 91, 83, 89, 70, 10, 91, 80, 77, 11, 95, 10, 23,18,74,91,10,26,31,46,92,11,25,52,18,64,80,18,70,49,11,1,63,21,8,14,42,84,31,17,80,32,72,27,38,75,24,55,55,3,95,63,52,42,31,39,10]

#Procesamiento del programa
principal(n)
                












    
