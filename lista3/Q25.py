#Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se
#a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é
#jovem, adulta ou idosa, conforme a média calculada.

idade=int(input("Informe a idade: "))
pessoas=[]
resp=1
p=0

if(idade>0 and idade<=110):
    while(resp==1):
        pessoas.append(idade)
        p+=1
        resp=int(input("Deseja inserir outra Nota?(1->SIM 2->NAO): "))
        if(resp==1): idade=int(input("\nInforme a idade: "))

    media=sum(pessoas)/p
    if(media>0 and media<=25): print(f"A media da turma eh {media} esta eh uma Turma de pessoas Jovens")
    elif(media>25 and media<=60): print(f"A media da turma eh {media} esta eh uma Turma de pessoas Adultas")
    elif(media>60): print(f"A media da turma eh {media} esta eh uma Turma de pessoas Idosas")
else:
    print("Idade invalida!")