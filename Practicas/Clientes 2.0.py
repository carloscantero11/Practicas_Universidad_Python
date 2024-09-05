listadatos = []
lista_clientes = [
    {
        "correo": "rodarge32@gmail.com",
        "cedula": "21004151",
        "nombre": "Argenis",
        "apellido": "Rodriguez",
        "direccion": "lorem ipsu",
        "calificacion": 5,
        "pedidos": [{
                        "codigo": "01",
                        "precio_total": 10,
                        "direccion_facturacion": "lorem ipsu",
                        "status": "Pagada",
                        "productos": []
                   }]
    },
    {
        "correo": "carlos.osorio@gmail.com",
        "cedula": "21004152",
        "nombre": "Carlos",
        "apellido": "Osorio",
        "direccion": "lorem ipsu",
        "calificacion": 5,
        "pedidos": [{
                        "codigo": "02",
                        "precio_total": 20,
                        "direccion_facturacion": "lorem ipsu",
                        "status": "Pagada",
                        "productos": []
                   },{
                        "codigo": "03",
                        "precio_total": 30,
                        "direccion_facturacion": "lorem ipsu",
                        "status": "Pagada",
                        "productos": []
                   },{
                        "codigo": "04",
                        "precio_total": 12,
                        "direccion_facturacion": "lorem ipsu",
                        "status": "Pagada",
                        "productos": []
                   }]
    },
    {
        "correo": "rosa.rodriguez@gmail.com",
        "cedula": "21004152",
        "nombre": "Rosa",
        "apellido": "Rodriguez",
        "direccion": "lorem ipsu",
        "calificacion": 5,
        "pedidos": [{
                        "codigo": "05",
                        "precio_total": 100,
                        "direccion_facturacion": "lorem ipsu",
                        "status": "Pagada",
                        "productos": []
                   },{
                        "codigo": "06",
                        "precio_total": 500,
                        "direccion_facturacion": "lorem ipsu",
                        "status": "Pagada",
                        "productos": []
                   },{
                        "codigo": "07",
                        "precio_total": 350,
                        "direccion_facturacion": "lorem ipsu",
                        "status": "Pagada",
                        "productos": []
                   },{
                        "codigo": "08",
                        "precio_total": 100,
                        "direccion_facturacion": "lorem ipsu",
                        "status": "Pagada",
                        "productos": []
                   }]
    },
    {
        "correo": "carmen.zapata@gmail.com",
        "cedula": "21004153",
        "nombre": "Carmen",
        "apellido": "Zapata",
        "direccion": "lorem ipsu",
        "pedidos": [{
                        "codigo": "09",
                        "precio_total": 80,
                        "direccion_facturacion": "lorem ipsu",
                        "status": "Pagada",
                        "productos": []
                   },{
                        "codigo": "10",
                        "precio_total": 1000,
                        "direccion_facturacion": "lorem ipsu",
                        "status": "Pagada",
                        "productos": []
                   }]
    }
]
lista_productos = [
{
        "referencia": "001",
        "nombre": "laptop",
        "precio": 1000,
        "descripcion": "lorem ipsu",
        "cantidad": 5,
        "calificacion": 5,
        "status": "activo",
        "categoria": "producto"
    },
{
        "referencia": "002",
        "nombre": "pentdrive",
        "precio": 20,
        "descripcion": "lorem ipsu",
        "cantidad": 5,
        "calificacion": 5,
        "status": "activo",
        "categoria": "producto"
    },
    {
        "referencia": "003",
        "nombre": "Televisor",
        "precio": 300,
        "descripcion": "lorem ipsu",
        "cantidad": 2,
        "calificacion": 5,
        "status": "activo",
        "categoria": "producto"
    },
    {
        "referencia": "004",
        "nombre": "Celular",
        "precio": 300,
        "descripcion": "lorem ipsu",
        "cantidad": 10,
        "calificacion": 4,
        "status": "activo",
        "categoria": "producto"
    },
    {
        "referencia": "005",
        "nombre": "Nevera",
        "precio": 350,
        "descripcion": "lorem ipsu",
        "cantidad": 10,
        "calificacion": 3,
        "status": "activo",
        "categoria": "producto"
    }
]


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
        "direccion_facturacion": None,
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
    return producto


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
        # si no existe lo agrego

        lista_productos.append(objeto)
        print("Producto Agregado Correctamente")
    else:
        # si no existe, se muestra mensaje de error
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

    print("Insertar Cliente no debe haber alumnos repetidos")
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
        status = input("Estatus: ")  # pagado, en espera por pago, rechazado

        # se asignan los datos al alumno
        objeto["codigo"] = len(cliente_actual["pedidos"]) + 1
        objeto["precio_total"] = precio_total
        objeto["direccion_facturacion"] = direccion_facturacion
        objeto["status"] = status
        asigproducto = True
        listaProd = []
        #Programar asignación de productos a un pedido
        while asigproducto:
            refProducto = input("Introducir referencia del producto (Escribir 'Salir' para continuar)")
            if refProducto == "Salir":
                asigproducto = False
            else:
                listaProd.append(refProducto)
                print("Producto asignado correctamente")
        objeto["productos"] = listaProd
        cliente_actual["pedidos"].append(objeto)
        print("Pedido Agregado Correctamente")
    else:
        # si no existe, se muestra mensaje de error
        print("El Pedido no existe")


