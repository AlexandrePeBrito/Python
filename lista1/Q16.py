#Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros 
#quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 
#metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao 
#usuário a quantidades de latas de tinta a serem compradas e o preço total.

area = float(input("Informe o tamanho da area(em metros quadrados): "))
size=area*area
l=size/3
can = int(l/18)
rest=l%18

if(rest>0) :
    can=can+1
    price=can*80
    print("Vai ser nescessario %.0f Latas e o valor total eh R$%.0f"%(can,price))
else :
    price=can*80
    print("Vai ser nescessario %.0f Latas e o valor total eh R$%.0f"%(can,price))
