#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#   a. o produto do dobro do primeiro com metade do segundo .
#   b. a soma do triplo do primeiro com o terceiro.
#   c. o terceiro elevado ao cubo.

num1 = int(input("Informe um numero inteiro: "))
num2 = int(input("Informe um numero inteiro: "))
realnum = float(input("Informe um numero real: "))


a = (num1*2) * (num2/2)
b = (num1*3) + realnum
c = pow(realnum,3)


print("O resultado da Sentença A eh %.1f\nO resultado da Sentença B eh %.1f\nO resultado da Sentença C eh %.1f"%(a,b,c))