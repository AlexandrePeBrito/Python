#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas 
#no mês. Calcule e mostre o total do seu salário no referido mês.

hours = int(input("Informe quantas horas voce trabalha por mes: "))
dollarPerHour = float(input("Informe quanto voce recebe por hora trabalhada: "))

salary = dollarPerHour * hours

print("Seu salario eh de %.2f"%salary)
