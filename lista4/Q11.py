#Altere o programa anterior, intercalando 3 vetores de
#10 elementos cada.
import random
vetorA=[]
vetorB=[]
vetorS=[]
vetorC=[]
for c in range(0,10):
    vetorA.append(random.randint(1,50))
    vetorC.append(vetorA[c])
    vetorB.append(random.randint(1,50))
    vetorC.append(vetorB[c])
    vetorS.append(random.randint(1,50))
    vetorC.append(vetorS[c])
print(vetorA)
print(vetorB)
print(vetorS)
print(vetorC)