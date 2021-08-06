#Faça um programa que leia e valide as seguintes informações:
#a. Nome: maior que 3 caracteres;
#b. Idade: entre 0 e 150;
#c. Salário: maior que zero;
#d. Sexo: 'f' ou 'm';
#e. Estado Civil: 's', 'c', 'v', 'd';

nome = input("Infome seu nome: ")
idade = int(input("Informe sua idade: "))
salario = float(input("Informe seu salario: "))
sexo = input("Infome o seu Genero (M para MASCULINO e F para FEMININO):")
estado_civil =  input("Informe seu estado Civil (S para Solteiro(a), C para Casado(a), V para viuvo(a), D para Divorciado(a)): ")
rep=1

while(rep==1):
    if(len(nome)<=3): 
        print("Nome Invalido") 
        nome = input("Infome seu nome: ")
        rep=1
    else: rep=0
    if(idade<=0 or idade>=150):
        print("Idade Invalida")
        idade = int(input("Informe sua idade: "))
        rep=1
    else: rep=0
    if(salario<=0):
        print("Salario Invalido")
        salario = float(input("Informe seu salario: "))
        rep=1
    else: rep=0
    if(sexo!="M"):
        if(sexo!="F"):
            print("Genero Invalido")
            sexo = input("Infome o seu Genero (M para MASCULINO e F para FEMININO):")
            rep=1
        else: rep=0
    else: rep=0
    if(estado_civil!='S'):
        if(estado_civil!='C'):
            if(estado_civil!='V'):
                if(estado_civil!='D'):
                    print("Estado civil Invalido")
                    estado_civil =  input("Informe seu estado Civil (S para Solteiro(a), C para Casado(a), V para viuvo(a), D para Divorciado(a)): ")
                    rep=1
                else: rep=0
            else: rep=0
        else: rep=0
    else: rep=0
print("Inserido com Sucesso!")
print(f"Nome: {nome}\nIdade: {idade}\nSalario: {salario}\nSexo: {sexo}\nEstado Civil: {estado_civil}")

