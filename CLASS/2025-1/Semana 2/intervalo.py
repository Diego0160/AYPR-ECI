# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 11:55:13 2025

@author: Diego Prado Pardo
"""

# real a, b, c
print("Programa que solicita valores para a, b y c y dice si a pertenece al intervalo  ( b , c ]")
print("Escriba el valor de a:")
a = float(input())
print("Escriba el valor de b:")
b = float(input())
print("Escriba el valor de c:")
c = float(input())

if b < a <= c:
    print(a," pertenece al intervalo (",b,", ",c,"]")
else:
    print(a," no pertenece al intervalo (",b,", ",c,"]")