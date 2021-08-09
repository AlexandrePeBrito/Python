#Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, o
#programa deve perguntar ao aluno a resposta de cada questão e ao final comparar com o
#gabarito da prova e assim calcular o total de acertos e a nota (atribuir 1 ponto por resposta
#certa). Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro aluno vai utilizar o
#sistema. Após todos os alunos terem respondido informar:
#. Maior e Menor Acerto;
#a. Total de Alunos que utilizaram o sistema;
#b. A Média das Notas da Turma.
#c. Gabarito da Prova:
#d.
#e. 01 - A
#f. 02 - B
#g. 03 - C
#h. 04 - D
#i. 05 - E
#j. 06 - E
#k. 07 - D
#l. 08 - C
#m. 09 - B
#10 - A

gabarito={1:"A",2:"C",3:"A",4:"B",5:"B",6:"C",7:"E",8:"A",9:"A",10:"C"}
escola=[]
a=0
aluno=int(input("Deseja corrigir a prova do aluno? 1-Sim 2-Nao "))

while(aluno==1):
    a+=1
    correto=0
    for c in range(1,11):
        resposta=input(f"\nInforme a Resposta da Questao {c}: ")
        if(gabarito[c]==resposta):
            correto+=1
    escola.append(correto)
    aluno=int(input("\nDeseja corrigir a prova do aluno? 1-Sim 2-Nao "))

media=sum(escola)/a
menor=min(escola)
maior=max(escola)
print(f"\nO numero total de alunos que usaram o APP foi {a}.\n\
A menor nota foi {menor}\n\
A maior nota foi {maior}\n\
A media dos alunos foi {round(media)}")
