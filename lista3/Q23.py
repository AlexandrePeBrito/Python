#Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido
#pelo usuário. O programa deverá mostrar também o número de divisões que ele executou para
#encontrar os números primos. Serão avaliados o funcionamento, o estilo e o número de testes
#(divisões) executados.

num = int(input("Informe um numero:"))
div=[]
d=0
c=0
divisoes=0
if(num>0):
    for i in range(1,num+1):
        c=0
        for u in range(1,i+1):
            divisoes+=1
            if(i%u==0):
                c+=1           
        if(c<=2): 
            d+=1
            div.append(i)
        
    print(f"Os numeros Primos entre 1 e {num} sao {div} e foi necessario {divisoes} divisoes para identificar este valor.")
   

