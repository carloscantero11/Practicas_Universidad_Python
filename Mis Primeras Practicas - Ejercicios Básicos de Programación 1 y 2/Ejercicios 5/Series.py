#Nombre: Carlos Cantero
#C.I: 26.803.874
#Escuela: Computación
p="""– Dada la siguiente serie. Guardar en un vector llamado termino los
términos de cada uno y al final muestre el vector termino y la suma total
de la serie, Se deben calcular 4 series y un  detallado por cada serie
imprimiendo su vector termino y su suma, y por ultimo mostrar  reporte
general de la suma de la serie 
"""
print(p)
#Ejercicio
print()
print()
print("Programa para el EJERCICIO 2:")
print()
while("e"):
    n=int(input("Deme un número N POSITIVO: "))
    if(n<0):
        print("NUMERO POSITIVO. Vuelva a introducirlo")
    else:

        x=int(input("Valor de x: "))
        y=int(input("Valor de y: "))
        z=int(input("Valor de z: "))
        

        ter= [0]*n
        e=1
        ep=0
        s=0.0
        for i in range(n):
            ter[i]= (-1)**(e+1)*(x)**(e)*(z)**(e-1)/y**(n-ep)
            s+=ter[i]
            e+=1
            ep+=1
            mayor=ter[i]
            if(ter[i]>mayor):
                mayor=ter[i]
        print(end="| ")
        for i in range(n):
            print(ter[i],end=" | ")
        print()
        print(f"Sumatoria de series= {s}")
        print(f"Serie mayor= {mayor}")
        
        break
