#Faça um Programa que peça as quatro notas de 10 alunos,
#calcule e armazene num vetor a média de cada aluno,
#imprima o número de alunos com média maior ou igual
#a 7.0.
notas=[]
escola=[]
r=0
for c in range(0,10):
    for i in range(0,4):
        notas.append(int(input("informe uma nota: ")))
    escola.append(sum(notas)/4)
    notas.clear()
    if(escola[c]<7):
        r+=1
print(escola)
print(f"O numero de aprovados eh {2-r}")