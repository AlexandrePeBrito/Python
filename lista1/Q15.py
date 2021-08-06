#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas 
#no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são 
#descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um 
#programa que nos dê:
#. salário bruto.
#a. quanto pagou ao INSS.
#b. quanto pagou ao sindicato.
#c. o salário líquido.
#d. calcule os descontos e o salário líquido, conforme a tabela abaixo:
#e. + Salário Bruto : R$
#f. - IR (11%) : R$
#g. - INSS (8%) : R$
#h. - Sindicato ( 5%) : R$
#= Salário Liquido : R$
#Obs.: Salário Bruto - Descontos = Salário Líquido.

hours = int(input("Informe quantas horas por mes voce trabalha: "))
pricePerHours = float(input("Informe O valor que voce recebe por hora: "))

allsalary = pricePerHours * hours
ir = allsalary*0.11
inss = allsalary*0.08
sind = allsalary*0.05
discount =ir + inss + sind
realsalary = allsalary - discount

print('Salario Bruto: R$ %.1f'%allsalary)
print('\nIR (11%%): R$ %.1f'%ir)
print('\nINSS (8%%):  R$  %.1f'%inss)
print('\nSindicato (5%%):  R$ %.1f'%sind)
print('\nSalario Liquido:  R$ %.1f' %realsalary)
