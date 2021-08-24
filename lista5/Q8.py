#Faça uma função que informe a quantidade de dígitos 
#de um determinado número inteiro
#informado.
def contar(num):
    n=str(num)
    print(len(n))

num=int(input("Informe um numero inteiro: "))
contar(num)