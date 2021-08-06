#Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
#. "Telefonou para a vítima?"
#a. "Esteve no local do crime?"
#b. "Mora perto da vítima?"
#c. "Devia para a vítima?"
#d. "Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a 
#participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões 
#ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como 
#"Assassino". Caso contrário, ele será classificado como "Inocente".
print("Responda apenas com S ou N\n")
ans1 = input("Telefonou para a vitima?")
ans2 = input("Esteve no local do crime?")
ans3 = input("Sabe aonde a vitima mora?")
ans4 = input("Tinha algum problema com a vitima?")
ans5 = input("Frequentava o mesmo lugar que a vitima?")
c=0
if(ans1 =="s"or ans1 =="S"):
    c=c+1
if(ans2 =="s"or ans2 =="S"):
    c=c+1
if(ans3 =="s"or ans3 =="S"):
    c=c+1
if(ans4 =="s"or ans4 =="S"):
    c=c+1
if(ans5 =="s"or ans5 =="S"):
    c=c+1

if(c==5):
    print("\nVoce eh o Assassino")
elif(c>=3 and c<=4):
    print("\nVoce eh Cumplice")
elif(c==2):
    print("\nVoce eh Suspeito")
else:
    print("\nVoce eh Inocente")
