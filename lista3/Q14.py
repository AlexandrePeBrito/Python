#Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números
#pares e a quantidade de números impares.
lista=[]
par=0
impar=0
num = int(input("Informe um numero inteiro: "))

lista.append(num)
for c in range(1,10):
    num = int(input("Informe um numero inteiro: "))
    lista.append(num)

for c in range(0,10):
    if(lista[c]%2==0):
        par+=1
    elif(lista[c]%2==1):
        impar+=1
    
print(f"A quantidades de numeros pares eh {par} e a quantidade de numeros impares eh {impar}.")