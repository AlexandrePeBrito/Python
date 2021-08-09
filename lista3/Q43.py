#O cardápio de uma lanchonete é o seguinte:
#o Especificação Código Preço
#o Cachorro Quente 100 R$ 1,20
#o Bauru Simples 101 R$ 1,30
#o Bauru com ovo 102 R$ 1,50
#o Hambúrguer 103 R$ 1,20
#o Cheeseburguer 104 R$ 1,30
#o Refrigerante 105 R$ 1,00
#Faça um programa que leia o código dos itens pedidos e as quantidades desejadas.
#Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do
#pedido. Considere que o cliente deve informar quando o pedido deve ser encerrado.

cardapio={100:1.2,101:1.3,102:1.5,103:1.2,104:1.3,105:1}
cesta=0

print(cardapio)
pedido=int(input("Informe qual item deseja comprar: "))
qnt=int(input("Informe quantos deste item deseja comprar: "))

cesta=(cardapio[pedido]*qnt)+cesta
resp=int(input("Deseja inserir mais algum produto? 1-Sim 2 -Nao "))

while(resp==1):
    print(f"\n\n{cardapio}")
    pedido=int(input("Informe qual item deseja comprar: "))
    qnt=int(input("Informe quantos deste item deseja comprar: "))
    cesta=(cardapio[pedido]*qnt)+cesta
    resp=int(input("Deseja inserir mais algum produto? 1-Sim 2 -Nao "))

print(f"\nO valor total da compra eh R${cesta}")