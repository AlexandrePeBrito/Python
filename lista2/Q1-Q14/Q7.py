#Faça um Programa que leia três números e mostre o maior e o menor deles

num1 = int(input("Informe o primeiro numero: "))
num2 = int(input("Informe o segundo numero: "))
num3 = int(input("Informe o terceiro numero: "))

if((num1>num2)and(num1>num3)):
    print("O Primeiro numero que tem o valor %.0f eh o maior dentre os 3 numeros."%num1)
    if(num2<num3):
        print("O Segundo numero que tem o valor %.0f eh o menor dentre os 3 numeros."%num2)
    elif(num3<num2):
        print("O Terceiro numero que tem o valor %.0f eh o menor dentre os 3 numeros."%num3)
elif((num2>num1)and(num2>num3)):
    print("O Segundo numero que tem o valor %.0f eh o maior dentre os 3 numeros."%num2)
    if(num1<num3):
        print("O Primeiro numero que tem o valor %.0f eh o menor dentre os 3 numeros."%num1)
    elif(num3<num1):
        print("O Terceiro numero que tem o valor %.0f eh o menor dentre os 3 numeros."%num3)
else:
    print("O Terceiro numero que tem o valor %.0f eh o maior dentre os 3 numeros."%num3)
    if(num1<num2):
        print("O Primeiro numero que tem o valor %.0f eh o menor dentre os 3 numeros."%num1)
    elif(num2<num1):
        print("O Segundo numero que tem o valor %.0f eh o menor dentre os 3 numeros."%num2)