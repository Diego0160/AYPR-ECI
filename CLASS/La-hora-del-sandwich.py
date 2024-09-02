"""
=========================================
AYPR - Algorítmos y programación
Grupo 61
Programa: La hora del sándwich
=========================================
Fecha: 21 de Agosto de 2024
Autor: Diego Prado Pardo
=========================================
"""
hora_actual = input('Ingrese la hora actual: ')
hora_inicial = input('Ingrese la hora inicial: ')
hora_final = input('Ingrese la hora final: ')
hh, mm = hora_actual.split(':')
hh, mm = hora_inicial.split(':')
hh, mm = hora_final.split(':')
if hora_actual >= hora_inicial and hora_actual <= hora_final:
    print('Es hora del sandwich')
else:
    print('No es hora del sandwich')