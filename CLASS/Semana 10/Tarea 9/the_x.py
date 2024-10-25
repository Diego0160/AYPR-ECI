"""
=========================================
AYPR - Algorítmos y programación
Grupo 61
Programa: La X
=========================================
Fecha: 22 de Octubre de 2024
Autor: Diego Prado Pardo
=========================================
"""
def main ():
    n = int(input())

    matriz =[[[' '] for i in range (n)] for i in range (n)]
    for i in range (n):
        matriz[i][i] = "X"  # type: ignore
        matriz[i][(n-1)-i] = "X" # type: ignore

    print(matriz)
main()
