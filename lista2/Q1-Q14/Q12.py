#Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são 
#do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o 
#Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a 
#empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O 
#programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no 
#mês.
#o Desconto do IR:
#o Salário Bruto até 900 (inclusive) - isento
#o Salário Bruto até 1500 (inclusive) - desconto de 5%
#o Salário Bruto até 2500 (inclusive) - desconto de 10%
#o Salário Bruto acima de 2500 - desconto de 20% 
# Imprima na tela as informações,dispostas conforme o exemplo abaixo.
#  No exemplo o valor da hora é 5 e a quantidade de hora é 220.
#o Salário Bruto: (5 * 220) : R$ 1100,00
#o (-) IR (5%) : R$ 55,00 
#o (-) INSS ( 10%) : R$ 110,00
#o FGTS (11%) : R$ 121,00
#o Total de descontos : R$ 165,00
#Salário Liquido : R$ 935,00

hours = int(input("Informe quantas horas voce trabalha por mes: "))
pricePerHours = float(input("Informe o valor da sua hora trabalhada: "))

salary = hours*pricePerHours

INSS = salary*0.1
FGTS = salary*0.11

if(salary <=900):
    IR = 0
    discount = IR + INSS
    newSalary = salary - discount
    print("\nSalário Bruto: (%.0f * %.2f) : R$ %.2f"%(hours,pricePerHours,salary)
    +"\nIR (Isento) : R$ %.0f"%IR
    +"\nINSS ( 10%%) : R$ %.2f"%INSS
    +"\nFGTS (11%%) : R$ %.2f"%FGTS
    +"\nTotal de descontos : R$ %.2f"%discount
    +"\nSalário Liquido : R$ %.2f"%newSalary)
elif(salary<=1500):
    IR = 0.05 * salary
    discount = IR + INSS
    newSalary = salary - discount
    print("\nSalário Bruto: (%.0f * %.2f) : R$ %.2f"%(hours,pricePerHours,salary)
    +"\nIR (5%%) : R$ %.0f"%IR
    +"\nINSS ( 10%%) : R$ %.2f"%INSS
    +"\nFGTS (11%%) : R$ %.2f"%FGTS
    +"\nTotal de descontos : R$ %.2f"%discount
    +"\nSalário Liquido : R$ %.2f"%newSalary)
elif(salary<=2500):
    IR = 0.1 * salary
    discount = IR + INSS
    newSalary = salary - discount
    print("\nSalário Bruto: (%.0f * %.2f) : R$ %.2f"%(hours,pricePerHours,salary)
    +"\nIR (10%%) : R$ %.0f"%IR
    +"\nINSS ( 10%%) : R$ %.2f"%INSS
    +"\nFGTS (11%%) : R$ %.2f"%FGTS
    +"\nTotal de descontos : R$ %.2f"%discount
    +"\nSalário Liquido : R$ %.2f"%newSalary)
else: 
    IR = 0.2 * salary
    discount = IR + INSS
    newSalary = salary - discount
    print("\nSalário Bruto: (%.0f * %.2f) : R$ %.2f"%(hours,pricePerHours,salary)
    +"\nIR (20%%) : R$ %.0f"%IR
    +"\nINSS ( 10%%) : R$ %.2f"%INSS
    +"\nFGTS (11%%) : R$ %.2f"%FGTS
    +"\nTotal de descontos : R$ %.2f"%discount
    +"\nSalário Liquido : R$ %.2f"%newSalary)

