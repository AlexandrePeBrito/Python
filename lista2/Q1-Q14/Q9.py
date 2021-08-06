#Faça um Programa que leia três números e mostre-os em ordem decrescente

num1 = int(input("Informe o primeiro numero: "))
num2 = int(input("Informe o segundo numero: "))
num3 = int(input("Informe o terceiro numero: "))

if(num1>num2 and num1>num3):
    if(num2>num3):
        print('Ordem decrescente: %.0f %.0f %.0f'%(num1,num2,num3))
    else:
        print('Ordem decrescente: %.0f %.0f %.0f'%(num1,num3,num2))
elif(num2>num1 and num2>num3):
    if(num1>num3):
        print('Ordem decrescente: %.0f %.0f %.0f'%(num2,num1,num3))
    else:
        print('Ordem decrescente: %.0f %.0f %.0f'%(num2,num3,num1))
else:
    if(num2>num1):
        print('Ordem decrescente: %.0f %.0f %.0f'%(num3,num2,num1))
    else:
        print('Ordem decrescente: %.0f %.0f %.0f'%(num3,num1,num2))