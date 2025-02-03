# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 11:16:03 2025

@author: Diego Prado Pardo
"""
# real nota1, nota2, nota3, defi
print("Programa que solicita al usuario tres definitivas y muestra la definitiva si aprovó")
print("Escriba su primera nota:")
nota1 = float(input())
print("Escriba su segunda nota:")
nota2 = float(input())
print("Escriba su tercera nota:")
nota3 = float(input())

defi = (nota1 * 0.30) + (nota2 * 0.30) + (nota3 * 0.40)

if defi >= 3.0:
    print("Usted aprobó con:", defi)
else:
    print("Usted reprobó")