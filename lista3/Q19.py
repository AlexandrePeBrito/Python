#Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.

lista=[]
num = int(input("\nInforme o valor: "))
if((num>=0 and num<=1000)):
    resp = int(input("Deseja inserir outro valor?(1->SIM 2->NAO): "))

    lista.append(num)

    while(resp==1):
        num = int(input("\nInforme o valor: "))
        resp = int(input("Deseja inserir outro valor?(1->SIM 2->NAO): "))
        lista.append(num)

    print(f"\n\nO Maior valor eh {max(lista)}")
    print(f"O Menor valor eh {min(lista)}")
    print(f"A soma dos valores eh {sum(lista)}")
else:
    print("Valor Invalido!! Insira um valor entre 0 e 1000")