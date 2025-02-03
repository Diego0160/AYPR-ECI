"""
=========================================
AYPR - Algorítmos y programación
Grupo 61
Programa: Ecuación cuadrática
=========================================
Fecha: 17 de Septiembre de 2024
Autor: Diego Prado Pardo
=========================================
"""
import math

def e_cuadratica(a, b, c):
    """ Dado tres coeficientes de una ecuación cuadrática, calcula sus raíces.
    (float, float, float) -> str
    """
    discriminante = b**2 - 4*a*c
    
    if discriminante > 0:
        x1 = (-b + math.sqrt(discriminante)) / (2*a)
        x2 = (-b - math.sqrt(discriminante)) / (2*a)
        return (round(x1, 1), round(x2, 1))
    
    elif discriminante == 0:
        x = -b / (2*a)
        return (round(x, 1),)
    
    else:
        return "No tiene solución real"

def main():
    valores = input("Ingrese los valores de a, b y c separados por comas: ")
    a, b, c = map(float, valores.split(','))
    resultado = e_cuadratica(a, b, c)
    print(resultado)

main()
