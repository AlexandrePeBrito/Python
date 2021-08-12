#Faça um Programa que leia um vetor de 10 números reais
#e mostre-os na ordem inversa.
vetor=[]
for c in range(0,5):
    vetor.append(int(input("Informe um numero: ")))
print(vetor)
vetor.reverse()
print(vetor)