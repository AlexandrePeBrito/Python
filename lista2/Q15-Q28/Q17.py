#Faça um Programa que peça um número correspondente a um determinado ano e em seguida 
#informe se este ano é ou não bissexto.
year = int(input("Informe um ano: "))

if(year%4==0 and year%100!=0):
    print("\n%.0f eh um ano bissexto\n"%year)
else:
    print("\nEste ano não eh bissexto\n")