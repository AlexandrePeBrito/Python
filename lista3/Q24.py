#Faça um programa que calcule o mostre a média aritmética de N notas.

n=int(input("Informe a nota:"))
resp=1
notas=[]
q=0
if(n>=0 and n<=10):
    while(resp==1):
        notas.append(n)
        q+=1
        resp=int(input("Deseja inserir outra Nota?(1->SIM 2->NAO): "))
        if(resp==1): n=int(input("\nInforme a nota:"))
    media=(sum(notas)/q)

    print(f"A media das notas eh {media}")
else:
    print("Nota invalida!!")