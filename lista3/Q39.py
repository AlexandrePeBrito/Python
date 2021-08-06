#Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número
#do aluno e o segundo representando a sua altura em centímetros. Encontre o aluno mais alto e o
#mais baixo. Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com suas
#alturas.

escola={}
altura=int(input("Informe a altura do aluno em centimetros: "))
resp=1
cod=1
menor=[]
maior=[]

while(resp==1):
    aluno={cod:altura}
    escola.update(aluno)
    cod+=1
    resp=int(input("Deseja inserir outro cliente?(1->SIM 2->NAO): "))
    if(resp==1):altura=int(input("\nInforme a altura do aluno em centimetros: "))

menor.append(escola[1])
menor.append(0)  
maior.append(escola[1])
maior.append(0)  

for c in range(2,len(escola)+1):
    if(escola[c]<menor[0]):
        menor[0]=escola[c]
        menor[1]=c
    if(escola[c]>maior[0]):
        maior[0]=escola[c]
        maior[1]=c

print(f"O aluno com a menor altura tem o codigo {menor[1]} tendo {menor[0]} centimetros de altura")
print(f"O aluno com a maior altura tem o codigo {maior[1]} tendo {maior[0]} centimetros de altura")   
