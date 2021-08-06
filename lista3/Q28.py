#Faça um programa que calcule o valor total investido por um colecionador em sua coleção de
#CDs e o valor médio gasto em cada um deles. O usuário deverá informar a quantidade de CDs e
#o valor para em cada um.

num_CD=int(input("Informe o numero de CDs: "))
valores=[]

if(num_CD>0):
    for c in range(0,num_CD):
        preco=float(input(f"\nInforme o valor do CDs {c+1}: "))
        if(preco>0): valores.append(preco)
    media=sum(valores)/num_CD
    print(f"A media do valor gasto em CDs eh {media} reais")
else: 
    print("Numeros de CDs Invalido!")