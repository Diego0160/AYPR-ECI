# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 09:56:25 2025

@author: Diego Prado Pardo
"""

print("Programa que simula ser una caja registradora")

total = 0
ans = 'si'

while ans == 'si':
    print("Escriba el valor del artículo:")
    val = float(input())
    
    print("Escriba la cantidad de artículos:")
    cant = int(input())
    
    subtotal = val * cant
    total = total + subtotal
    
    print("Subtotal de los productos: $", subtotal)
    
    print("¿Desea agregar otro artículo? (s/n):")
    ans = input()

print("Total de la factura: $", total)
print()
print("¡Gracias por su compra!")