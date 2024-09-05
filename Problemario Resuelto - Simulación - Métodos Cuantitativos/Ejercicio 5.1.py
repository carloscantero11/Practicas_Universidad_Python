#Ejercicio 5.1

"""
Utilice los números aleatorios de un dígito, 5, 2, 4, 9, 7, para
generar observaciones aleatorias para cada una de las siguientes
situaciones:

a) La tirada al aire de una moneda.

b) El color de la luz del semáforo que llega al azar, si el 40% del tiempo está en verde, 10% en amarillo y
   50% en rojo.
"""

#Elaborado por Carlos Cantero

#Modulos o subprograma

#Subprograma de enunciado (a)
def a():
    #Inicializamos de Variables
    k = 0
    na = [5, 2, 4, 9, 7]

    #Procesamos los datos
    print("Número Aleatorio | Resultado")
    for k in range (len(na)):
        print("      ", na[k], "        |   ", end="")
        if na[k]<5:
            print("Cara")
        else:
            print("Cruz")


#Subprograma de enunciado (b)
def b():
    #Inicializamos de Variables
    k = 0
    na = [5, 2, 4, 9, 7]
    
    #Procesamos los datos
    print("Número Aleatorio |  Resultado")
    for k in range (len(na)):
        print("      ", na[k], "        |    ", end="")
        if na[k]<4:
            print("Verde")
        elif na[k]<5:
            print("Amarillo")
        else:
            print("Rojo")



#Inicio del programa
            
print("\nSituacion (a):\n")
a()
print("\n\nSituacion (b):\n")
b()
    
