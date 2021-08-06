#Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + 
#c. O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao 
#usuário nas seguintes situações:
#a. Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o 
#programa não deve fazer pedir os demais valores, sendo encerrado;
#b. Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário 
#e encerre o programa;
#c. Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a 
#ao usuário;
#d. Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
import math

a = float(input("Informe o valor de A: "))
b = float(input("Informe o valor de B: "))
c = float(input("Informe o valor de C: "))

if(a == 0):
    print("Não eh uma equação do 2 grau")
else:
    delta = pow(b,2)-(4*a*c)

    if(delta<0):
        print("Esta equação nao possui raiz.")
    elif(delta==0):
        x=-b/(2*a)
        print("Esta equação possui apenas uma raiz que eh %.2f"%x)
    elif(delta>0):
        x1=((-b)-math.sqrt(delta))/(2*a)
        x2=((-b)+math.sqrt(delta))/(2*a)
        print("Esta equação possui duas raizes  que são x1: %.1f e x2: %.1f e o delta de valor %.0f"%(x1,x2,delta))