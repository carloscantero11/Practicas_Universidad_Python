#########################################################
##ADMINISTRADOR DE CONTACTOS, ASIGNACION DE ACTIVIDADES##
#########################################################

#Se importan los contactos del archivo contac.py
#Se crea un objeto Contacto

import json
import time
from contac import contactos

data = {}  #diccionario
data['contactos_creados'] = []  #lista

##############################################################################
class Admin_Contacto():                                                      #
##############################################################################
#---------------------------------------#Con el metodo __init__
#Metodo inicializacion init             #se inicializan los atributos 
#---------------------------------------#de los objetos ident, nombre, cargo, clase   
   def __init__(self,ident, nombre, cargo, clase):  
       self.ident = ident
       self.nombre = nombre
       self.cargo = cargo
       self.clase = clase
       
#---------------------------------------#Con el metodo configurarContactos(self) se refiere al
#Metodo Configurar contactos            #objeto instanciado de esa clase sobre el cual
#---------------------------------------#se está invocando dicho método
   def configurarContactos(self):       
       print("""\n ¿Qué Contacto trabajador desea registrar?\n
       1) Supervisores
       2) Tecnicos""")
       cargo_seleccionado = input("\n> ")
       if cargo_seleccionado == '1':
           cargo_seleccionado = "Supervisores"
           print("""\n¿Qué cargo de Supervisor deseas Registrar?\n
       1) Electrico
       2) Mecanico
       3) Operador """)
           clase_seleccionada = input("\n>")
           if clase_seleccionada == '1':
               clase_seleccionada = 'Electrico'
               self.crearContacto(cargo_seleccionado,clase_seleccionada)
               #Se llama un método que cree el Contacto
           elif clase_seleccionada == '2':
               clase_seleccionada = 'Mecanico'
               self.crearContacto(cargo_seleccionado,clase_seleccionada)
               #Se llama un método que cree el Contacto
           elif clase_seleccionada == '3':
               clase_seleccionada = 'Operador'
               self.crearContacto(cargo_seleccionado,clase_seleccionada)
               #Se llama un método que cree el Contacto
       elif cargo_seleccionado == '2': 
             cargo_seleccionado = "Tecnicos"
             print("""\n¿Qué clase de Tecnico desea registrar?\n
       1) Electrico
       2) Electronico
       3) Instrumentista """)
             clase_seleccionada = input("\n>") 
             if clase_seleccionada == '1':
               clase_seleccionada = 'Electrico'
               self.crearContacto(cargo_seleccionado,clase_seleccionada)
               #Llamaremos un método que cree el Contacto
             elif clase_seleccionada == '2':
                 clase_seleccionada = 'Electronico'
                 self.crearContacto(cargo_seleccionado,clase_seleccionada)
               #Llamaremos un método que cree el Contacto
             elif clase_seleccionada == '3':
                 clase_seleccionada = 'Instrumentista'
                 self.crearContacto(cargo_seleccionado,clase_seleccionada)
               #Llamaremos un método que cree el Contacto
       else:
            print("\nHas introducido un comando inválido")

#---------------------------------------# Se crea método llamado crearContacto(self, Cargo, clase)
#Metodo Crear contacto                  # este método recibe dos argumentos, la Cargo y la clase del Contacto que ya habrá
#---------------------------------------# seleccionado el usuario anteriormente
   def crearContacto(self, cargo_seleccionado,clase_seleccionada):
       try:
           ident =  int(input("\nIntroduzca Identificacion CI del Contacto >"))
       except:
              print("!!! Introduzca un valor numerico !!!")
              return 
       nombre = input("\nIntroduce el nombre de tu Contacto >") 
       nueva_actividad = Admin_Contacto(ident=ident, nombre=nombre, cargo=cargo_seleccionado,clase=clase_seleccionada)  
       datos = {"id": nueva_actividad.ident,        #diccionario
                "Nombre": nueva_actividad.nombre,
                "Cargo": nueva_actividad.cargo,
                "Clase": nueva_actividad.clase}
       
       print("\nEl Contacto \"{}\" ha sido creado".format(datos["Nombre"])) 
       self.guardarContacto(datos)

