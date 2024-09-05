# definir la estructura básica de los alumnos
listadatos = []
lista_clientes = []
lista_productos = []

def cliente():
    cliente = {
        "correo": None,
        "cedula": None,
        "nombre": None,
        "apellido": None,
        "direccion": None,
        "calificacion": None,
        "pedidos": []
    }
    return cliente


def pedido():
    pedido = {
        "codigo": None,
        "precio_total": None,
        "direccion_facturacion":None,
        "status": None,
        "productos": []
    }
    return pedido


def producto():
    producto = {
        "referencia": None,
        "nombre": None,
        "precio": None,
        "descripcion": None,
        "cantidad": 0,
        "calificacion": None,
        "status": None,
        "categoria": None
        }
    return property


# se crea un producto nuevo
def crearproducto():
    # obtengo el cliente vacío
    objeto = producto()
    print("Insertar Cliente no debe haber clientes repetidos")
    
    # se solicita los datos al usuario
    referencia = str(input("Referencia: "))
    nombre = input("Nombre: ")
    descripcion = input("Descripcion: ")
    cantidad = int(input("Cantidad: "))
    precio = int(input("Precio: "))
    calificacion = input("Calificacion: ")
    categorias = input("Categorias(separadas en ','): ")
    status = input("Status: ")
    
    # se asignan los datos al alumno
    objeto["referencia"] = referencia
    objeto["nombre"] = nombre
    objeto["descripcion"] = descripcion
    objeto["cantidad"] = cantidad
    objeto["precio"] = precio
    objeto["calificacion"] = calificacion
    objeto["status"] = status
    objeto["categorias"] = categorias
    
    existe = False
    
    # se valida si el cliente ya existe
    for fila in lista_productos:
        if fila["referencia"] == referencia:
            existe = True
            
    if not existe:
       lista_productos.append(objeto)
       print("Producto Agregado Correctamente")
        
    else:
        print("El producto ya existe")



# se crea un cliente nuevo
def crearcliente():
    # obtengo el cliente vacío
    objeto = cliente()
    print("Insertar Cliente no debe haber clientes repetidos")
    
    # se solicita los datos al usuario
    cedula = str(input("Cedula: "))
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    correo = input("Correo: ")
    direccion = input("Direccion: ")
    calificacion = int(input("Calificacion: "))
    
    # se asignan los datos al alumno
    objeto["cedula"] = cedula
    objeto["nombre"] = nombre
    objeto["apellido"] = apellido
    objeto["correo"] = correo
    objeto["calificacion"] = calificacion
    objeto["direccion"] = direccion
        
    existe = False
    
    # se valida si el cliente ya existe
    for fila in lista_clientes:
        if fila["correo"] == correo:
            existe = True
            
    if not existe:
        # si no existe lo agrego
        lista_clientes.append(objeto)
        print("Cliente Agregado Correctamente")
    else:
        # si no existe, se muestra mensaje de error
        print("El cliente ya existe")

        
# se crea un cliente nuevo
def crearpedido():
    # obtengo el pedido vacío
    objeto = pedido()
    
    print("Insertar Alumno no debe haber alumnos repetidos")
    # se solicita los datos al usuario
    correo = str(input("Correo del cliente comprador: "))
    
    existe = False
    cliente_actual = []
    
    # se valida si el cliente ya existe
    
    for fila in lista_clientes:
        if fila["correo"] == correo:
            cliente_actual = fila

    if cliente_actual:
        # si no existe lo agrego
        precio_total = int(input("Precio: "))
        direccion_facturacion = input("Direccion de Facturacion: ")
        status = input("Estatus: ") # pagado, en espera por pago, rechazado

        # se asignan los datos al alumno
        objeto["precio_total"] = precio_total
        objeto["direccion_facturacion"] = direccion_facturacion
        objeto["status"] = status
        cliente_actual["pedidos"].append(objeto)
        print("Cliente Agregado Correctamente")

    else:
        # si no existe, se muestra mensaje de error
        print("El cliente no existe")

