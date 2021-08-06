nome= input("AKI: ")
rep=1
while(rep==1):
    if(nome!="M"):
        if(nome!="F"):
            print("Diferente")
            nome = input("LA: ")
            rep=1
        else: rep=0
    else: rep=0

print("igual")