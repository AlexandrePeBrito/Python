#Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo 
#de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
#o Média de Aproveitamento Conceito
#o Entre 9.0 e 10.0 A
#o Entre 7.5 e 9.0 B
#o Entre 6.0 e 7.5 C
#o Entre 4.0 e 6.0 D
#o Entre 4.0 e zero E
#O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a 
#mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito 
#for D ou E

grade1 = float(input("Informe a sua primeira nota: "))
grade2 = float(input("Informe a sua segunda nota: "))

media=(grade1 + grade2)/2

if(media>=9 and media<=10):
    print("Nota conceitual: A\nAprovado")
elif(media>=7.5 and media<9):
    print("Nota conceitual: B\nAprovado")
elif(media>=6 and media<7.5):
    print("Nota conceitual: C\nAprovado")
elif(media>=4 and media<6):
    print("Nota conceitual: D\nReprovado")
elif(media>=0 and media<4):
    print("Nota conceitual: E\nReprovado")