class Libro:
    def __init__(self, titulo, autor, editorial, año_publicacion):   #Constructor de Libros.
        self.titulo = titulo
        self.autor = autor
        self.editorial = editorial
        self.año_publicacion = año_publicacion


    def __str__(self):   #Cadena del objeto que se devolvera.
        return f"Título: {self.titulo}\nAutor: {self.autor}\nEditorial: {self.editorial}\nAño de Publicación: {self.año_publicacion}"
    

class Biblioteca:
    def __init__(self):   #La Biblioteca se inicia vacia.
        self.libros = []
        self.cantidad_libros = 0


    def agregar_libros(self, libro):    #Agregar libros.
        self.libros.append(libro)
        self.cantidad_libros += 1


    def eliminar_libros(self, titulo):    #Eliminar libros.
        for libro in self.libros:
            if(libro.titulo == titulo):
                self.libros.remove(libro)
                self.cantidad_libros -= 1
                print(f"\nEl libro '{titulo}' ha sido removido correctamente.")
                return
        print(f"\nEl libro '{titulo}' no se ha encontrado en la biblioteca.")
        

    def buscar_libros(self, titulo = None, autor = None):   #Buscar libros.
        libros_encontrados = []    
        if titulo:
            for libro in self.libros:
                if(libro.titulo == titulo and libro.autor == autor):
                    libros_encontrados.append(libro)
                    return libros_encontrados
                else:
                    print("Libro no encontrado\n")
    
        

    def mostrar_libros(self):    #Mostrar libros.
        for libro in self.libros:
            print(libro)
            print("\n------------------------------------------------")


biblioteca = Biblioteca()
x = False

print("\n---------------Bienvenido a la app de Biblioteca---------------")

while(x==False):
    print("\n\nElija con un número la acción que desea realizar:\n")
    print("1) Agregar un libro. \n2) Eliminar un libro. \n3) Buscar un libro. \n4) Mostrar libros. \n5) Salir de la app.\n")

    val = int(input())
    print()

    if(val == 1):    #Agregar libro
        t = input("Título del Libro: ")
        a = input("Autor del Libro: ") 
        e = input("Editorial del Libro: ") 
        ap = input("Año de publicación del Libro: ") 
        libro = Libro(t, a, e, ap)
        biblioteca.agregar_libros(libro)
        
    elif(val == 2):   #Eliminar libro
        t = input("Título del Libro: ")
        biblioteca.eliminar_libros(t)
        
    elif(val == 3):   #Buscar libro
        t = input("Título del Libro: ")
        a = input("Autor del Libro: ") 
        print("------------------------------------------------")
        libro_encontrado = biblioteca.buscar_libros(t, a)
        for libro in libro_encontrado:
            print(libro)

    elif(val == 4):
        biblioteca.mostrar_libros()

    elif(val == 5):
        x = True
        
    else:
        print("Error. Vuelva a intentarlo.")
    

"""
Datos a mejorar en el futuro:
1) Manejo de errores en las entradas.
2) Mejorar la función de busqueda.
3) Mejorar algunas cosas en la función de eliminar
"""