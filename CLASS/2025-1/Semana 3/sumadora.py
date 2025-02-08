# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 09:23:54 2025

@author: Diego Prado Pardo
"""

print("Programa que solicita al usuario dos números y presenta el resultado de su suma")
print("Ingrese el primer número:")
num1 = float(input())
    
print("Ingrese el segundo número:")
num2 = float(input())

suma = num1 + num2
print("La suma de", num1, "y", num2, "es de: ", suma)

print("¿Desea realizar otra suma? (responda con si o no):")
ans = input()


while ans == 'si' or ans == 'SI' or ans == 'Si':
    print("Ingrese el primer número:")
    num1 = float(input())
    
    print("Ingrese el segundo número:")
    num2 = float(input())
    
    suma = num1 + num2
    print("La suma de", num1, "y", num2, "es de: ", suma)

    print("¿Desea realizar otra suma? (responda con si o no):")
    ans = input()

print("Adios")