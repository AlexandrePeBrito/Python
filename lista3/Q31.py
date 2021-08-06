#O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui
#uma loja de conveniências. Faça um programa que implemente uma caixa registradora
#rudimentar. O programa deverá receber um número desconhecido de valores referentes aos
#preços das mercadorias. Um valor zero deve ser informado pelo operador para indicar o final da
#compra. O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o
#cliente forneceu, para então calcular e mostrar o valor do troco. Após esta operação, o programa
#deverá voltar ao ponto inicial, para registrar a próxima compra. A saída deve ser conforme o
#exemplo abaixo:
# Lojas Tabajara
#o Produto 1: R$ 2.20
#o Produto 2: R$ 5.80
#o Produto 3: R$ 0
#o Total: R$ 9.00
#o Dinheiro: R$ 20.00
# Troco: R$ 11.00
# ...

cesta=[]
valor_prod=float(input("Informe o valor do produto: "))
resp=1

while(resp==1):
    cesta.append(valor_prod)
    resp=int(input("Deseja inserir outro produto?(1->SIM 2->NAO): "))
    if(resp==1): valor_prod=float(input("Informe o valor do produto: "))

total=sum(cesta)
dinheiro=float(input(f"O valor total das suas compras deu R${total} reais\nInforme o valor para o pagamento: "))
troco=dinheiro-total

if(troco<0): print("Esta faltando dinheiro!")
elif(troco==0): print("Esta pago!")
elif(troco>0): print(f"Aqui esta R${troco} de troco.")