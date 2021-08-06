#A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... Faça um programa
#que gere a série até que o valor seja maior que 500.

atual=1
prox=0
ant=1
c=0
print(atual)
while(atual<=500):
    c+=1
    prox=atual+ant
    ant=atual
    atual=prox
    print(atual)

print(f"O Termo {c} desta serie tem valor de {atual}.")