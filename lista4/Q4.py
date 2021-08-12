#Faça um Programa que leia um vetor de 10 caracteres, 
#e diga quantas consoantes foram lidas. Imprima as
#consoantes.
vetor=[]
i=0
for c in range(0,5):
    vetor.append(input("Informe uma letra: "))
for c in range(0,5):
    if(vetor[c]=='a' or vetor[c]=='e' or vetor[c]=='i'\
 or vetor[c]=='o' or vetor[c]=='u'):
        i+=1
i=5-i
print(i)
print(vetor)