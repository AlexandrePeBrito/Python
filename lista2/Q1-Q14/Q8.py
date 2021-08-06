#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve 
#comprar, sabendo que a decisão é sempre pelo mais barato.

prod1 = float(input("Informe o valor do primeiro produto: "))
prod2 = float(input("Informe o valor do segundo produto: "))
prod3 = float(input("Informe o valor do terceiro produto: "))

if(prod1<prod2 and prod1<prod3):
    print("Voce devera comprar o produto 1")
elif(prod2<prod1 and prod2<prod3):
    print("Voce devera comprar o produto 2")
else:
    print("Voce devera comprar o produto 3")