#---------------------------------------# Se crea método llamado guardarContacto(self, datos), este método recibe
#Metodo Guardar contacto                # un argumento (datos), que corresponde a el Id, Nombre, Cargo y clase de cargo,
#---------------------------------------# se reutiliza en la Clase Admin_Contacto y Admin_Actividades
   def guardarContacto(self, datos):
       data['contactos_creados'].append(datos)
       contacs = data['contactos_creados']
       archivo = open('contactos.json', 'w')
       json.dump(contacs, archivo, indent=4)

#---------------------------------------#Se crea método llamado guardarListaActualizada(self), 
#Metodo Guardar lista actualizada       #self se refiere al objeto instanciado de esa clase sobre el cual se 
#---------------------------------------#está invocando el método
   def guardarListaActualizada(self):
       contacs = data['contactos_creados']
       archivo = open('contactos.json', 'w')
       json.dump(contacs, archivo, indent=4)

#---------------------------------------#Se crea método llamado cargarContactos(self), self se refiere  
#Metodo Cargar contactos                #al objeto instanciado de esa clase sobre el cual se que está
#---------------------------------------#invocando el método
   def cargarContactos(self):
       try:          
           archivo = open('contactos.json')
           data['contactos_creados'] = json.load(archivo)
                  
       except FileNotFoundError:
           print("\nCreando registro de contactos...")
           time.sleep(1)
           archivo = open('contactos.json', 'a+')         

       except json.decoder.JSONDecodeError:

              print("\nNo hay Contactos Registrados, crear nuevos contactos a partir de ahora;D") 
              pass

#---------------------------------------#Se crea método llamado ModificarContacto(self), self se refiere 
#Metodo Modificar contacto              #al objeto instanciado de esa clase sobre el cual se que está
#---------------------------------------#invocando el método
   def ModificarContacto(self):
       try:
           cedula =  int(input("\nIntroduzca ID/CI del contacto que desea Modificar >"))
       except:
              print("!!! Introduzca un valor numerico !!!")
              return 
       
       for Contacto in data['contactos_creados']:           
           if Contacto['id'] == cedula:
              print("*** Contacto Encontrado ***\n" +
              "Cedula:    %s\n" % Contacto['id']+
              "Nombre:    %s\n" % Contacto['Nombre']+
              "****--Introducir los a Modificar--****")
              cedula =  int(input("ID/Cedula: "))
              nombre = input("Nombre: ")

              if (cedula ==None or nombre==""):     #se compara si algunos de los datos presentan campos vacios
                  print ("--Igrese datos nuevamente por dejar espacion es blanco--")
                  return ModificarContacto()

              #se sobreescribe los datos actuales del contacto 
              Contacto['id'] = cedula
              Contacto['Nombre'] = nombre
              print("*** Contacto: ***\n" +
              "Cedula:    %s\n" % Contacto['id']+
              "Nombre:    %s\n" % Contacto['Nombre']+
              "****--MODIFICADO CORRECTAMENTE--****")
              
              self.guardarListaActualizada() 
              break

       if Contacto['id'] != cedula:       #se recorre las filas dentro de la tabla para verificar si la cedula esta registrada o no 
          print("*** Contacto no existe ***\n")
               
#---------------------------------------#Se crea método llamado borrarContacto(self), self se refiere 
#Metodo Borrar contacto                 #al objeto instanciado de esa clase sobre el cual se que está
#---------------------------------------#invocando el método            
   def borrarContacto(self):
       try:
           cedula =  int(input("\nIntroduzca ID/CI del contacto que desea Borrar >"))
       except:
              print("!!! Introduzca un valor numerico !!!")
              return 
       
       for Contacto in data['contactos_creados'].copy():
          
           if Contacto['id'] == cedula:
              data['contactos_creados'].remove(Contacto)
              print("*** Contacto: ***\n" +
              "Cedula:    %s\n" % Contacto['id']+
              "Nombre:    %s\n" % Contacto['Nombre']+
              "****--ELIMINADO CORRECTAMENTE--****")
              
              self.guardarListaActualizada()
              break        

       if Contacto['id'] != cedula:     #se recorre las filas dentro de la tabla para verificar si la cedula esta registrada o no 
          print("*** Contacto no existe ***\n")
      
