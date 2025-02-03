"""
===========================================
AYPR - Algorítmos y programación
Grupo 61
Programa: Rotacion
===========================================
Fecha: 26 de Noviembre de 2024
Autor: Diego Prado Pardo
===========================================
"""
def lista_rotada(numeros, n):
    """ Rota una lista de números enteros n veces
    (list, int) -> list """
    n = n % len(numeros)
    
    numeros_rotados = numeros[-n:] + numeros[:-n]
    
    return numeros_rotados

def main():
    numeros = input().split(',')
    
    n = int(input())
    
    numeros_rotados = lista_rotada(numeros, n)
    print(",".join(map(str, numeros_rotados)))
main()