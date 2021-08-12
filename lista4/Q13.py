#Faça um programa que receba a temperatura média de cada
#mês do ano e armazene-as em uma lista. Após isto, 
#calcule a média anual das temperaturas e mostre todas
#as temperaturas acima da média anual, e em que mês 
#elas ocorreram (mostrar o mês por extenso: 
#1 – Janeiro, 2– Fevereiro, . . . ).
vetor=[]
for c in range(1,13):
    vetor.append(float(input("Informe uma temperatura: ")))
media=sum(vetor)/3
print(vetor)
for c in range(1,13):
    if(vetor[c]>media):
        if(c==1):
            print(f"1-Janeiro Temp: {vetor[c]}")
        elif(c==2):
            print(f"2-Fevereiro Temp: {vetor[c]}")
        elif(c==3):
            print(f"3-Março Temp: {vetor[c]}")
        elif(c==4):
            print(f"4-Abril Temp: {vetor[c]}")
        elif(c==5):
            print(f"5-Maio Temp: {vetor[c]}")
        elif(c==6):
            print(f"6-Junho Temp: {vetor[c]}")
        elif(c==7):
            print(f"7-Julho Temp: {vetor[c]}")
        elif(c==8):
            print(f"8-Agosto Temp: {vetor[c]}")
        elif(c==9):
            print(f"9-Setembro Temp: {vetor[c]}")
        elif(c==10):
            print(f"10-Outubro Temp: {vetor[c]}")
        elif(c==11):
            print(f"11-Novembro Temp: {vetor[c]}")
        elif(c==12):
            print(f"12-Dezembro Temp: {vetor[c]}")
