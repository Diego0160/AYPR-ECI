# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 10:12:03 2025

@author: Diego Prado Pardo
"""

print("Programa que simula ser un juego de adivinanzas numérico")

from random import randint as ri

num_secreto = ri(1, 100)
num = 0
intentos = 0

print("¡Bienvenido al juego de adivinanza!")
print("Estoy pensando en un número entre 1 y 100")
print("¿Podrás adivinarlo?")
print()

while num != num_secreto:
    print("Ingresa tu número:")
    num = int(input())
    intentos += 1
    
    if num < num_secreto:
        print("El número secreto es mayor que", num)
    elif num > num_secreto:
        print("El número secreto es menor que", num)

print("Felicitaciones, has adivinado el número en ", intentos, "intentos")

if intentos <= 5:
    print("Eres muy bueno en esto")
elif intentos <= 10:
    print("Eres un buen adivinador")
else:
    print("Necesitas más práctica, prueba más suerte la proxima vez")