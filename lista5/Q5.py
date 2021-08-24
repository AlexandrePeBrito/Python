#Faça um programa com uma função chamada somaImposto. A
#função possui dois parâmetros formais: taxaImposto, que
#é a quantia de imposto sobre vendas expressa em 
#porcentagem e custo, que é o custo de um item antes 
#do imposto. A função “altera” o valor de custo para
#incluir o imposto sobre vendas.
def somaImposto(taxaImposto, custo):
    taxaEmPorc=taxaImposto/100
    return custo*(taxaEmPorc+1)

valorProd=float(input("Informe o valor bruto do produto: "))
imposto=float(input("Informe o imposto em porcentagem: "))
valorFinal=somaImposto(imposto,valorProd)
print(f"O valor final do produto eh R${valorFinal}")