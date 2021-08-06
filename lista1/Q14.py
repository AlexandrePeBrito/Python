#João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o 
#rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o 
#estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma 
#multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a 
#variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade 
#de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima 
#os dados do programa com as mensagens adequadas.

weight = float(input("Informe o peso dos peixes: "))

if(weight>50) :
    more=weight-50
    price=more*4

    print("\n\nVoce pescou %.1f quilos de peixe.\nVoce ultrapassou %.1f quilos do peso estabelecido.\nVoce devera pagar R$%.1f Reais de multa."%(weight,more,price))
else :
    print("\n\nO peso dos peixes esta dentro do regulamento")