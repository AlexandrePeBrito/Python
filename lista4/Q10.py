#Faça um Programa que leia dois vetores com 10 elementos
#cada. Gere um terceiro vetor de 20 elementos, cujos
#valores deverão ser compostos pelos elementos 
#intercalados dos dois outros vetores.
import random
vetorA=[]
vetorB=[]
vetorC=[]
for c in range(0,10):
    vetorA.append(random.randint(1,50))
    vetorC.append(vetorA[c])
    vetorB.append(random.randint(1,50))
    vetorC.append(vetorB[c])
print(vetorA)
print(vetorB)
print(vetorC)
