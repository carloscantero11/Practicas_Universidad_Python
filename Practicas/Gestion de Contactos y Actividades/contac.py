

#se agrega el siguiente diccionario
#Este dicionario definira la Cargo, la clase y los atributos como
#la Actividad, catidad de actividad, fecha de inicio y fin de la actividad status de la actividad 
contactos = {
   "Cargo": { #Supervidor/Tecnicos
       "Supervisores": {      
           "Clase": {          #Electrico/Mecanico/Operador
               "Electrico": {   
                   "Asignacion": {
                       "Actividad": "Registrar novedades",  
                       "CantActividad": 6,
                       "Fecha_inicio": "10/09/2022",
                       "Fecha_fin": "18/09/2022",
                       "Status": "Cerrada"  # Por hacer/En progreso/Terminada/Cerrada
                       }
               },
               "Mecanico": {     
                   "Asignacion": {
                       "Actividad": "Cargar Nomina",  
                       "CantActividad": 10,
                       "Fecha_inicio": "10/09/2022",
                       "Fecha_fin": "18/09/2022",
                       "Status": "Por hacer"  # Por hacer/En progreso/Terminada/Cerrada
                   }
               },
               "Operador": {      
                   "Asignacion": {  
                       "Actividad": "Registrar incidentes",   
                       "CantActividad": 4,
                       "Fecha_inicio": "10/09/2022",
                       "Fecha_fin": "18/09/2022",
                       "Status": "En Proceso"   # Por hacer/En progreso/Terminada/Cerrada
                   }
               }
          }
     },
     "Tecnicos": {        
         "Clase": {     #Electrico/Electronico/Instrumentista
             "Electrico": {    
                 "Asignacion": {
                     "Actividad": "Mantenimiento a PLC",   
                     "CantActividad": 2,
                     "Fecha_inicio": "10/09/2022",
                     "Fecha_fin": "18/09/2022",
                     "Status": "Cerrada"
                 }
             },
             "Electronico": {      
                 "Asignacion": {
                     "Actividad": "Mantenimiento a cadenas",    
                     "CantActividad": 5,
                     "Fecha_inicio": "10/09/2022",
                     "Fecha_fin": "18/09/2022",
                     "Status": "En Proceso"
                 }
             },
             "Instrumentista": {     
                 "Asignacion": {
                     "Actividad": "Calibrar lazo de control",   
                     "CantActividad": 3,
                     "Fecha_inicio": "10/09/2022",
                     "Fecha_fin": "18/09/2022",
                     "Status": "Terminada"   # Por hacer/En progreso/Terminada/Cerrada
                 }
             }
         }
      }
   }
}






