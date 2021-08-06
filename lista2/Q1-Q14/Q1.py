 #Faça um Programa que peça dois números e imprima o maior deles.

num1 = int(input("Informe o primeiro numero: "))
num2 = int(input("Informe o segundo numero: "))

if(num1>num2):
    print("O maior numero eh %.0f"%num1)
elif(num2>num1):
    print("O maior numero eh %.0f"%num2)
else:
    print("Os dois numeros tem o mesmo valor %.0f"%num1)
