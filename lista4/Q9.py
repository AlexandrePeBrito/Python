#Faça um Programa que leia um vetor A com 10 números
#inteiros, calcule e mostre a soma dos quadrados dos
#elementos do vetor.
vetor=[]
for c in range(0,10):
    n=int(input("Informe um numero: "))
    vetor.append(pow(n,2))
print(f"A soma dos quadrados do vetor eh {sum(vetor)}")