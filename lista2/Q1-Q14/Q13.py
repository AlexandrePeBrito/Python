#Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 
#2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

number = int(input("Informe um numero correspondente ao dia da semana: "))

if(number == 1):
    print("\nDomingo")
elif(number == 2):
    print("\nSegunda")
elif(number == 3):
    print("\nTerca")
elif(number == 4):
    print("\nQuarta")
elif(number == 5):
    print("\nQuinta")
elif(number == 6):
    print("\nSexta")
elif(number == 7):
    print("\nSabado")
else:
    print("\nValor invalido!")