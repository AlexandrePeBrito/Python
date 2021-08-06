#Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e
#limitando o fatorial a números inteiros positivos e menores que 16.


num = int(input("Infome o numero para verificar o fatorial: "))
resp=1

if(num>0 and num<16):
    while(resp==1):
        aux=num-1
        fatorial=num
        while(aux>0):
            fatorial=fatorial*aux
            aux-=1 
        print(f"{num}! = {fatorial}")
        resp = int(input("Deseja inserir outro valor?(1->SIM 2->NAO): "))
        if(resp==1):
            num = int(input("\nInfome o numero para verificar o fatorial: "))
        else:
            print("\n\nPrograma finalizado!\n")
