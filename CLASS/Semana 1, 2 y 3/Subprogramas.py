"""
=========================================
AYPR - Algorítmos y programación
Grupo 61
Test: Subprogramas
=========================================
Fecha: 29 de Agosto de 2024
Autor: Diego Prado Pardo
=========================================
"""
from math import pi

def leer_dato():
    '''
    LEE UN VALOR NUMERICO INGRESADO POR TECLADO
    () -> float
    '''
    valor = float(input('Digite valor numerico: '))
    return valor

def area_circulo(radio):
    ''' 
    CALCULA EL ÁREA DE UN CÍRCULO TAMAÑO RADIO
    (float) -> float
    '''
    area = pi * radio ** 2
    return area

def area_cuadro(lado):
    '''
    CALCULA ÁREA DE UN CUADRADO DE LONGITUD LADO
    (float) -> float 
    '''
    return lado * lado
def main(): #Función Principal
    lado_grande = leer_dato()
    lado_pequeño = leer_dato()
    radio_pequeño = leer_dato()
    radio_grande = lado_grande/2
    a_diags = area_cuadro (lado_grande) - area_circulo(radio_grande)
    print(a_diags)
    a_sombra = area_circulo (radio_grande) - area_circulo (radio_pequeño)
    a_puntos = area_circulo (radio_pequeño) - area_cuadro (lado_pequeño)
    escribir = (a_diags, a_sombra, a_puntos, area_cuadro(lado_pequeño))
main()