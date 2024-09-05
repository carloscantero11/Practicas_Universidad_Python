"""Dadas las coordenadas X,Y de un punto en el plano cartesiano
determinar si el punto esta en el Yin o Yang o fuera de la figura (radio = 4)"""

#Inicializamos Variables:
x = y = 0.0
radio = 0.0
b = n = 0.0
s = d = 0

#Entrada de Datos:
x = float(input("Coordenada X: "))
y = float(input("Coordenada Y: "))

#Proceso:

radio = x**2 + y**2
b = x**2 + (y - 1)**2
n = x**2 + (y + 1)**2
s = (y+1)**2
d=x**2

#Imprimir Resultados:

if(radio<=4):       #Esta dentro de la figura.

    if(x>0)and(y>0):      #1er Cuadrante
        if(b<=1):
            print(f"El punto ({x};{y}) esta en el Yang")
        else:
            print(f"El punto ({x};{y}) esta en el Yin")

    elif(x<0)and(y>0):    #2do Cuadrante
        if(b<=1):
            print(f"El punto ({x};{y}) esta en el Yang")
        else:
            print(f"El punto ({x};{y}) esta en el Yang")
        
    elif(x<0)and(y<0):    #3er Cuadrante
        if(n<=1):
            print(f"El punto ({x};{y}) esta en el Yang")
        else:
            print(f"El punto ({x};{y}) esta en el Ying")

    else:                 #4to Cuadrante
        if(n<=1):
            print(f"El punto ({x};{y}) esta en el Yin")
        else:
            print(f"El punto ({x};{y}) esta en el Yin")
    
else:
    print(f"\nEl punto ({x};{y}) Esta fuera de la figura")
