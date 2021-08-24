#Faça um programa, com uma função que necessite de um 
#argumento. A função retorna o valor de caractere ‘P’, 
#se seu argumento for positivo, e ‘N’, se seu argumento
#for zero ou negativo.
def verifNum(num):
    if(num<=0):
        return 'n'
    elif(num>0):
        return 'p'

numero=int(input("Informe um numero positivo ou negativo: "))
resp=verifNum(numero)
print(resp)