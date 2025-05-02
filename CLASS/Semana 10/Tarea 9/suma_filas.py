"""
=========================================
AYPR - Algorítmos y programación
Grupo 61
Programa: Suma filas
=========================================
Fecha: 22 de Octubre de 2024
Autor: Diego Prado Pardo
=========================================
"""

def suma_filas(matriz):
    """ 
    Función para sumar los valores de cada fila de una matriz.
    (list de dos dimensiones) -> list de una dimensión
    """
    resultado = []
    
    for fila in matriz:
        suma_fila = sum(fila)
        resultado.append(suma_fila)
    
    return resultado

def main():
    m, n = map(int, input().split(','))
    matriz = []

    for _ in range(m):

        fila = list(map(int, input().split(',')))
        matriz.append(fila)

    suma_filas(matriz)
    resultado = suma_filas(matriz)
    print(",".join(map(str, resultado)))

main()