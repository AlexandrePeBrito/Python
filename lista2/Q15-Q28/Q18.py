#Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma 
#data válida

date = input("Informe uma data (no formato dd/mm/aaaa) :")

day,month,year = date.split("/")

d = int(day)
m = int(month)
y = int(year)

if((d>0 and d<=31)and(m>0 and m<=12)and(y<=2021)):
    print("\nEsta data eh valida\n")
else:
    print("\nEsta data NAO eh valida\n")