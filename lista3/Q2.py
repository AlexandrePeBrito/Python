#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao
#nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

nome = input("Informe o nome de Usuario: ")
senha = input("Informe a senha: ")

while(nome==senha):
    print('ERROR! Senha igual ao usuario! Coloque uma senha diferente')
    senha = input("Informe a senha: ")

print("Usuario cadastrado com Sucesso!")