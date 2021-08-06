#Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus 
#Farenheit

celsius = float(input("Informe a temperatura (em Celsius): "))

f = (celsius * 9/5) + 32

print("A temperatura em Farenheit eh %.1f"%f)

