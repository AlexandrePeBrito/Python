#Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
#. Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
#a. Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
#b. A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do
#percentual do ano anterior. Faça um programa que determine o salário atual desse
#funcionário. Após concluir isto, altere o programa permitindo que o usuário digite o
#salário inicial do funcionário.

salario_inicial=float("Informe o salario inicial do funcionario: ")
aumento=0.015
tempo=2021-1996

for c in range(1,tempo):
    salario_nv=salario_inicial*(aumento+1)
    aumento=aumento*2

print(f"O salario atual do funcionario eh R${salario_nv}")