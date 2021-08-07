#Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de
#trânsito. Foram obtidos os seguintes dados:
#. Código da cidade;
#a. Número de veículos de passeio (em 1999);
#b. Número de acidentes de trânsito com vítimas (em 1999). Deseja-se saber:
#c. Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
#d. Qual a média de veículos nas cinco cidades juntas;
#e. Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de
#passeio.

cidades={}
cod=1
num_veic=int(input(f"Informe o numeros de veiculos(em 1999) da cidade {cod}: "))
num_aci=int(input(f"Informe o numero de acidentes(em 1999) da cidade {cod}: "))
veic=[]
acid=[]
menor=[]
maior=[]

municipios={cod:(num_veic,num_aci)}
cidades.update(municipios)

for c in range(1,5):
    cod+=1
    veic.append(num_veic)
    acid.append(num_aci)
    num_veic=int(input(f"\nInforme o numeros de veiculos(em 1999) da cidade {cod}: "))
    num_aci=int(input(f"\nInforme o numero de acidentes(em 1999) da cidade {cod}: "))
    municipios={cod:(num_veic,num_aci)}
    cidades.update(municipios)

media_veic=sum(veic)/5
media_aci=sum(acid)/5

menor.append(cidades[1][1])
menor.append(0)  
maior.append(cidades[1][1])
maior.append(0)  

for c in range(1,len(cidades)+1):
    if(cidades[c][1]<menor[0]):
        menor[0]=cidades[c][1]
        menor[1]=c
    if(cidades[c][1]>maior[0]):
        maior[0]=cidades[c][1]
        maior[1]=c
    
print(f"A cidade com o menor indice de acidentes tem o codigo {menor[1]} tendo {menor[0]} acidentes")
print(f"A cidade com o maior indice de acidentes tem o codigo {maior[1]} tendo {maior[0]} acidentes")   