#O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
#o Até 5 Kg Acima de 5 Kg
#o File Duplo R$ 4,90 por Kg R$ 5,80 por Kg
#o Alcatra R$ 5,90 por Kg R$ 6,80 por Kg
#o Picanha R$ 6,90 por Kg R$ 7,80 por Kg
#Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de 
#carne da promoção, porém não há limites para a quantidade de carne por cliente. Se 
#compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre 
#o total da compra. Escreva um programa que peça o tipo e a quantidade de carne 
#comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra: 
#tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a 
#pagar

buy = int(input("Deseja comprar: \n1-File duplo\n2-Alcatra\n3-Picanha"))

if(buy==1):
    fileKg=float(input("Informe quantos Kg de file duplo deseja comprar: "))
    if(fileKg<5):
        filePrice=fileKg*5.9
    elif(fileKg>5):
        filePrice=fileKg*6.8
    card=input("Deseja usar o cartao tabajara? S para Sim ou N para Nao ")
    if(card=="S"or card=="s"):
        newFilePrice=filePrice*0.95
    else:
        newFilePrice=filePrice
    print("Voce Comprou %.2f Kg de File Duplo no total de R$%.2f"%(fileKg,newFilePrice))

elif(buy==2):
    alcatraKg=float(input("Informe quantos Kg de alcatra deseja comprar: "))
    if(alcatraKg<5):
        alcatraPrice=alcatraKg*4.9
    elif(alcatraKg>5):
        alcatraPrice=alcatraKg*5.8
    card=input("Deseja usar o cartao tabajara? S para Sim ou N para Nao ")
    if(card=="S"or card=="s"):
        newAlcatraPrice=alcatraPrice*0.95
    else:
        newAlcatraPrice=alcatraPrice
    print("Voce Comprou %.2f Kg de Alcatra no total de R$%.2f"%(alcatraKg,newAlcatraPrice))

elif(buy==3):
    picanhaKg=float(input("Informe quantos Kg de picanha deseja comprar: "))
    if(picanhaKg<5):
        picanhaPrice=picanhaKg*6.9
    elif(picanhaKg>5):
        picanhaPrice=picanhaKg*7.8
    card=input("Deseja usar o cartao tabajara? S para Sim ou N para Nao ")
    if(card=="S"or card=="s"):
        newPicanhaPrice=picanhaPrice*0.95
    else:
        newPicanhaPrice=picanhaPrice

    print("Voce Comprou %.2f Kg de Picanha no total de R$%.2f"%(picanhaKg,newPicanhaPrice))
    
else:
    print('Opção invalida')