#Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a
#quantidade de turmas e a quantidade de alunos para cada turma. As turmas não podem ter mais
#de 40 alunos.

num_turm=int(input("Informe o numero de turmas: "))
alunos=[]

if(num_turm>0):
    for c in range(0,num_turm):
        num_alunos=int(input(f"Informe quantos alunos tem na sala {c+1}: "))
        if(num_alunos<=40 and num_alunos>0): alunos.append(num_alunos)
    media=sum(alunos)/num_turm

    print(f"A media de alunos por turma eh {media}")    
else:
    print("Numero de turmas Invalido!")