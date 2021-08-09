#Em uma competição de salto em distância cada atleta tem direito a cinco saltos. No final da série
#de saltos de cada atleta, o melhor e o pior resultados são eliminados. O seu resultado fica sendo
#a média dos três valores restantes. Você deve fazer um programa que receba o nome e as cinco
#distâncias alcançadas pelo atleta em seus saltos e depois informe a média dos saltos conforme a
#descrição acima informada (retirar o melhor e o pior salto e depois calcular a média). Faça uso
#de uma lista para armazenar os saltos. Os saltos são informados na ordem da execução,
#portanto não são ordenados. O programa deve ser encerrado quando não for informado o nome
#do atleta. A saída do programa deve ser conforme o exemplo abaixo:
#47.Atleta: Rodrigo Curvêllo
#48.
#49.Primeiro Salto: 6.5 m
#50.Segundo Salto: 6.1 m
#51.Terceiro Salto: 6.2 m
#52.Quarto Salto: 5.4 m
#53.Quinto Salto: 5.3 m
#54.
#55.Melhor salto: 6.5 m
#56.Pior salto: 5.3 m
#57.Média dos demais saltos: 5.9 m
#58.
#59.Resultado final:
#Rodrigo Curvêllo: 5.9 m

nome=input("Informe o nome do atleta: ")
saltos=[]

for c in range(0,5):
    altura=float(input(f"Informe a altura do salto do {nome}: "))
    saltos.append(altura)

print(f"Primeiro Salto: {saltos[0]} M\n\
Segundo Salto: {saltos[1]} M\n\
Terceiro Salto: {saltos[2]} M\n\
Quarto Salto: {saltos[3]} M\n\
Quinto Salto: {saltos[4]} M\n")

menor=min(saltos)
maior=max(saltos)
saltos.pop(saltos.index(menor))
saltos.pop(saltos.index(maior))
media=(sum(saltos)/3)
print(f"Melhor Salto: {maior} M\n\
Menor Salto: {menor} M\n\
Media dos demais Saltos: {media} M\n\n\
Resultado Final:\n{nome}: {media} M")
