#Faça um programa que mostre os n termos da Série a seguir:
#o S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m.
#Imprima no final a soma da série.

n=int(input("Informe o termo N que deseja visualizar: "))
serie=[]
serie_attN=[]
serie_attV=[]
cima=1
baixo=1
serie.append(cima)
serie.append(baixo)

for c in range(1,n):
    cima+=1
    baixo+=2
    serie.append(cima)
    serie.append(baixo)
txt=f"{str(serie[0])}/{str(serie[1])}"
num=serie[0]/serie[1]
serie_attN.append(num)
serie_attV.append(txt)
for c in range(2,n*2,2):
    num=serie[c]/serie[c+1]
    txt=f"+ {str(serie[c])}/{str(serie[c+1])}"
    serie_attN.append(num)
    serie_attV.append(txt)

print(f"S = {serie_attV} = {round(sum(serie_attN),2)}")
    

