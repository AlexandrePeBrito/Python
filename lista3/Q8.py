#Faça um programa que leia 5 números e informe a soma e a média dos números.

num=int(input("Infome um numero: "))
lista=[]
lista.append(num)

for c in range(1,5):
    num=int(input("Infome um numero: "))
    lista.append(num)

media= sum(lista)/len(lista)
print(f"A somas dos elementos da lista eh {sum(lista)} e a media desses numeros eh {media}")