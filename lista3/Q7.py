#Faça um programa que leia 5 números e informe o maior número.

num=int(input("Infome um numero: "))
lista=[]
lista.append(num)

for c in range(1,5):
    num=int(input("Infome um numero: "))
    lista.append(num)

print(max(lista))