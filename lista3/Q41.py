#Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes
#dados: valor da dívida, valor dos juros, quantidade de parcelas e valor da parcela.
#o Os juros e a quantidade de parcelas seguem a tabela abaixo:
#o Quantidade de Parcelas % de Juros sobre o valor inicial
#da dívida
#o 1 0
#o 3 10
#o 6 15
#o 9 20
#12 25
#Exemplo de saída do programa:
#Valor da Dívida Valor dos Juros Quantidade de Parcelas
#Valor da Parcela
#R$ 1.000,00 0 1 R$
#1.000,00
#R$ 1.100,00 100 3 R$
#366,00
#R$ 1.150,00 150 6 R$
#191,67

divida=int(input("Informe o valor da divida: "))
parcelas=int(input("Informe o numero de parcelas(1,3,6,9 ou 12 vezes):"))

if(parcelas==1):
    vl_final=divida
    vl_parcela=vl_final/parcelas
    juros=0
elif(parcelas==3):
    vl_final=divida*1.1
    vl_parcela=vl_final/parcelas
    juros=10
elif(parcelas==6):
    vl_final=divida*1.15
    vl_parcela=vl_final/parcelas
    juros=15
elif(parcelas==9):
    vl_final=divida*1.2
    vl_parcela=vl_final/parcelas
    juros=20
elif(parcelas==12):
    vl_final=divida*1.25
    vl_parcela=vl_final/parcelas
    juros=25

print(f"Valor da divida = R${divida}\nNumero de parcelas = {parcelas}\nJuros= {juros}%\nValor total a pagar = R${vl_final}\nValor da parcela = R${round(vl_parcela,1)}")