# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 15:15:14 2025

@author: Diego Prado Pardo
"""

print("Multiplicacion con suma y resta")
print("Digite el primer numero:")
num1 = int(input())
print("Digite el segundo numero:")
num2 = int(input())

ans = 0

if num2 > 0:
    for val in range(num2):
        ans = ans + num1
elif num2 < 0:
    for val in range(-num2):
        ans = ans + num1
    ans = -ans
    
print(num1, "*", num2, "=", ans)