# lista todos los clientes existentes
def listarclientes():
    print("Listar Clientes")
    
    print("correo Nombre Apellido Direccion Calificacion")

    # recorro la lista de alumnos
    for fila in lista_clientes:
    # imprimo los alumnos en pantalla
        print("=========================================================================================")
        print(" %s %s %s %s %i" % (fila["correo"], fila["nombre"], fila["apellido"], fila["direccion"], fila["calificacion"]))

        print("Pedidos de este cliente")
        for pedido in fila["pedidos"]:
            print(pedido)

            
    # lista todos los productos existentes
def listarproductos():
    print("Listar Productos")
    print("Referencia Nombre Descripcion Precio Cantidad")
    
    # recorro la lista de alumnos
    for fila in lista_productos:
    # imprimo los alumnos en pantalla
        print("=========================================================================================")
        print(" %s %s %s %i %i" % (fila["referencia"], fila["nombre"], fila["descripcion"], fila["precio"], fila["cantidad"]))


    # consultar un determinado cliente según su correo
def consultarcliente():
    print("Consultar cliente segun correo")
    correo = str(input("Correo: "))
    
    for fila in lista_clientes:
    # válido si el correo fue encontrado
        if fila["correo"] == correo:
            # muestro los datos del alumno
            print("Cliente Encontrado")
            print("correo %s" % fila["correo"])
            print("Nombre %s" % fila["nombre"])
            print("Apellido %s" % fila["apellido"])
            print("Calificacion %s" % fila["calificacion"])
            print("Cantidad de Pedidos %s" % len(fila["pedidos"]))
            
            break

    print("Terminado")


    
    # eliminar un cliente según su correo
def eliminarcliente():
    print("eliminar Cliente según correo Introducida")
    # se solicita el correo l cliente
    correo = str(input("Correo: "))
    
    # se recorre los alumnos existentes
    for fila in lista_clientes:
        if fila["correo"] == correo:
            # si el usuario fue encontrado, se elimina
            lista_clientes.remove(fila)
            print("Cliente eliminado correctamente")
            break
    print("Terminado")


def modificarcliente():
    print("modificar datos de un cliente según correo introducido")
    correo = str(input("Correo: "))
    
    # se recorre los clientes existentes
    for fila in lista_clientes:
        if fila["correo"] == correo:
            # si se encuentra el cliente
            print("Datos Actuales del Cliente")
            print(" %s %s %s %s" % (fila["cedula"], fila["nombre"], fila["apellido"], fila["correo"]))
            print("Introducir Nuevos Datos: ")
            
            # se solicita introducir nuevos datos
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            correo = input("Correo: ")
            calificacion = int(input("Calificacion: "))
            
            # se sobreescribe los datos actuales
            fila["nombre"] = nombre
            fila["apellido"] = apellido
            fila["correo"] = correo
            fila["calificacion"] = calificacion
            print("Cliente modificado correctamente")
            break
        
    print("Terminado")




def main():
    eje = True
    print("---Menu Principal---")
    
    while eje == True:
        print("0.- Salir: ")
        print("1.- Insertar Nuevo Cliente: ")
        print("2.- Modificar cliente según su correo: ")
        print("3.- Eliminar cliente según su correo: ")
        print("4.- Consultar cliente según su correo: ")
        print("5.- Insertar Nuevo Producto")
        print("6.- Listar Productos Existentes")
        print("7.- Insertar Nuevo Pedido")
        print("8.- Listar Clientes Existentes")
        comando = int(input("/> "))
        
        if comando == 1:
            crearcliente()
        elif comando == 2:
            modificarcliente()
        elif comando == 3:
            eliminarcliente()
        elif comando == 4:
            consultarcliente()
        elif comando == 5:
            crearproducto()
        elif comando == 6:
            listarproductos()
        elif comando == 7:
            crearpedido()
        elif comando == 8:
            listarclientes()
        elif comando == 0:
            eje = False
    print("Programa Finalizado Correctamente")


main()




    
