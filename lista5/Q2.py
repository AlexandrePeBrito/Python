#Faça um programa para imprimir:
#* 1
#* 1 2
#* 1 2 3
#*.....
#* 1 2 3 ... n
#para um n informado pelo usuário. Use uma função que 
#receba um valor n inteiro imprima até a n-ésima linha.

def piramide(n):
    vetor=[]
    for c in range(1,n+1):
        vetor.append(c)
        print(vetor)

n=int(input("Informe um numero: "))
piramide(n)