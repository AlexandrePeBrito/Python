#Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de 
#centenas, dezenas e unidades do mesmo.
#o Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
#o 326 = 3 centenas, 2 dezenas e 6 unidades
#o 12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 
#111, 25, 20, 10, 21, 11, 1, 7 e 16

numb = int(input("Informe um numero(menor que 1000): "))
n = str(numb)
if(numb<1000):
    if(n[0]==0):
        if(n[1]==0):
            if(n[2]==1):
                print(" %.0f = %s unidade"%(numb,n[2]))
            else:
                print(" %.0f = %s unidades"%(numb,n[2]))
        else:
            if(n[1]==1):
                if(n[2]==1):
                    print(" %.0f = %s dezena e %s unidade"%(numb,n[1],n[2]))
                else:
                    print(" %.0f = %s dezena e %s unidades"%(numb,n[1],n[2]))
            else:
                if(n[2]==1):
                    print(" %.0f = %s dezenas e %s unidade"%(numb,n[1],n[2]))
                else:
                    print(" %.0f = %s dezenas e %s unidades"%(numb,n[1],n[2]))
    else:
        if(n[0]==1):
            if(n[1]==1):
                if(n[2]==1):
                    print(" %.0f = %s centena, %s dezena e %s unidade"%(numb,n[0],n[1],n[2]))
                else:
                    print(" %.0f = %s centena, %s dezena e %s unidades"%(numb,n[0],n[1],n[2]))
            else:
                if(n[2]==1):
                    print(" %.0f = %s centena, %s dezenas e %s unidade"%(numb,n[0],n[1],n[2]))
                else:
                    print(" %.0f = %s centena, %s dezenas e %s unidades"%(numb,n[0],n[1],n[2]))
        else:
            if(n[1]==1):
                if(n[2]==1):
                    print(" %.0f = %s centenas, %s dezena e %s unidade"%(numb,n[0],n[1],n[2]))
                else:
                    print(" %.0f = %s centenas, %s dezena e %s unidades"%(numb,n[0],n[1],n[2]))
            else:
                if(n[2]==1):
                    print(" %.0f = %s centenas, %s dezenas e %s unidade"%(numb,n[0],n[1],n[2]))
                else:
                    print(" %.0f = %s centenas, %s dezenas e %s unidades"%(numb,n[0],n[1],n[2]))
else:
    print("Numero invalido")