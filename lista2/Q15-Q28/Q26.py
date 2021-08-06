#Um posto está vendendo combustíveis com a seguinte tabela de descontos:
#. Álcool:
#a. até 20 litros, desconto de 3% 
#b. acima de 20 litros, desconto de 5% 
# c. Gasolina:
#d. até 20 litros, desconto de 4% 
#e. acima de 20 litros, desconto de 6%. Escreva um algoritmo que leia o número de litros 
#vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), 
#calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da 
#gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.

fuel = input("Informe se Deseja Gasolina - G ou Alcool - A: ")
liters = float(input("Informe quantos litros de combustivel deseja: "))

if(fuel=="G" or fuel=="g"):
    if(liters<20):
        price=liters*2.5
        newPrice = price*0.96
    else:
        price=liters*2.5
        newPrice = price*0.94
    print("O valor total do combustivel foi %.2f"%newPrice)
elif(fuel=="A" or fuel=="a"):
    if(liters<20):
        price=liters*1.9
        newPrice = price*0.97
    else:
        price=liters*1.9
        newPrice = price*0.95
    print("O valor total do combustivel foi %.2f"%newPrice)