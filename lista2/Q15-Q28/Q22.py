#Faça um Programa que peça um número inteiro e determine se ele é par ou impar. Dica: utilize o 
#operador módulo (resto da divisão).

numb = int(input("Informe um numero: "))

if(numb%2==0):
    print("Este numero eh PAR")
else:
    print("Este numero eh IMPAR")