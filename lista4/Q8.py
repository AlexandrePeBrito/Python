#Faça um Programa que peça a idade e a altura de 5 
#pessoas, armazene cada informação no seu respectivo 
#vetor. Imprima a idade e a altura na ordem inversa a
#ordem lida.
vetorI=[]
vetorA=[]
for c in range(0,5):
    vetorI.append(int(input("Informe a sua Idade: ")))
    vetorA.append(float(input("Informe a sua Altura: ")))
print(vetorI)
print(vetorA)
vetorI.reverse()
vetorA.reverse()
print(vetorI)
print(vetorA)