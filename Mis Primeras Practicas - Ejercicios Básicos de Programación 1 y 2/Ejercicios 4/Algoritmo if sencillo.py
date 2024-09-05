#Datos:
A=int(input("Deme un número:"))
B=int(input("Deme otro número:"))
C=int(input("Deme otro número:"))
#Condiciones:
if(A>B>C)or(A>C>B):
    print(A,"Es el número mayor")
elif(B>A>C)or(B>C>A):
    print(B,"Es el número mayor")
elif(C>A>B)or(C>B>A):
    print(C,"Es el número mayor")
elif(A>B==C):
    print(A,"Es el número mayor")
elif(B>A==C):
    print(B,"Es el número mayor")
elif(C>A==B):
    print(C,"Es el número mayor")
else:
    (A==B==C)
    print("Los tres números son iguales")
    
