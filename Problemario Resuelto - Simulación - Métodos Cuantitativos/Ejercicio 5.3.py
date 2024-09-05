#  Ejercicio 5.3
"""El clima se puede considerar un sistema estocástico, porque
evoluciona de una manera probabilística de un día a otro.
Suponga que para cierto lugar este comportamiento probabilístico
satisface la siguiente descripción: La probabilidad de un día
despejado para mañana si hoy no llueve es del 80% y la
probabilidad de un día despejado para mañana si hoy llueve
es del 40%.

Nª aleatorios: 8-1-3-7-2-7-1-6-5-5
"""
#Elaborado por: Carlos Cantero


#Lectura de Datos
#Función que determina si hoy llovio o no
def lluvia():
    print("¿Hoy llovio?\n(0) No.\n(1) Sí.")
    lluvia = int(input())
    return lluvia    #Retornamos el dato de entrada


#Función que determina la probabilidad si estara despejado o no
def clima(lista, lluvia):
    #Declaramos las variables
    i=int   
    clima = ""
    
    if(lluvia==0):   #Probabilidad si no llovio
        print("\nProbabilidad de un día despejado si llovió")
        print("\n  N° Aleatorio               Clima")
        
        for i in range(len(lista)):    #Recorremos la lista
            
            if(lista[i]<4):    #Evaluamos la probabilidad del clima
                clima = "Despejado"
            else:
                clima = "Lluvioso"
                
            print(f"      {lista[i]}                    {clima}")

    else:   #Probabilidad si llovio
        print("\nProbabilidad de un día despejado sino llovió")
        print("\n  N° Aleatorio               Clima")
        
        for i in range(len(lista)):
            
            if(lista[i]<8):
                clima = "Despejado"
            else:
                clima = "Lluvioso"
                
            print(f"      {lista[i]}                    {clima}")

#Declaración de Variable
#Var. de Entrada
na = []

#Var. de Salida
#Var. de Proceso

#Inicialización de variables
na = [8, 1, 3, 7, 2, 7, 1, 6, 5, 5]

#Procesamiento de datos
l = lluvia()
clima(na, l)
        
