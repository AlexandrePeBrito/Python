#Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do 
#saque e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis 
#serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O 
#programa não deve se preocupar com a quantidade de notas existentes na máquina.
#. Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, 
#uma nota de 50, uma nota de 5 e uma nota de 1;
#a. Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, 
#uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.

loot = int(input("Informe o valor para o saque: "))
if(loot>=10 and loot<=600):
    money=str(loot)
    cent=int(money[0])
    dez=int(money[1])
    unit=int(money[2])
    d=dez
    u=unit
    d50 =0
    u5=0
   
    if(dez>=5): 
        d=dez-5
        d50=d50+1
    
    if(unit>=5):
        u=unit-5
        u5=u5+1
  
    print("Para sacar a quantia de R$%.0f, o programa fornece %.0f Notas de 100, %.0f Notas de 50, %.0f Notas de 10, %.0f Notas de 5 e %.0f Notas de 1"%(loot,cent,d50,d,u5,u))
else:
    print("Valor invalido")