# lista todos los clientes existentes
def listarclientes():
    print("Listar Clientes")
    print("correo  Nombre  Apellido  Direccion Calificacion")
    # recorro la lista de alumnos
    for fila in lista_clientes:
        # imprimo los alumnos en pantalla
        print("=========================================================================================")
        print(" %s  %s %s %s %i" % (
        fila["correo"], fila["nombre"], fila["apellido"], fila["direccion"], fila["calificacion"]))
        print("Pedidos de este cliente")
        for pedido in fila["pedidos"]:
            print(pedido)


# lista todos los productos existentes
def listarproductos():
    print("Listar Productos")
    print("Referencia  Nombre  Descripcion  Precio Cantidad")
    # recorro la lista de alumnos
    for fila in lista_productos:
        # imprimo los alumnos en pantalla
        print("=========================================================================================")
        print(" %s  %s %s %i %i" % (
        fila["referencia"], fila["nombre"], fila["descripcion"], fila["precio"], fila["cantidad"]))


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


# modificar los datos de un cliente
def modificarcliente():
    print("modificar datos de un cliente según correo introducido")
    correo = str(input("Correo: "))
    # se recorre los clientes existentes
    for fila in lista_clientes:
        if fila["correo"] == correo:
            # si se encuentra el cliente
            print("Datos Actuales del Cliente")
            print(" %s  %s %s %s" % (fila["cedula"], fila["nombre"], fila["apellido"], fila["correo"]))
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


def tresclientespartition(l, r, nums):
    # Last element will be the pivot and the first element the pointer
    pivot, ptr = nums[r], l
    for i in range(l, r):
        if len(nums[i]["pedidos"]) > len(pivot["pedidos"]):
            # Swapping values smaller than the pivot to the front
            nums[i], nums[ptr] = nums[ptr], nums[i]
            ptr += 1
    # Finally swapping the last element with the pointer indexed number
    nums[ptr], nums[r] = nums[r], nums[ptr]
    return ptr


# Tres clientes con más pedidos utilizando el algoritmo de quicksort
def tresclientesporquicksort(l, r, nums):
    if len(nums) == 1:  # Terminating Condition for recursion. VERY IMPORTANT!
        return nums
    if l < r:
        pi = tresclientespartition(l, r, nums)
        tresclientesporquicksort(l, pi - 1, nums)  # Recursively sorting the left values
        tresclientesporquicksort(pi + 1, r, nums)  # Recursively sorting the right values
    return nums

# Tres clientes con más pedidos utilizando el algoritmo de quicksort
def reporte_tresclientesporquicksort():
    list = tresclientesporquicksort(0, len(lista_clientes) - 1, lista_clientes)
    if 0 <= len(list):
        print("Cantiad de pedidos: ", len(list[0]["pedidos"]))
        print(list[0])
    if 1 <= len(list):
        print("Cantiad de pedidos: ", len(list[1]["pedidos"]))
        print(list[1])
    if 2 <= len(list):
        print("Cantiad de pedidos: ", len(list[2]["pedidos"]))
        print(list[2])
#ordenar de forma ascendente con shellsort
def reporteshellSort(array, n):

    # Rearrange elements at each n/2, n/4, n/8, ... intervals
    interval = n // 2
    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            j = i
            while j >= interval and array[j - interval]["precio_total"] > temp["precio_total"]:
                array[j] = array[j - interval]
                j -= interval

            array[j] = temp
        interval //= 2

