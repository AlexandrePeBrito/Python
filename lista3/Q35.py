#Encontrar números primos é uma tarefa difícil. Faça um programa que gera uma lista dos
#números primos existentes entre 1 e um número inteiro informado pelo usuário.

num = int(input("Informe um numero:"))
div=[]
d=0
c=0

if(num>0):
    for i in range(1,num+1):
        c=0
        for u in range(1,i+1):
            if(i%u==0):
                c+=1           
        if(c<=2): 
            d+=1
            div.append(i)
        
    print(f"Os numeros Primos entre 1 e {num} sao {div}")