#Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a 
#temperatura em graus Celsius.
#o C = (5 * (F-32) / 9).

temp = float(input("Informe a temperatura (em Farenheit): "))

c = (5 * (temp-32) / 9)

print("A temperatura em Celsius eh %.1f" %c)