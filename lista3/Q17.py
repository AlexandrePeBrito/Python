#Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.:
#5!=5.4.3.2.1=120

num = int(input("Infome o numero para verificar o fatorial: "))
aux=num-1
fatorial=num

while(aux>0):
   fatorial=fatorial*aux
   aux-=1 

print(f"{num}! = {fatorial}")