# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 14:50:13 2025

@author: Diego Prado Pardo
"""
print("Programa Factorial")
print("Ingrese el número a sacar factorial:")
num= int(input())
count = num
factorial = 1

while count > 0:
    factorial = factorial * count
    count = count - 1
    
print("El numero factorial de", num, "es:", factorial)