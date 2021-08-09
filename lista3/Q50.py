#Sendo H= 1 + 1/2 + 1/3 + 1/4 + ... + 1/N, Faça um programa que calcule o valor de H com N
#termos.

n=int(input("Informe o termo N que deseja visualizar: "))
serie=[]
serie_attN=[]
serie_attV=[]
cima=1
baixo=1
serie.append(cima)
serie.append(baixo)

for c in range(1,n):
    baixo+=1
    serie.append(cima)
    serie.append(baixo)
txt=f"{str(serie[0])}"
num=serie[0]/serie[1]
serie_attN.append(num)
serie_attV.append(txt)
for c in range(2,n*2,2):
    num=serie[c]/serie[c+1]
    txt=f"+ {str(serie[c])}/{str(serie[c+1])}"
    serie_attN.append(num)
    serie_attV.append(txt)

print(f"H = {serie_attV} = {round(sum(serie_attN),2)}")
    

