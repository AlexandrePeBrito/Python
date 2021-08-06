#O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia
#as um conjunto indeterminado de temperaturas, e informe ao final a menor e a maior
#temperaturas informadas, bem como a média das temperaturas.

temp=float(input("Informe a temperatura: "))
temperaturas=[]
resp=1

while(resp==1):
    temperaturas.append(temp)
    resp=int(input("Deseja inserir outra Temperatura?(1->SIM 2->NAO): "))
    if(resp==1): temp=float(input("nInforme a temperatura: "))

print(f"A maior temperatura foi {max(temperaturas)} e a menor temperatura foi {min(temperaturas)}")