def reporte_pedidosascendenteshellsort():
    listPedidos = []
    for cliente in lista_clientes:
        for pedido in cliente["pedidos"]:
            listPedidos.append(pedido)
    reporteshellSort(listPedidos, len(listPedidos))

    for i in listPedidos:
        print(i)


def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2

    # See if left child of root exists and is
    # greater than root
    if l < n and arr[i]["precio"] > arr[l]["precio"]:
        largest = l

        # See if right child of root exists and is
    # greater than root
    if r < n and arr[largest]["precio"] > arr[r]["precio"]:
        largest = r

        # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap

        # Heapify the root.
        heapify(arr, n, largest)

    # The main function to sort an array of given size


def heapSort(arr):
    n = len(arr)

    # Build a maxheap.
    # Since last parent will be at ((n//2)-1) we can start at that location.
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

        # One by one extract elements
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)

    # Driver code to test above

#Listar productos ordenados de forma descendente utilizando el algoritmo de heapsort
def reporte_productosascheapsort():
    heapSort(lista_productos)
    for producto in lista_productos:
        print(producto)


#monto total de compras realizadas por cliente
def montototal(cliente):
    total = 0
    for pedido in cliente["pedidos"]:
        total += pedido["precio_total"]

    return total

def merge_sort(list):
    # 1. Store the length of the list
    list_length = len(list)

    # 2. List with length less than is already sorted
    if list_length == 1:
        return list

    # 3. Identify the list midpoint and partition the list into a left_partition and a right_partition
    mid_point = list_length // 2

    # 4. To ensure all partitions are broken down into their individual components,
    # the merge_sort function is called and a partitioned portion of the list is passed as a parameter
    left_partition = merge_sort(list[:mid_point])
    right_partition = merge_sort(list[mid_point:])

    # 5. The merge_sort function returns a list composed of a sorted left and right partition.
    return merge(left_partition, right_partition)


# 6. takes in two lists and returns a sorted list made up of the content within the two lists
def merge(left, right):
    # 7. Initialize an empty list output that will be populated with sorted elements.
    # Initialize two variables i and j which are used pointers when iterating through the lists.
    output = []
    i = j = 0

    # 8. Executes the while loop if both pointers i and j are less than the length of the left and right lists
    while i < len(left) and j < len(right):
        # 9. Compare the elements at every position of both lists during each iteration
        if montototal(left[i]) > montototal(right[j]):
            # output is populated with the lesser value
            output.append(left[i])
            # 10. Move pointer to the right
            i += 1
        else:
            output.append(right[j])
            j += 1
    # 11. The remnant elements are picked from the current pointer value to the end of the respective list
    output.extend(left[i:])
    output.extend(right[j:])

    return output


#Cliente con mayor monto total de compras realizadas utilizando el algoritmo de mergesort
def reporte_totlcomprasmergesort():
    sorted_list = merge_sort(lista_clientes)

    print("El cliente con mayor monnto total de compras realizadas es: ")
    print(sorted_list[0])
    print("Monto total: ")
    print(montototal(sorted_list[0]))


def existencias_shellsort(array, n):
    # Rearrange elements at each n/2, n/4, n/8, ... intervals
    interval = n // 2
    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            j = i
            while j >= interval and array[j - interval]["cantidad"] > temp["cantidad"]:
                array[j] = array[j - interval]
                j -= interval

            array[j] = temp
        interval //= 2

def reporte_listarporexistencias():
    existencias_shellsort(lista_productos, len(lista_productos))
    for producto in lista_productos:
        print(producto)

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
        print("9.- Tres clientes con más pedidos utilizando el algoritmo de quicksort")
        print("10.- Listar pedidos de forma ascendente según su precio total utilizando el algoritmo de shellsort")
        print("11.- Listar productos ordenados de forma descendente utilizando el algoritmo de heapsort")
        print("12.- Cliente con mayor monto total de compras realizadas utilizando el algoritmo de mergesort")
        print("13.- Listar productos ordenados de forma ascendente según su cantidad de existencia")

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
        elif comando == 9:
            reporte_tresclientesporquicksort()
        elif comando == 10:
            reporte_pedidosascendenteshellsort()
        elif comando == 11:
            reporte_productosascheapsort()
        elif comando == 12:
            reporte_totlcomprasmergesort()
        elif comando == 13:
            reporte_listarporexistencias()

        elif comando == 0:
            eje = False
    print("Programa Finalizado Correctamente")


main()
