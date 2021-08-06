#Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor
#seja inválido e continue pedindo até que o usuário informe um valor válido.

nota =int(input("Informe a nota do usuario: "))

while(nota<0 or nota>10):
    print("Valor Invalido!")
    nota =int(input("Informe a nota do usuario: "))

print("A nota do usuario foi %d"%nota)