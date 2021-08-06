#Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.
#Um número primo é aquele que é divisível somente por ele mesmo e por 1.

num = int(input("Informe um numero:"))
c=0
if(num>0):
    for i in range(1,num+1):
        if(num%i==0):
            c+=1
    if(c>2):
        print(f"O numero {num} não eh um numero primo")
    elif(c==2):
        print(f"O numero {num} eh um numero primo")

