#Os números primos possuem várias aplicações dentro da Computação, por exemplo na
#Criptografia. Um número primo é aquele que é divisível apenas por um e por ele mesmo. Faça
#um programa que peça um número inteiro e determine se ele é ou não um número primo.

num = int(input("Informe um numero:"))
div=[]
d=0
c=0

if(num>0):
    for u in range(1,num+1):
        if(num%u==0):
            c+=1           
    if(c<=2): 
        print(f"O numero {num} eh um Numero PRIMO")
    else:
        print(f"O numero {num} NAO eh um Numero PRIMO")