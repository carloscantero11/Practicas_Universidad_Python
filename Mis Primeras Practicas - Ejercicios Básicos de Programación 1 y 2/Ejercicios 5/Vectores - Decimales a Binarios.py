n=int(input("Ingrese la cantidad del número: "))
num=[0]*n
Bin=[0]*n

print("Vector números")

for i in range(n):
    num[i]=int(input(f"Num[{i}]="))
    #Decimal binario
    aux=num[i]
    cociente=0
    while(aux!=0):
        aux=aux//2
        cociente+=1
    b=[0]*cociente
    j=0
    aux=num[i]
    while(aux!=0):
        b[j]=aux%2
        j+=1
        aux=aux//2
    cociente-=1
    valor_Bin=0
    while(cociente>=0):
        valor_Bin=valor_Bin*10+b[cociente]
        cociente-=1
    Bin[i]=valor_Bin
#Salida de datos
print("Vector decimal:")
for i in range(n):
    print(num[i],end="|")
print()
print("Vector binarios")
for i in range(n):
    print(f"{Bin[i]}",end="|")
