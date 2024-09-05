#Ejercicio 5.2

"""
Utilice el método congruencial mixto para generar las siguientes
sucesiones de nº aleatorios.

a) Una sucesión de 10 n.a. enteros de un dígito tal que
   Xn+1 = (Xn + 3)(módulo10) y Xo=2.
   
b) Una sucesión de 8 n.a. enteros entre 0 y 7 de un dígito tal
   que Xn+1 = (5Xn+1)(modulo8) y Xo=1.
   
c) Una sucesión de 5 n.a. enteros de un dígito tal que
   Xn+1 = (61Xn + 27)(modulo100) y Xo=100.
"""

#Elaborado por: Carlos Cantero


#Modulos o subprograma

#Subprograma para el generador congruencial mixto.
def generador(a,xi,b,m):
    x = int
    x = ((a * xi) + b) % m
    return x

#Subprograma de números aleatorios generados por este método
def aleatorio(x,m):
    u = float
    u = x / m
    return u

#Subprograma en donde se realiza la sucesión de 10 n.a
def sucesion1():
    i = int   #Var de entrada
    
    #Inicializamos variables
    ale = 2 / 10
    x0 = 2
    
    print("  n  |   xn   |   N° Aleatorio  |")
    print(f"  0  |   2    |      {ale}        |")
    
    for i in range(1,9+1):   #Aqui llamaremos a los subprogramas
        x0 = generador(1,x0,3,10)
        ale = aleatorio(x0,10)
        print(" {0:2d}  |  {1:2d}    |      {2:1.2f}       |".format(i,x0,ale))

#Subprograma en donde se realiza la sucesión de 8 n.a
def sucesion2():
    i = int   #Var de entrada

    #Inicializamos variables
    ale = 1/8
    x0 = 1
    
    print("  n  |   xn   |   N° Aleatorio  |")
    print(f"  0  |   1    |      {ale}      |")
    
    for i in range(1,7+1):    #Aqui llamaremos a los subprogramas
        x0 = generador(5,x0,1,8)
        ale = aleatorio(x0,8)
        print(" {0:2d}  |  {1:2d}    |      {2:1.4f}     |".format(i,x0,ale))
        
#Subprograma en donde se realiza la sucesión de 5 n.a
def sucesion3():
    i = int   #Var de entrada

    #Inicializamos variables
    ale = 100/100
    x0 = 100
    
    print("  n  |    xn    |   N° Aleatorio  |")
    print(f"  0  |    100   |      {ale}        |")
    
    for i in range(1,4+1):   #Aqui llamaremos a los subprogramas
        x0 = generador(61,x0,27,100)
        ale = aleatorio(x0,8)
        print(" {0:2d}  |   {1:3d}    |      {2:1.4f}     |".format(i,x0,ale))
        
#Subprograma Principal
def principal():
    #1° Sucesión
    print("\nSucesión 1:\n")
    sucesion1()

    #2° Sucesiónv
    print("\nSucesión 2:\n")
    sucesion2()

    #3° Sucesión
    print("\nSucesión 3:\n")
    sucesion3()
    
    

#Var de entrada
#Var de proceso
#Var de salida
#Inicialización de las variables
    
#Inicio del programa
principal()
    
    
