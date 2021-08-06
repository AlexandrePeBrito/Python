#Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais
#baixo, a mais gordo e o mais magro, para isto você deve fazer um programa que pergunte a
#cada um dos clientes da academia seu código, sua altura e seu peso. O final da digitação de
#dados deve ser dada quando o usuário digitar 0 (zero) no campo código. Ao encerrar o programa
#também deve ser informados os códigos e valores do clente mais alto, do mais baixo, do mais
#gordo e do mais magro, além da média das alturas e dos pesos dos clientes

academia = {}
altura=float(input("Informe a altura do cliente: "))
peso=float(input("Informe o peso do cliente: "))
resp=1
cod=0
menor=[]
maior=[]
mais=[]
menos=[]

while(resp==1):
    cliente={cod:(altura,peso)}
    academia.update(cliente)
    cod+=1
    resp=int(input("Deseja inserir outro cliente?(1->SIM 2->NAO): "))
    if(resp==1):
        altura=float(input("Informe a altura do cliente: "))
        peso=float(input("Informe o peso do cliente: "))

menor.append(academia[0][0])            #primeira casa do vetor eh a variavel
menor.append(0)                         #Segunda casa do vetor eh o cod do cliente
maior.append(academia[0][0])
maior.append(0)

mais.append(academia[0][1])
mais.append(0)
menos.append(academia[0][1])
menos.append(0)

for c in range(1,len(academia)):
    if(academia[c][0]<menor[0]):
        menor[0]=academia[c][0]
        menor[1]=c
    if(academia[c][0]>maior[0]):
        maior[0]=academia[c][0]
        maior[1]=c
    if(academia[c][1]>mais[0]):
        mais[0]=academia[c][1]
        mais[1]=c
    if(academia[c][1]<menos[0]):
        menos[0]=academia[c][1]
        menos[1]=c

print(f"O cliente com a menor altura tem o codigo {menor[1]} tendo {menor[0]} metros de altura")
print(f"O cliente com a maior altura tem o codigo {maior[1]} tendo {maior[0]} metros de altura")   
print(f"O cliente com o menor peso tem o codigo {menos[1]} tendo {menos[0]} kg ")
print(f"O cliente com o maior peso tem o codigo {mais[1]} tendo {mais[0]} kg ")


#print(academia[0][0])     #cliente 0 e altura

#len(academia)