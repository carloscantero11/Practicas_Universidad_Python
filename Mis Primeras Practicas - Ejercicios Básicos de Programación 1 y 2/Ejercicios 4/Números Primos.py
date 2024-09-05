num = i = rest = bt = 0

resp = "s"

while resp == "s":
    rest = 0
    num = int(input("Deme un número positivo: "))

    if(num<0):
        print("No se aceptan números negativos")
        continue
    else:
        i=1
        while(i<=num):
            if(num%i==0):
                rest+=1
            i+=1
        if(rest==2):
            print(f"El número {num} ES PRIMO")
        else:
            print(f"El número {num} NO ES PRIMO")

    resp = input("Pulse s para seguir o cualquier tecla para salir: ")
    print("")
    
