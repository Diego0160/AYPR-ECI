# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 12:43:52 2025

@author: Diego Prado Pardo
"""

print("Ingresa el número de vacas en la finca: ")
num = int(input())
total_litros = 0
mayor = 0

while num < 0:
    print("Numero fuera de rango")
    print("Ingresa el número de vacas en la finca: ")
    num = int(input())
    
for val in range(num):
    print("Ingresa los litros producidos por la vaca", val+1)
    litros = float(input())
    
    total_litros = total_litros + litros
    
    if litros > mayor:
        mayor = litros

 
if num > 0:
    promedio = total_litros / num
else:
    promedio = 0


print("El Promedio de producción de la finca es de:", promedio," litros")
print("La vaca más productiva dio:", mayor, " litros")
