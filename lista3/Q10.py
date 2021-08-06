#Faça um programa que receba dois números inteiros e gere os números inteiros que estão no
#intervalo compreendido por eles.

num1 = int(input("Informe um numero: "))
num2 = int(input("Informe um numero: "))

while(num1==num2):
    num1 = int(input("Informe um numero: "))
    num2 = int(input("Informe um numero: "))

if(num1<num2):
    for numeros in range(num1+1,num2):
        print(numeros)
elif(num1>num2):
    for numeros in range(num2+1,num1):
        print(numeros)
