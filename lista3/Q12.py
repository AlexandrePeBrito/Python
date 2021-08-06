#Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre
#1 a 10. O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser
#conforme o exemplo abaixo:
#o Tabuada de 5:
#o 5 X 1 = 5
#o 5 X 2 = 10
#o ...
#o 5 X 10 = 50

numero = int(input("Informe o numero para saber a tabuada: "))

while(numero<=0 or numero>10):
    numero = int(input("Informe o numero para saber a tabuada: "))

print("TABUADA")
for valor in range(1,11):
    print(f"{numero} * {valor} = {numero*valor}")