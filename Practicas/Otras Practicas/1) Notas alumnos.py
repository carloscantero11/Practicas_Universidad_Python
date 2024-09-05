listadatos = []
    
def alumno():
    alumno = {
        "cedula": None,
        "nombre": None,
        "apellido": None,
        "correo": None,
        "nota": None
    }
    return alumno

def crear():
    objeto = alumno()
    
    print("Nuevo alumno\n")
    cedula = str(input("Cedula: "))
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    correo = input("Correo: ")
    nota = int(input("Nota: "))

    objeto["cedula"] = cedula
    objeto["nombre"] = nombre
    objeto["apellido"] = apellido
    objeto["correo"] = correo
    objeto["nota"] = nota

    existe = False

    for fila in listadatos:
        if fila["cedula"]==cedula:
            existe = True
    if not existe:
        listadatos.append(objeto)
        print("El alumno fue agregado correctamente")
    else:
        print("El alumno ya existe")

def listar():
    print("Listar notas")
    print("Cedula Nombre Apellido Correo Nota")


    for fila in listadatos:
        print(" %s %s %s %s %i" % (fila["cedula"], fila["nombre"], fila["apellido"], fila["correo"], fila["nota"]))

def consultar():
    print("Consultar Notas según cedula")
    cedula = str(input("Cedula: "))

    for fila in listadatos:
        print("Alumno Encontrado")
        
        if(fila["cedula"] == cedula):

            print("Cédula %s" % fila["cedula"])
            print("Nombre %s" % fila["nombre"])
            print("Apellido %s" % fila["apellido"])
            print("Correo %s" % fila["correo"])
            print("Nota %s" % fila["nota"])

            break
    print("Terminado")
    
def eliminar():
    print("eliminar Alumno según cédula Introducida")
    cedula = str(input("Cedula: "))

    for fila in listadatos:
        if fila["cedula"] == cedula:

            listadatos.remove(fila)
            print("Alumno eliminado correctamente")
            break
    print("Terminado")

def modificar():
    print("Modificar datos del alumno")
    cedula = str(input("Cedula: "))

    for fila in listadatos:
        if(fila["cedula"] == cedula):
            print("Datos Actuales del Alumno")
            print(" %s %s %s %s %i" % (fila["cedula"], fila["nombre"],
fila["apellido"], fila["correo"], fila["nota"]))
            print("Introducir Nuevos Datos: ")
            #se solicita introducir nuevos datos
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            correo = input("Correo: ")
            nota = int(input("Nota: "))
            #se sobreescribe los datos actuales
            fila["nombre"] = nombre
            fila["apellido"] = apellido
            fila["correo"] = correo
            fila["nota"] = nota
            print("Alumno modificado correctamente")
            break
    print("Terminado")


def main():
    eje = True
    print("---Menu Principal---")
    while eje == True:
        print("0.- Salir: ")
        print("1.- Insertar Nuevo Alumno: ")
        print("2.- Modificar alumno según su cédula: ")
        print("3.- Eliminar alumno según su cédula: ")
        print("4.- Consultar alumno según su cédula: ")
        print("5.- Listar las notas de todos los alumnos existentes")
        comando = int(input("/> "))
        if comando == 1:
            crear()
        elif comando == 2:
            modificar()
        elif comando == 3:
            eliminar()
        elif comando == 4:
            consultar()
        elif comando == 5:
            listar()
        elif comando == 0:
            eje = False
    print("Programa Finalizado Correctamente")
main()







        
