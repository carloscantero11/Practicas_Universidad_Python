import time
#Programa de conjuntos.
#Profe, perdone que lo haga aqui, pero de verdad no sé como hacer una interfaz gráfica :c

#Datos:

A={1,2,3,4,5,6}
B={2,4,6,8,10}
C={3,6,9}
D={1,5,7,10}

#Operaciones:

E=A|B
E1=B|C|A
E2=D|A

I=A&B
I1=A&B&C
I2=D&A

R=B-C
R1=C-B
R2=A-C

W=A^B
W1=B^C
W2=C^D

M=A.issubset(B)
M1=B.issubset(C)
M2=D.issubset(B)
M3=C.issubset(D)

print("A=",A)
print("B=",B)
print("C=",C)
print("D=",D)

print("")
time.sleep(1.5)
print("Unión:")
print("")
print("A|B=",E)
print("B|C|A=",E1)
print("D|A=",E2)

print("")
time.sleep(1.5)
print("Intersección:")
print("")
print("A&B=",I)
print("A&B&C=",I1)
print("D&A=",I2)
print("")
time.sleep(1.5)
print("Diferencia:")
print("")
print("B-C=",R)
print("C-B=",R1)
print("A-C=",R2)
print("")
time.sleep(1.5)
print("Unión Exclusica:")
print("")
print("A^B=",W)
print("B^C=",W1)
print("C^D=",W2)
print("")
time.sleep(1.5)
print("Subconjuntos:")
print("")
print("¿A Es un subconjunto de B?")
time.sleep(0.5)
print(M)
print("")
print("¿B Es un subconjunto de C?")
time.sleep(0.5)
print(M1)
print("")
print("¿B Es un subconjunto de B?")
time.sleep(0.5)
print(M2)
print("")
print("¿C Es un subconjunto de D?")
time.sleep(0.5)
print(M3)
time.sleep(1.5)
print("")
print("**********************************************************************")
print("")
time.sleep(1.5)
print("Carlos Cantero")
time.sleep(0.5)
print("CI: 26.803.874")
time.sleep(0.5)
print("Lógica Simbólica")
time.sleep(0.5)
print("Sección: 204C1")
