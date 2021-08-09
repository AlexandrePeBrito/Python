#Em uma competição de ginástica, cada atleta recebe votos de sete jurados. A melhor e a pior
#nota são eliminadas. A sua nota fica sendo a média dos votos restantes. Você deve fazer um
#programa que receba o nome do ginasta e as notas dos sete jurados alcançadas pelo atleta em
#sua apresentação e depois informe a sua média, conforme a descrição acima informada (retirar o
#melhor e o pior salto e depois calcular a média com as notas restantes). As notas não são
#informados ordenadas. Um exemplo de saída do programa deve ser conforme o exemplo abaixo:
#61.Atleta: Aparecido Parente
#62.Nota: 9.9
#63.Nota: 7.5
#64.Nota: 9.5
#65.Nota: 8.5
#66.Nota: 9.0
#67.Nota: 8.5
#68.Nota: 9.7
#69.
#70.Resultado final:
#71.Atleta: Aparecido Parente
#72.Melhor nota: 9.9
#73.Pior nota: 7.5
#Média: 9,04

nome=input("Informe o nome do atleta: ")
apresentacao=[]

for c in range(0,7):
    nota=float(input(f"Informe a Nota de {nome}: "))
    apresentacao.append(nota)

for c in range(0,7):
    print(f"Nota {c+1}: {apresentacao[c]}")

menor=min(apresentacao)
maior=max(apresentacao)
apresentacao.pop(apresentacao.index(menor))
apresentacao.pop(apresentacao.index(maior))
media=(sum(apresentacao)/5)

print(f"\nResultado Final:\nAtleta: {nome}\nMelhor Nota: {maior}\nMenor Nota: {menor}\nMedia: {media}")