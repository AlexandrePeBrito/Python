#Faça um programa que peça um numero inteiro positivo e em seguida mostre este numero
#invertido.
#o Exemplo:
#o 12376489
#=> 98467321

num=int(input("Informe um numero: "))

if(num>0):
    num1=str(num)
    num1=num1[::-1]
    print(num1)