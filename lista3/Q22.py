#Altere o programa de cálculo dos números primos, informando, caso o número não seja primo,
#por quais número ele é divisível.

num = int(input("Informe um numero:"))
d=[]
c=0
if(num>0):
    for i in range(1,num+1):
        if(num%i==0):
            c+=1
            d.append(i)
    if(c>2):
        print(f"\nO numero {num} não eh um numero primo")
        print(f"Ele eh divisivel pelos numeros {d}")
    elif(c==2):
        print(f"O numero {num} eh um numero primo\n")

