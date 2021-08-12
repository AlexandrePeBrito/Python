#Faça um Programa que leia 4 notas, mostre as notas e
#a média na tela.
notas=[]
for c in range(0,4):
    notas.append(int(input("Informe uma nota: ")))
media=sum(notas)/4