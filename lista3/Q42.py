#Faça um programa que leia uma quantidade indeterminada de números positivos e conte
#quantos deles estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. A entrada de
#dados deverá terminar quando for lido um número negativo.

num=int(input("Informe um numero: "))
numeros=[]
cl1=0
cl2=0
cl3=0
cl4=0
#clas[0]=[0-25]
#clas[1]=[26-50]
#clas[2]=[51-75]
#clas[3]=[76-100]

while(num>=0):
    numeros.append(num)
    num=int(input("\nInforme um numero: "))

for c in range(0,len(numeros)):
    if(numeros[c]>=0 and numeros[c]<=25):
        cl1+=1
    elif(numeros[c]>=26 and numeros[c]<=50):
        cl2+=1
    elif(numeros[c]>=51 and numeros[c]<=75):
        cl3+=1
    elif(numeros[c]>=76 and numeros[c]<=100):
        cl4+=1
    
print(f"\nDentre os numeros digitados tem {cl1} numeros entre [0-25], {cl2} numeros entre [26-50], {cl3} numeros entre [51-75], {cl4} numeros entre [76-100]")
