#Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou 
# VVespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou 
#"Valor Inválido!", conforme o caso

shift = input("Informe o Turno que voce estuda M-matutino ou V-Vespertino ou N- Noturno: ")

if(shift=="M" or shift=="m"):
    print("Tenha um BOM DIA!")
elif(shift=="V" or shift=="v"):
    print("Tenha uma BOA TARDE!")
elif(shift=="N" or shift=="n"):
    print("Tenha uma BOA NOITE!")