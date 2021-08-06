#Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele 
#deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o 
#número é:
#. par ou ímpar;
#a. positivo ou negativo;
#b. inteiro ou decimal.

numb = float(input("Informe um numero: "))

if(numb%2==0):
    if(numb>0):
        if(numb == round(numb)):
            print("Este numero é PAR, POSITIVO e INTEIRO")
        else:
             print("Este numero é PAR, POSITIVO e DECIMAL")
    else:  
        if(numb == round(numb)):
            print("Este numero é PAR, NEGATIVO E INTEIRO")
        else:
            print("Este numero é PAR, NEGATIVO E DECIMAL")
else:
    if(numb>0):
        if(numb == round(numb)):
            print("Este numero é IMPAR, POSITIVO e INTEIRO")
        else:
            print("Este numero é IMPAR, POSITIVO e DECIMNAL")   
    else:  
        print("Este numero é IMPAR e eh NEGATIVO")
        if(numb == round(numb)):
            print("Este numero é IMPAR, NEGATIVO e INTEIRO")
        else:
            print("Este numero é IMPAR, NEGATIVO e DECIMNAL")