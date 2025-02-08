# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 11:17:58 2025

@author: Diego Prado Pardo
"""

print("Programa que realiza una encuesta de tiempo de asignación de lockers")

tiempos = 0
count = 0
estudiante = 1

while estudiante < 5:
    print("Ingrese el tiempo en minutos que se demoró el estudiante",estudiante)
    tiempo = float(input())
    
    if tiempo > 40:
        tiempos = tiempos + tiempo
        count = count + 1
    
    estudiante = estudiante + 1

if count > 0:
    promedio = tiempos / count
    print("El promedio de los estudiantes que tardaron más de 40 minutos es de: ",promedio," minutos")
else:
    print("Ningún estudiante tardó más de 40 minutos")