import math

def main():
    resp = 1

    while(resp==1):
        print("""\nEscriba con un número que desea calcular:

(1)Tiempo entre los 2 vehivulos.
(2)Volumen de un cilindro.
(3)Área de un rectangulo.
(4)Área de un circulo""")

        num = int(input())

        if(num==1):
            print("\nTiempo entre los 2 vehivulos: {0:2.2f} horas\n".format(tvehiculos()))

        if(num==2):
            print("\nVolumen de un cilindro.: {0:2.2f} cm^3\n".format(vcilindro()))

        if(num==3):
            print("\nÁrea de un rectangulo: {0:2d} cm^2\n".format(arectangulo()))
            
        if(num==4):
            print("\nÁrea de un circulo: {0:2.2f} cm^2\n".format(avcirculo()))

        else:
            print("\n--------------Error vuelva a intentarlo--------------\n")
            continue
        
        resp = int(input("\n(1)Seguir  (2)Salir:  \n"))

def tvehiculos():
    distancia = int(input("\nDistancia en km entre los 2 vehivulos: "))
    va = int(input("Velocidad del Vehiculo en km/h (A): "))
    vb = int(input("Velocidad del Vehiculo km/h (B): "))
    tiempo = distancia/(va+vb)
    return tiempo

def vcilindro():
    radio = int(input("\nTamaño del radio en cm: "))
    altura = int(input("Altura en cm: "))
    volumen = math.pi*radio**2*altura
    return volumen

def arectangulo():
    base = int(input("\nBase en cm: "))
    altura = int(input("Altura en cm: "))
    area = base * altura
    return area

def avcirculo():
    radio = int(input("\nTamaño del radio en cm: "))
    area = math.pi*radio**2
    return area


main()
print("-----------------------Fin del programa-----------------------")
