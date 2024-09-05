# Carlos Cantero
# 26.803.874
# Algoritmos y Estructuras 2
# Sección: 305C2

# Versión de Python: (3.7.2)


listadatos = []

def contacto(): # Modulo que define la escructura básica del contacto
    contacto = {
        "nombre": None,
        "apellido": None,
        "correo": None,
        "lugar": None,
        "actividad": None
    }
    return contacto



def crear(): # Modulo para crear un nuevo contacto
    objeto = contacto()
    verificar = 0 #Variable que usaremos para verificar en el ciclo
    
    print("\n---------------------------Nuevo Contacto--------------------------\n")

    while(verificar==0): #Este ciclo nos permitira añadir al contacto nuevamente en caso de haber añadido un contacto existente

        #Trabaje con el metodo de formato Capitalize para que automaticamente la primera letra este en mayuscula
        nombre = input("Nombre: ").capitalize()  
        apellido = input("Apellido: ").capitalize()
        correo = input("Correo electronico: ")
        lugar = input("Lugar de trabajo: ").capitalize()
        actividad = int(input("Total de actividades a realizar: "))

        # Aquí se asignan los datos del contacto
        objeto["nombre"] = nombre
        objeto["apellido"] = apellido
        objeto["correo"] = correo
        objeto["lugar"] = lugar
        objeto["actividad"] = actividad

        existe = False

        # En esta parte del código se valida si el contacto existe o no
        for fila in listadatos:
            if(fila["nombre"]==nombre and fila["apellido"]==apellido):
                existe = True
              
        if(not existe):
            listadatos.append(objeto)
            print(f"\nEl contacto ({nombre} {apellido}) fue agregado correctamente.\n")
            verificar = 1 #Si el contacto no existe rompemos el ciclo haciendo falsa la condicion
            
        else:
            print("\n*********************ERROR AL AGREGAR CONTACTO*********************\n")
            print("Este contacto ya existe")
            print("\nVuelva a introducir los datos del contacto nuevamente.\n")
        


def listar(): # Aqui se listan todos los contactos existentes y los siguientes resultados
    actividadtotal = n = mayor = menor = 0
    promedio = 0.0
    mayornombre = menornombre = ""
    
    print("\n--------------------------Listar Contactos-------------------------\n")
    print("Nombre     Apellido            Correo           Lugar/trabajo   act\n")


    for fila in listadatos:
        print("{0:10} {1:10}  {2:25}  {3:12}   {4:2d}".format( fila["nombre"], fila["apellido"], fila["correo"], fila["lugar"], fila["actividad"]))

    for fila in listadatos:
        actividadtotal += fila["actividad"]
        n+=1

        #Contacto con menos actividades
        if(menor == 0): 
            menor = fila["actividad"]
            
        if(fila["actividad"] < menor):
            menor = fila["actividad"]
            menornombre = fila["nombre"]

        #Contacto con mas actividades
        if(fila["actividad"] > mayor):
            mayor = fila["actividad"]
            mayornombre = fila["nombre"]

    promedio = actividadtotal/n

    print(f"\n\nContacto con mas actividades a realizar: {mayornombre}")
    print(f"Total de actividades a realizar de {mayornombre}: {mayor}\n")
    print(f"Contacto con menos actividades a realizar: {menornombre}")
    print(f"Total de actividades a realizar de {menornombre}: {menor}\n")
    print("Promedio de actividades: {0:2.2f}\n".format(promedio))



def consultar(): # Se consultan los datos de un determinando contacto
    verificar = 0
    
    print("\n-------------------------Consultar Contacto------------------------\n")
    
    print("Para consultar un contacto, introduzca los siguientes datos.\n")

    while(verificar==0):
        nombre = input("Nombre: ").capitalize()
        apellido = input("Apellido: ").capitalize()

        existe = False
        
        for fila in listadatos:
            if(fila["nombre"]==nombre and fila["apellido"]==apellido): #Si el contacto existe, se mostraran sus datos en pantalla
                print("\n************************Contacto Encontrado************************\n")
                
                print("Nombre: %s" % fila["nombre"])
                print("Apellido: %s" % fila["apellido"])
                print("Correo: %s" % fila["correo"])
                print("Lugar de trabajo: %s" % fila["lugar"])
                print("Total de actividades a realizar: %s\n" % fila["actividad"])
                existe = True
                
        if(not existe):
            print("\n********************ERROR AL CONSULTAR CONTACTO********************\n")
            print("Vuelva a introducir los datos del contacto nuevamente.\n")

        else:
            verificar = 1

            

