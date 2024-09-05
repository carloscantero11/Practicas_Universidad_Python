#Inicializamos variables

equipos = []
resultado = []
part = 2

# Datos de entrada


for i in range(0,part):
    print(f"\n{i+1}° Partido:\n")
    equipo = []
    equipo.append(input("Nombre del equipo 1 del %d° partido: " % (i+1)))
    equipo.append(input("Nombre del equipo 2 del %d° partido: " % (i+1)))
    equipos.append(equipo)

    print()
    print("Goles: \n")

    goles = []
    goles.append(int(input("Goles metidos por el equipo %s: " % (equipo[0]))))
    goles.append(int(input("Goles metidos por el equipo %s: " % (equipo[1]))))
    resultado.append(goles)
    print()


print("\n=====================Resultados====================\n")


for equipo,goles in zip(equipos,resultado):
    print(equipo[0],goles[0],"-",goles[1],equipo[1],"",end="\n\n")
        
    if goles[0] > goles[1]:
        print(f"Gano el equipo -> {equipo[0]}")
        print(f"Perdio el equipo -> {equipo[1]}\n")
        
    elif goles[1] > goles[0]:
        print(f"Gano el equipo -> {equipo[1]}")
        print(f"Perdio el equipo -> {equipo[0]}\n")
        
    else:
        print("Empate\n")
