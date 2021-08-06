#Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F 
#- Feminino, M - Masculino, Sexo Inválido.

sex = input("Informe o seu genero, M para masculino e F para feminino: ")

if((sex=='M') or (sex=='m')):
    print("M - Masculino")
elif((sex=='F') or (sex=='f')):
    print("F - Feminino")
else:
    print("Sexo invalido")