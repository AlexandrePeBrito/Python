#Faça um Programa que leia 20 números inteiros e 
#armazene-os num vetor. Armazene os números pares no
#vetor PAR e os números IMPARES no vetor impar. Imprima
#os três vetores.
vetor=[]
vetorP=[]
vetorI=[]
for c in range(0,7):
    vetor.append(int(input("Informe um numero: ")))
    if(vetor[c]%2==0):
        vetorP.append(vetor[c])
    else:
        vetorI.append(vetor[c])
print(vetor)
print(vetorP)
print(vetorI)