def eliminar(): # Eliminar un contacto
    verificar = 0
  
    print("\n--------------------------Eliminar Contacto------------------------\n")
    
    print("Para eliminar un contacto, introduzca los siguiendas datos:\n")

    while(verificar==0):
        nombre = input("Nombre: ").capitalize()
        apellido = input("Apellido: ").capitalize()

        existe = False
        
        for fila in listadatos:
            if(fila["nombre"]==nombre and fila["apellido"]==apellido):
                listadatos.remove(fila)
                existe = True
                
        if(not existe):
            print("\n********************ERROR AL ELIMINAR CONTACTO********************\n")
            print("Vuelva a introducir los datos del contacto nuevamente.\n")

        else:
            print(f"\nEl contacto ({nombre} {apellido}) a sido eliminado correctamente.\n")
            verificar = 1


            

def modificar(): # Aqui se podra modificar los datos del contacto
    verificar = 0
    
    print("\n-------------------------Modificar Contacto------------------------\n")

    print("Para modificar un contacto, introduzca los siguiendas datos:\n")

    while(verificar==0):
        nombre = input("Nombre: ").capitalize()
        apellido = input("Apellido: ").capitalize()

        existe = False
        
        for fila in listadatos:
            if(fila["nombre"]==nombre and fila["apellido"]==apellido): 

                #Al validar el contacto, se mostraran sus datos para despues modificarlos
                print("\nDatos Actuales del Contacto:\n")
                print("Nombre: %s" % fila["nombre"])
                print("Apellido: %s" % fila["apellido"])
                print("Correo: %s" % fila["correo"])
                print("Lugar de trabajo: %s" % fila["lugar"])
                print("Total de actividades a realizar: %s" % fila["actividad"])

                print("\n**********************Introducir Nuevos Datos**********************\n")
                
                # Se solicita introducir nuevos datos
                nombre = input("Nombre: ").capitalize()
                apellido = input("Apellido: ").capitalize()
                correo = input("Correo: ")
                lugar = input("Lugar de trabajo: ").capitalize()
                actividad = int(input("Total de actividades a realizar: "))

                
                # Se sobreescribe los datos actuales
                fila["nombre"] = nombre
                fila["apellido"] = apellido
                fila["correo"] = correo
                fila["lugar"] = lugar
                fila["actividad"] = actividad
                
                print(f"\nContacto ({nombre} {apellido}) a sido modificado correctamente.\n")
                existe = True
                
        if(not existe):
            print("\n*******************ERROR AL MODIFICAR CONTACTO********************\n")
            print("Vuelva a introducir los datos del contacto nuevamente.\n")

        else:
            verificar = 1
    


def main(): # Definimos la función principal
    cantidad = 0
    verificar = True
    validar = False #Aqui validaremos si se hay un contacto o no. De no haber ningun contacto, las demas opciones no se podran seleccionar
                    #Exceptuando la opcion de salir.
    
    while(verificar == True):
        print("\n---------------------------Menu Principal--------------------------\n")
        
        print("(0) Salir. ")
        print("(1) Agregar nuevo contacto. ")
        print("(2) Modificar contacto. ")
        print("(3) Eliminar contacto. ")
        print("(4) Consultar contacto. ")
        print("(5) Listar contactos existentes.\n")
        
        comando = int(input("/> "))
        
        if(comando == 1):
            crear()
            cantidad += 1
            
        elif(comando == 2):
            
            if(validar == True):
                modificar()
            else:
                print("\nNo se puede elegir esta opción, ya que no tiene agregado ningún contactos")
                
            
        elif(comando == 3):
            
            if(validar == True):
                eliminar()
                cantidad -= 1
            else:
                print("\nNo se puede elegir esta opción, ya que no tiene agregado ningún contactos")
                
            
        elif(comando == 4):
            
            if(validar == True):
                consultar()
            else:
                print("\nNo se puede elegir esta opción, ya que no tiene agregado ningún contactos")
                
            
        elif(comando == 5):
            
            if(validar == True):
                listar()
            else:
                print("\nNo se puede elegir esta opción, ya que no tiene agregado ningún contactos")
                
            
        elif(comando == 0):
            verificar = False  #Aquí finaliza el programa

        else: #Condicional en caso de colocar un número diferente al que se muestra en el menu de opciones
            print("\nEl número que usted marco no existe")
            print("Vuelva elegir un número\n")
            

        #Aqui evaluaremos si tenemos o no tenemos contactos en nuestra agenda
        if(cantidad>0):
            validar = True
        else:
            validar = False

            
            
    print("--------------El Programa a Finalizado Correctamente---------------")
    
main()







        
