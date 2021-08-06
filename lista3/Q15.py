#série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa
#capaz de gerar a série até o n−ésimo termo.

n=int(input("Informe o N-esimo termo que deseja ver da serie Fibonacci: "))
atual=1
prox=0
ant=1

print(atual)
for c in range(0,n):
    prox=atual+ant
    ant=atual
    atual=prox
    print(atual)

