#Foram anotadas as idades e alturas de 30 alunos. Faça
#um Programa que determine quantos alunos com mais 
#de 13 anos possuem altura inferior à média de altura
#desses alunos.
escola={}
vetor=[]
soma=0
for c in range(0,10):
    idade=int(input('Informe a idade: '))
    altura=float(input("Informe a altura: "))
    vetor.append(idade)
    escola[idade]=altura
    soma=soma+altura
qnt_al=0
media=soma/10
for c in range(0,len(escola)):
    if(vetor[c]>13):
        if(escola[vetor[c]]<media):
            qnt_al+=1
print(escola)
print(qnt_al)