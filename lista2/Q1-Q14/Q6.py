#Faça um Programa que leia três números e mostre o maior deles

num1 = int(input("Informe o Primeiro numero: "))
num2 = int(input("Informe o Segundo numero: "))
num3 = int(input("Informe o Terceiro numero: "))

if((num1>num2) and (num1>num3)):
    print("O primeiro numero que tem o valor %.0f eh o maior dentre os 3 numeros."%num1)
elif((num2>num1)and(num2>num3)):
    print("O segundo numero que tem o valor %.0f eh o maior dentre os 3 numeros."%num2)
else:
    print("O terceiro numero que tem o valor %.0f eh o maior dentre os 3 numeros."%num3)