#---------------------------------------#Se crea método llamado listarContactos(self), self se refiere 
#Metodo listar contactos                #al objeto instanciado de esa clase sobre el cual se que está
#---------------------------------------#invocando el método         
   def listarContactos(self):
      if data['contactos_creados'] == []:
          print("\nNo se encuentran contactos registrados")
                            
      for Contacto in data['contactos_creados']:  
           print("""\nID: {}
                      Nombre: {}
                      Cargo: {}
                      Clase: {}\n """.format(Contacto['id'],Contacto['Nombre'],
                                      Contacto['Cargo'],Contacto['Clase']))
           
#---------------------------------------#Se crea método llamado consultarContacto(self), self se refiere         
#Metodo consultar un contacto           #al objeto instanciado de esa clase sobre el cual se que está
#---------------------------------------#invocando el método
   def consultarContacto(self):
      idEncontrada = 0
      
      print("***---Consultar un contacto introduzca ID/CI***---")

      try:
           cedula = int(input("Cedula/ID: "))
      except:
              print("!!! Introduzca un valor numerico !!!")
              return     
      
      if data['contactos_creados'] == []:           
         print("\nNo se encuentran contactos registrados")
                          
      for Contacto in data['contactos_creados']:
         
           if cedula == Contacto['id']:
              idEncontrada = Contacto['id']
              print("""\nID: {}
                      Nombre: {}
                      Cargo: {}
                      Clase: {}\n """.format(Contacto['id'],Contacto['Nombre'],
                                      Contacto['Cargo'],Contacto['Clase']))                    
      if idEncontrada != cedula:
          print ("**** Contacto no registrado ****")

#---------------------------------------#Se crea método llamado MenuContactos(self), self se refiere         
#Metodo Menu Contactos                  #al objeto instanciado de esa clase sobre el cual se que está
#---------------------------------------#invocando el método      
   def MenuContactos(self):
        i = 0
        while True:

             print("""\n=== Administrador de Contactos, agenda de trabajo ===\n
                  !Que desa hacer?\n
                  1--Registar contacto 
                  2--Listar los contactos creados
                  3--Consultar un contacto
                  4--Modificar un contacto
                  5--Borrar un contacto
                  6--Ir al menu Principal\n""")
             opcion = input("> ")

             if opcion == '1':        #Opcion 1
                self.configurarContactos()

             elif opcion == '2':      #Opcion 2
                  self.listarContactos()
                   
             elif opcion == '3':      #Opcion 3
                  self.consultarContacto()

             elif opcion == '4':      #Opcion 4
                  self.ModificarContacto()

             elif opcion == '5':      #Opcion 5
                  self.borrarContacto()

             elif opcion == '6':      #Opcion 6
                  MenuPrincipal.__init__(self)

             else:
                  print("\nHas introducido un comando inválido")
               
##############################################################################
class Admin_Actividad():                                                     #
##############################################################################
#---------------------------------------#Con el metodo __init__ se inicializan los atributos
#Metodo inicializacion init             #de los objetos ident, nombre, cargo, clase, actividad,
#---------------------------------------#cantActividad, f_ini, f_fin, status      
   def __init__(self,ident, nombre, cargo, clase, actividad, cantActividad, f_ini, f_fin, status):
       self.ident = ident
       self.nombre = nombre
       self.cargo = cargo
       self.clase = clase
       self.actividad = actividad
       self.cantActividad = cantActividad
       self.f_ini = f_ini
       self.f_fin = f_fin
       self.status = status

