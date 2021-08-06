#Altere o programa anterior permitindo ao usuário informar as populações e as taxas de
#crescimento iniciais. Valide a entrada e permita repetir a operação.

pais_a = int(input("Informe a população do Pais A: "))
tx_A = float(input("Informe a taxa de crescimento do Pais A em %: "))
tx_A=(tx_A/100)+1
pais_b = int(input("Informe a população do Pais B: "))
tx_B = float(input("Informe a taxa de crescimento do Pais B em %: "))
tx_B=(tx_B/100)+1
anos=0
print(tx_A)
print(tx_B)
while(pais_a<=pais_b):
    pais_a=pais_a*tx_A
    pais_b=pais_b*tx_B
    anos+=1

print(f"Em {anos} anos o Pais A tera {int(pais_a)} de habitantes e ira ultrapassar o Pais B que tera {int(pais_b)} habitantes")