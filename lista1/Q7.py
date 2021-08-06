#Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área 
#para o usuário.

side = float(input("Informe o tamanho do lado do quadrado: "))

area = pow(side,2)
dbarea = area * 2

print("A area do quadrado eh %.1f e o dobro desta area eh %.1f"%(area,dbarea))