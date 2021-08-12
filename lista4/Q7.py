#Faça um Programa que leia um vetor de 5 números inteiros,
#mostre a soma, a multiplicação e os números.
vetor=[]
mult=1
for c in range(0,5):
    vetor.append(int(input("Informe um numero: ")))
    mult=mult*vetor[c]
print(f"A soma: {sum(vetor)}\nA multiplicação: {mult}\n\
Quantidades de numeros: {len(vetor)}")