#Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a 
#média alcançada por aluno e presentar:
#. A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média 
#alcançada;
#a. A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média 
#alcançada;
#b. A mensagem "Aprovado com Distinção", se a média for igual a 10.

grade1 = float(input("Informe a primeira nota: "))
grade2 = float(input("Informe a segunda nota: "))
grade3 = float(input("Informe a terceira nota: "))

media=(grade1+grade2+grade3)/3

if(media>=7):
    if(media==10):
        print("Aluno APROVADO COM DISTINÇÃO")
    else:
        print("Aluno APROVADO")
else:
    print("Aluno REPROVADO")