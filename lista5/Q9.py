#Reverso do número. Faça uma função que retorne o
#reverso de um número inteiro informado.
#Por exemplo: 127 -> 721.
def inverter(num):
    n=str(num)
    n= n[::-1]
    print(n)

num=int(input("Informe um numero inteiro: "))
inverter(num)