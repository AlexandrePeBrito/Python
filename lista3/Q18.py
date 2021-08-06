#Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor
#e a soma dos valores.
lista=[]
num = int(input("\nInforme o valor: "))
resp = int(input("Deseja inserir outro valor?(1->SIM 2->NAO): "))

lista.append(num)

while(resp==1):
    num = int(input("\nInforme o valor: "))
    resp = int(input("Deseja inserir outro valor?(1->SIM 2->NAO): "))
    lista.append(num)

print(f"\n\nO Maior valor eh {max(lista)}")
print(f"O Menor valor eh {min(lista)}")
print(f"A soma dos valores eh {sum(lista)}")