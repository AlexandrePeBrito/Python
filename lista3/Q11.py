#Altere o programa anterior para mostrar no final a soma dos números.

num1 = int(input("Informe um numero: "))
num2 = int(input("Informe um numero: "))

lista=[]

while(num1==num2):
    num1 = int(input("Informe um numero: "))
    num2 = int(input("Informe um numero: "))

if(num1<num2):
    for numeros in range(num1+1,num2):
        lista.append(numeros)
        print(numeros)
elif(num1>num2):
    for numeros in range(num2+1,num1):
        lista.append(numeros)
        print(numeros)

print(f"A soma dos numeros eh {sum(lista)}")