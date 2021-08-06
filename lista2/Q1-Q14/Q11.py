#As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe 
#contraram para desenvolver o programa que calculará os reajustes.
#o Faça um programa que recebe o salário de um colaborador e o reajuste segundo o 
#seguinte critério, baseado no salário atual:
#o salários até R$ 280,00 (incluindo) : aumento de 20%
#o salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#o salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#o salários de R$ 1500,00 em diante : aumento de 5% 
# Após o aumento ser realizado, informe na tela:
#o o salário antes do reajuste;
#o o percentual de aumento aplicado;
#o o valor do aumento;
#o o novo salário, após o aumento.

salary = float(input("Informe o salario do colaborador: "))

if(salary<=280):
    newSalary = salary*1.2
    print("O salario antes do reajuste era de R$%.1f"%salary
    + " E o salario depois do reajuste é R$%.1f"%newSalary)
elif(salary<700):
    newSalary = salary*1.15
    print("O salario antes do reajuste era de R$%.1f"%salary
    + " E o salario depois do reajuste é R$%.1f"%newSalary)
elif(salary<1500):
    newSalary = salary*1.1
    print("O salario antes do reajuste era de R$%.1f"%salary
    + " E o salario depois do reajuste é R$%.1f"%newSalary)
else:
    newSalary = salary*1.05
    print("O salario antes do reajuste era de R$%.1f"%salary
    + " E o salario depois do reajuste é R$%.1f"%newSalary)