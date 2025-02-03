# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 11:55:13 2025

@author: Diego Prado Pardo
"""

# entero m, b50, b20, b10
print("Programa que solicita el monto a retirar en un cajero, y dice si puede o no entregar dicho monto")
print("Ingrese el monto a retirar:")

m = int(input())

if m % 10000 == 0:
    b50 = m // 50000
    residuo = m % 50000

    b20 = residuo // 20000
    residuo %= 20000

    b10 = residuo // 10000

    print("El cajero le entregará:")
    print(b50,"billetes de $50.000")
    print(b20,"billetes de $20.000")
    print(b10,"billetes de $10.000")
else:
    print("El monto no puede ser entregado")
