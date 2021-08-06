#Uma fruteira está vendendo frutas com a seguinte tabela de preços:
#o Até 5 Kg Acima de 5 Kg
#o Morango R$ 2,50 por Kg R$ 2,20 por Kg
#o Maçã R$ 1,80 por Kg R$ 1,50 por Kg
#Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 
#25,00, receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para 
#ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e 
#escreva o valor a ser pago pelo cliente.

buy = int(input("Deseja comprar: \n1-Maça\n2-Morango\n3-Ambos"))

if(buy==1):
    kgApple= float(input("Infome quantos kg de maça deseja comprar:"))

    if(kgApple<5):
        priceApple = kgApple*1.8
    else:
         priceApple = kgApple*1.5
    if(kgApple>8 or priceApple>25):
        newPrice = priceApple*0.9
    else:
        newPrice =priceApple
    print("Voce pediu %.1f KG de Maça que deu um total de R$%.2f"%(kgApple,newPrice))
elif(buy==2):
    kgStrawberry= float(input("Infome quantos kg de Morangos deseja comprar:"))

    if(kgStrawberry<5):
        priceStrawberry = kgStrawberry*2.5
    else:
         priceStrawberry = kgStrawberry*2.2
    if(kgStrawberry>8 or priceStrawberry>25):
        newPrice = priceStrawberry*0.9
    else:
        newPrice = priceStrawberry
    print("Voce pediu %.1f KG de Morangos que deu um total de R$%.2f"%(kgStrawberry,newPrice))

elif(buy==3):
    kgStrawberry= float(input("Infome quantos kg de Morangos deseja comprar:"))
    kgApple= float(input("Infome quantos kg de maça deseja comprar:"))

    if(kgApple<5):
        priceApple = kgApple*1.8
    else:
         priceApple = kgApple*1.5
    if(kgStrawberry<5):
        priceStrawberry = kgStrawberry*2.5
    else:
         priceStrawberry = kgStrawberry*2.2

    price = priceStrawberry + priceApple

    if((kgStrawberry+kgApple)>8 or price>25):
        newPrice = price*0.9
    else:
        newPrice = price
    print("Voce pediu %.1f KG de Morangos, %.1f KG de Maça que deu um total de R$%.2f"%(kgStrawberry,kgApple,newPrice))
else:
    print("Opção invalida!")