#---------------------------------------#Se crea método llamado AsignarActividad(self), self se refiere
#Metodo Asignar Actividad               #al objeto instanciado de esa clase sobre el cual se que está
#---------------------------------------#invocando el método
   def AsignarActividad(self):
       try:
            cedula =  int(input("\n!!--Introduzca ID/CI del contacto asignar actividad--!! >"))
       except:
              print("!!! Introduzca un valor numerico !!!")
              return
            
       for Contacto in data['contactos_creados']:
           if Contacto['id'] == cedula:        
              print("*** Contacto Encontrado.. Asigne la actividad!! ***\n" +
              "Cedula:    %s\n" % Contacto['id']+
              "Nombre:    %s\n" % Contacto['Nombre']+
              "****--INTRODUCIR ACTIVIDAD ASIGNAR--****")
              
              actividad = input("Actividad: ")
              try:
                  cantActividad = int(input("Cantidad actividades: "))
              except:
                     print("!!! Introduzca un valor numerico !!!")
                     return 
              fecha_inicio = input("Fecha inicio: ")
              fecha_fin = input("Fecha fin: ")
              status = input("Status: ")
              
              if (actividad =="" or cantActividad==None
                  or fecha_inicio=="" or fecha_fin=="" or status=="" ):     #se compara si algunos de los datos presentan campos vacios
                  print ("--Igrese datos nuevamente por dejar espacion es blanco--")
                  return AsignarActividad()

              #se sobreescribe los datos actuales de la actividad asignada del contacto               
              Contacto['Actividad'] = actividad
              Contacto['CantActividad'] = cantActividad
              Contacto['Fecha_inicio'] = fecha_inicio
              Contacto['Fecha_fin'] = fecha_fin
              Contacto['Status'] = status

              print("*** Contacto: ***\n" +
              "Cedula: %s\n" % Contacto['id']+
              "Nombre: %s\n" % Contacto['Nombre']+
              "Actividad: %s\n" % Contacto['Actividad']+
              "Fecha inicio: %s\n" % Contacto['Fecha_inicio']+
              "Fecha fin: %s\n" % Contacto['Fecha_fin']+
              "Status: %s\n" % Contacto['Status']+
              "****--ACTIVIDADES ASIGNADAS CORRECTAMENTE--****")
              
              Admin_Contacto.guardarListaActualizada(self) #Se accede a la calse Admin_Contacto para reutilizar el metodo guardarListaActualizada
              break

       if Contacto['id'] != cedula:       #se recorre las filas dentro de la tabla para verificar si la cedula esta registrada o no 
          print("*** Contacto no existe ***\n")

#---------------------------------------#Se crea método llamado ModificarActividad(self), self se refiere
#Metodo Modificar Actividad             #al objeto instanciado de esa clase sobre el cual se que está
#---------------------------------------#invocando el método
   def ModificarActividad(self):
       try:
             cedula =  int(input("\nIntroduzca ID/CI del contacto le requiere modificar la actividad >"))
       except:
              print("!!! Introduzca un valor numerico !!!")
              return
      
       for Contacto in data['contactos_creados']:
           if cedula == Contacto['id'] and ("id"and"Nombre"and"Cargo"and"Clase"and"Actividad"and"CantActividad"and"Fecha_inicio"and"Fecha_fin"and"Status") in Contacto:    
            
              print("*** Contacto Encontrado.. Asigne la actividad!! ***\n" +
              "Cedula:    %s\n" % Contacto['id']+
              "Nombre:    %s\n" % Contacto['Nombre']+
              "****--Introducir los datos Modificar--****")
              
              actividad = input("Actividad: ")
              try:
                  cantActividad = int(input("Cantidad actividades: "))
              except:
                     print("!!! Introduzca un valor numerico !!!")
                     return 
              fecha_inicio = input("Fecha inicio: ")
              fecha_fin = input("Fecha fin: ")
              status = input("Status: ")
              
              if (actividad =="" or cantActividad==None
                  or fecha_inicio=="" or fecha_fin=="" or status=="" ):     #se compara si algunos de los datos presentan campos vacios
                  print ("--Igrese datos nuevamente por dejar espacion es blanco--")
                  return ModificarActividad()

              #se sobreescribe los datos actuales de la actividad asignada del contacto               
              Contacto['Actividad'] = actividad
              Contacto['CantActividad'] = cantActividad
              Contacto['Fecha_inicio'] = fecha_inicio
              Contacto['Fecha_fin'] = fecha_fin
              Contacto['Status'] = status

              print("*** Contacto: ***\n" +
              "Cedula: %s\n" % Contacto['id']+
              "Nombre: %s\n" % Contacto['Nombre']+
              "Actividad: %s\n" % Contacto['Actividad']+
              "Fecha inicio: %s\n" % Contacto['Fecha_inicio']+
              "Fecha fin: %s\n" % Contacto['Fecha_fin']+
              "Status: %s\n" % Contacto['Status']+
              "****--ACTIVIDADES MODIFICADA CORRECTAMENTE--****")
              
              Admin_Contacto.guardarListaActualizada(self) #Se accede a la calse Admin_Contacto para reutilizar el metodo guardarListaActualizada
              break
           elif cedula == Contacto['id'] and ("id"and"Nombre"and"Cargo"and"Clase") in Contacto: 
                print("*** Contacto: ***\n" +
                     "Cedula:    %s\n" % Contacto['id']+
                     "Nombre:    %s\n" % Contacto['Nombre']+
                     "****--CONTACTO SIN ACTIVIDAD, ASIGNE ACTIVIDAD EN OPCION 1--****")
                return 

       if Contacto['id'] != cedula:       #se recorre las filas dentro de la tabla para verificar si la cedula esta registrada o no 
          print("*** Contacto no existe ***\n")
                        
