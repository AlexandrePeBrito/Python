#Faça um programa para imprimir:
#* 1
#* 2 2
#* 3 3 3
#* .....
#* n n n n n n ... n
#para um n informado pelo usuário. Use uma função que 
#receba um valor n inteiro e
#imprima até a n-ésima linha.

def piramide(n):
    vetor=[]
    for c in range(1,n+1):
        for i in range(0,c):
            vetor.append(c)
        print(vetor)
        vetor.clear()

n=int(input("Informe um numero: "))
piramide(n)