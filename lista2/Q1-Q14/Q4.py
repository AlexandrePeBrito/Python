#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letters = input("Informe a letra(minuscula): ")

if((letters=="a")or(letters=="e")or(letters=="i")or(letters=="o")or(letters=="u")):
    print("Esta letra eh uma vogal")
else:
    print("Esta letra eh uma consoante")