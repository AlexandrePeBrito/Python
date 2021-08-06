#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu 
#peso ideal, utilizando as seguintes fórmulas:
#. Para homens: (72.7*h) - 58
#a. Para mulheres: (62.1*h) - 44.7

height = float(input("Informe sua altura: "))
sex = input("Informe o seu genero, M para masculino e F para feminino: ")

if(sex=="M") :
    weight = (72.7*height) - 58

    print("O seu peso ideal eh %.1f"%weight)
else :
    weight = (62.1*height) - 44.7

    print("O seu peso ideal eh %.1f"%weight)
