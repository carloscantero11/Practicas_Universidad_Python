# Determinar si un número es par o impar

# Declaramos Variables:
num = 0
x = True
d = ""

# Datos de Entrada:
while x:
    num = int(input("Número: "))
     
    if num % 2 == 0:
        print(f"El {num} es par\n")
    else:
        print(f"El {num} es impar\n")
    
    while True:  # Bucle interno para validar la entrada de 'd'
        d = input("Desea continuar (S / N): ").upper()
        
        if d == "S":
            x = False
            break
        elif d == "N":
            print()
            x = True
            break
        else:
            print("Entrada no válida. Por favor, ingrese 'S' o 'N'.\n")