#---------------------------------------#
#Metodo Borrar Actividad                #
#---------------------------------------#
   def borrarActividad(self):
       try:
             cedula =  int(input("\nIntroduzca ID/CI del contacto que se requiere borrar actividad >"))
       except:
              print("!!! Introduzca un valor numerico !!!")
              return
       
       for Contacto in data['contactos_creados'].copy():
          
           if cedula == Contacto['id'] and ("id"and"Nombre"and"Cargo"and"Clase"and"Actividad"and"CantActividad"and"Fecha_inicio"and"Fecha_fin"and"Status") in Contacto:   
              del (Contacto['Actividad'],Contacto['CantActividad'],
                   Contacto['Fecha_inicio'],Contacto['Fecha_fin'],
                   Contacto['Status'])
              print("*** Contacto: ***\n" +
              "Cedula:    %s\n" % Contacto['id']+
              "Nombre:    %s\n" % Contacto['Nombre']+
              "****--ACTIVIDAD ELIMINADA CORRECTAMENTE--****")
              
              Admin_Contacto.guardarListaActualizada(self) #Se accede a la clase Admin_Contacto para reutilizar el metodo guardarListaActualizada
              break
            
           elif cedula == Contacto['id'] and ("id"and"Nombre"and"Cargo"and"Clase") in Contacto: 
              print("*** Contacto: ***\n" +
                     "Cedula:    %s\n" % Contacto['id']+
                     "Nombre:    %s\n" % Contacto['Nombre']+
                  "****--CONTACTO NO TIENE ACTIVIDAD ASIGNADA--****")
              return 

       if Contacto['id'] != cedula:     #se recorre las filas dentro de la tabla para verificar si la cedula esta registrada o no 
          print("*** Contacto no existe ***\n")
      
#---------------------------------------#
#Metodo listar actividades              #
#---------------------------------------#    
   def listarActividades(self):
       for Contacto in data['contactos_creados']:   
           if ("id"and"Nombre"and"Cargo"and"Clase"and"Actividad"and"CantActividad"and"Fecha_inicio"and"Fecha_fin"and"Status") in Contacto:
              print("""\n ID: {}
                 Nombre: {}
                 Cargo: {}
                 Clase: {}
                 Actividad: {}
                 CantActividad: {}
                 Fecha_inicio: {}
                 Fecha_fin: {}
                 Status: {}\n """.format(Contacto['id'],Contacto['Nombre'],
                                         Contacto['Cargo'],Contacto['Clase'],
                                         Contacto['Actividad'],Contacto['CantActividad'],
                                         Contacto['Fecha_inicio'],Contacto['Fecha_fin'],
                                         Contacto['Status']))
   
