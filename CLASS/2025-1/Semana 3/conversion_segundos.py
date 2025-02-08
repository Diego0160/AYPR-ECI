# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 11:17:58 2025

@author: Diego Prado Pardo
"""

print("Programa que convierte segundos a días, horas, minutos y segundos")
print("Número de segundos:")
num = int(input())

dias = num // 86400
s_restante = num % 86400

horas = s_restante // 3600
s_restante = s_restante % 3600

minutos = s_restante // 60
segundos = s_restante % 60

# Mostramos el resultado
print("Equivale a ",dias," dias, ",horas, "horas, ",minutos," minutos y ",segundos," segundos")
