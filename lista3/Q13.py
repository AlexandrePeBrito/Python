#Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro
#número elevado ao segundo número. Não utilize a função de potência da linguagem.

base = int(input("Informe a Base: "))
expoente = int(input("Informe a Expoente: "))
base1=base
if(expoente==1):
    print(base)
else:
    for c in range(1,expoente):
        base1=base1*base
        print(base1)


print(f"O resultado de {base} elevado a {expoente} eh {base1}")
print(f"{base}^{expoente} = {base1}")