#---------------------------------------#
#Metodo consultar una actividad         #
#---------------------------------------#
   def consultarActividad(self):
      idEncontrada = 0      
      print("***---Consultar actividad!! introduzca ID/CI del contacto***---")

      try:
          cedula = int(input("Cedula/ID: "))
      except:
              print("!!! Introduzca un valor numerico !!!")
              return
           
      if data['contactos_creados'] == []:           
         print("\nNo se encuentran contactos/actividades registrados")
                          
      for Contacto in data['contactos_creados']:
         
          if cedula == Contacto['id'] and ("id"and"Nombre"and"Cargo"and"Clase"and"Actividad"and"CantActividad"and"Fecha_inicio"and"Fecha_fin"and"Status") in Contacto:
             idEncontrada = Contacto['id']
             print("""\nID: {}
                 Nombre: {}
                 Cargo: {}
                 Clase: {}
                 Actividad: {}
                 CantActividad {}
                 Status: {}\n """.format(Contacto['id'],Contacto['Nombre'],
                                         Contacto['Cargo'],Contacto['Clase'],
                                         Contacto['Actividad'],Contacto['CantActividad'],
                                         Contacto['Fecha_inicio'],Contacto['Fecha_fin'],
                                         Contacto['Status']))
              
          elif cedula == Contacto['id'] and ("id"and"Nombre"and"Cargo"and"Clase") in Contacto: 
              print("*** Contacto: ***\n" +
                     "Cedula:    %s\n" % Contacto['id']+
                     "Nombre:    %s\n" % Contacto['Nombre']+
                  "****--CONTACTO NO TIENE ACTIVIDAD ASIGNADA--****")
              return
                         
      if idEncontrada != cedula:
          print ("**** Contacto no registrado ****")

#---------------------------------------#
#Metodo Menu de Actividades             #
#---------------------------------------#
   def MenuActividades(self):
        while True:
             print("""\n=== Administrador de actividades de trabajo ===\n
                  !Que desa hacer?\n
                  1--Asignar Actividad
                  2--Listar actividades
                  3--Consultar Actividad
                  4--Modificar Actividad
                  5--Borrar Actividad
                  6--Ir al menuPrincipal\n""")
             opcion = input("> ")

             if opcion == '1':        #Opcion 1
                self.AsignarActividad()

             elif opcion == '2':      #Opcion 2
                  self.listarActividades()
                   
             elif opcion == '3':      #Opcion 3
                  self.consultarActividad()

             elif opcion == '4':      #Opcion 4
                  self.ModificarActividad()

             elif opcion == '5':      #Opcion 5
                  self.borrarActividad()

             elif opcion == '6':      #Opcion 6
                  MenuPrincipal.__init__(self)

             else:
                  print("\nHas introducido un comando inválido")

##############################################################################
class MenuPrincipal():                                                       #
##############################################################################
#---------------------------------------#
            #
#---------------------------------------#
    def __init__(self):
        self.Admin_Contacto = Admin_Contacto
        self.Admin_Actividad = Admin_Actividad 

        while True:

             print("""\n=== Bienvenidos al gestor de actividades de trabajo ===\n
                  !Que desa hacer?\n
                  1--Crear/Administrar contactos
                  2--Crear/Administrar actividades a contactos
                  3--Salir\n""")
             
             opcion = input("> ")

             if opcion == '1':        #Opcion 1
                Admin_Contacto.MenuContactos(self)

             elif opcion == '2':      #Opcion 2
                  Admin_Actividad.MenuActividades(self) 

             elif opcion == '3':      #Opcion 3
                  print("\n...Saliendo del programa...")
                  time.sleep(2)
                  quit()

             else:
                  print("\nHas introducido un comando inválido")
   
############################################################################## Se crea la clase llamada Iniciar y decirle que herede                 
class Iniciar(Admin_Contacto, Admin_Actividad ):   #Constructor clase Iniciar# de la clase Admin_Contacto,Admin_Actividad y en su constructores 
############################################################################## correspondientes se llaman a sus respectivos metodos.
#---------------------------------------#
#            #
#---------------------------------------#
     def __init__(self):

       self.cargarContactos()
       MenuPrincipal.__init__(self)
             
Iniciar()



















