#Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros 
#quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 
#metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em 
#galões de 3,6 litros, que custam R$ 25,00.
#o Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços 
#em 3 situações:
#o comprar apenas latas de 18 litros;
#o comprar apenas galões de 3,6 litros;
#o misturar latas e galões, de forma que o preço seja o menor. Acrescente 10% de folga e 
#sempre arredonde os valores para cima, isto é, considere latas cheias.

area = float(input("Informe o tamanho da area(em metros): "))
size=area*area
liters=size/6
print("Sera nescessario utilizar %.1f Litros de Tinta"%liters)

#situação A
can = int(liters/18)
rest1=liters%18

if(rest1>0) :
    can=can+1
    price1=can*80
    print("Vai ser nescessario %.0f Latas De 18 Litros e o valor total eh R$%.0f"%(can,price1))
else : 
    price1=can*80
    print("Vai ser nescessario %.0f Latas De 18 Litros e o valor total eh R$%.0f"%(can,price1))
        
#Situação B     
smallCan = int(liters/3.6)
print(smallCan)
rest2=liters%3.6

if(rest2>0):
    smallCan=smallCan+1
    price2=smallCan*25
    print("Vai ser nescessario %.0f Latas de 3.6 Litros e o valor total eh R$%.0f"%(smallCan,price2))
else:
    price2=smallCan*25
    print("Vai ser nescessario %.0f Latas de 3.6 Litros e o valor total eh R$%.0f"%(smallCan,price2))

#Situacao C
can2 = int(liters/18)
smallCan2 = int(liters%3.6)
print(smallCan2)
rest3 = liters%3.6

if(rest3>0):
    priceSmallCan=smallCan2*25
    priceBigCan=can2*80
    price3 = priceSmallCan + priceBigCan
    print("Vai ser nescessario %.0f Latas De 18 Litros e %.0f Latas de 3.6 Litros o valor total eh R$%.0f"%(can2,smallCan2,price3))
else:
    priceSmallCan=smallCan2*25
    priceBigCan=can2*80
    price3 = priceSmallCan + priceBigCan
    print("Vai ser nescessario %.0f Latas De 18 Litros e %.0f Latas de 3.6 Litros o valor total eh R$%.0f"%(can2,smallCan2,price3))