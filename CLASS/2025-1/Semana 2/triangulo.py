# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 11:55:13 2025

@author: Diego Prado Pardo
"""

# real a, b, c
print("Programa que solicita las dimensiónes de los lados de un triangulo y dice si es un triangulo Equilátero, Isósceles o Escaleno")
print("Escriba la longitud del primer lado:")
l1 = float(input())
print("Escriba la longitud del segundo lado:")
l2 = float(input())
print("Escriba la longitud del tercer lado:")
l3 = float(input())

if l1 == l2 == l3:
    print("El triángulo con dimensiones",l1,",",l2,"y",l3," es Equilátero.")
elif l1 == l2 or l1 == l3 or l2 == l3:
    print("El triángulo con dimensiones",l1,",",l2,"y",l3," es Isósceles.")
else:
    print("El triángulo con dimensiones",l1,",",l2,"y",l3," es Escaleno.")