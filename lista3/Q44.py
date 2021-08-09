#Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de
#código. Os códigos utilizados são:
#o 1 , 2, 3, 4 - Votos para os respectivos candidatos
#o (você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
#o 5 - Voto Nulo
#o 6 - Voto em Branco
#Faça um programa que calcule e mostre:
#o O total de votos para cada candidato;
#o O total de votos nulos;
#o O total de votos em branco;
#o A percentagem de votos nulos sobre o total de votos;
#o A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de
#votos tem-se o valor zero.

eleicao=[]
eleicao.append(0)
eleicao.append(0)
eleicao.append(0)
eleicao.append(0)
eleicao.append(0)
eleicao.append(0)
resp=1
v=0
#eleicao[0] = candidato 1
#eleicao[1] = candidato 2
#eleicao[2] = candidato 3

while(resp==1):
    voto=int(input("Voce deseja votar em:\n1-Claudio\n2-Ana\n3-Leo\n4-Miguel\n5-Voto Nulo\n6-Voto em Branco: "))
    v+=1
    if(voto==1):
        eleicao[0]=eleicao[0]+1
    elif(voto==2):
        eleicao[1]=eleicao[1]+1
    elif(voto==3):
        eleicao[2]=eleicao[2]+1
    elif(voto==4):
        eleicao[3]=eleicao[3]+1
    elif(voto==5):
        eleicao[4]=eleicao[4]+1
    elif(voto==6):
        eleicao[5]=eleicao[5]+1
    resp=int(input("\nTem mais alguma pessoa para votar? 1-Sim 2-Nao "))

porc_nulo=(eleicao[4]/v)*100
porc_branco=(eleicao[5]/v)*100

print(f"O candidato 1 teve {eleicao[0]} votos\n\
O candidato 2 teve {eleicao[1]} votos\n\
O candidato 3 teve {eleicao[2]} votos\n\
O candidato 4 teve {eleicao[3]} votos\n\
A eleicão teve {eleicao[4]} votos Nulos\n\
A eleicão teve {eleicao[5]} votos Brancos\n\
A porcentagem de Votos Nulos eh {round(porc_nulo)}%\n\
A porcentagem de Votos Brancos eh {round(porc_branco)}%")
