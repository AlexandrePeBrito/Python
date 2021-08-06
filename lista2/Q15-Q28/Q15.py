#Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os 
#valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: 
#equilátero, isósceles ou escaleno.
#o Dicas:
#o Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o 
#terceiro;
#o Triângulo Equilátero: três lados iguais;
#o Triângulo Isósceles: quaisquer dois lados iguais;
#o Triângulo Escaleno: três lados diferentes;

a = float(input("Informe o tamanho do lado A:"))
b = float(input("Informe o tamanho do lado B:"))
c = float(input("Informe o tamanho do lado C:"))

if(a < (b+c) and b < (a+c) and c < (a+b)):
    if(a!=b!=c):
        print("\nCom base nos valores, Esta figura eh um TRIANGULO ESCALENO")
    elif(a==b==c):
        print("\nCom base nos valores, Esta figura eh um TRIANGULO EQUILATERO")
    elif((a==b!=c)or(a==c!=b)or(b==c!=a)):
        print("\nCom base nos valores, Esta figura eh um TRIANGULO ISOCELES")
else:
    print("\nIsto nao eh um TRIANGULO")