#Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores.
#Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.

num_total=int(input("Infome o numero total de eleitores: "))
votos=[]
for c in range(0,num_total):
    v=int(input("Deseja votar no candidato 1, 2 ou 3? "))
    votos.append(v)

print(f"O candidato 1 teve {votos.count(1)} Votos\nO candidato 2 teve {votos.count(2)} Votos\nO candidato 3 teve {votos.count(3)} Votos")
