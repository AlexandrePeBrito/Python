#Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize 
#uma função de arredondamento.

numb = float(input("Informe um numero: "))

if(numb == round(numb)):
    print("Este numero eh inteiro!")
else:
    print("Este numero eh Decimal!")