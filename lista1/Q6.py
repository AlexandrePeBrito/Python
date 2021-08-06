#Faça um Programa que peça o raio de um círculo, calcule e mostre sua área

import math

radius = float(input("Informe o radio do circulo: "))

area = 3.14 * pow(radius,2)
print("O tamanho da area do circulo eh %.2f" %area)