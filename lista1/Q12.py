#Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu 
#peso ideal, usando a seguinte fórmula: (72.7*altura) - 58

height = float(input("Informe a sua altura: "))

weight = (72.7*height) - 58

print("O seu peso ideal eh %.1f"%weight)

