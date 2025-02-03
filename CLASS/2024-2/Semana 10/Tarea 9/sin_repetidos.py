"""
=========================================
AYPR - Algorítmos y programación
Grupo 61
Programa: Sin Repetidos
=========================================
Fecha: 22 de Octubre de 2024
Autor: Diego Prado Pardo
=========================================
"""
def sin_repetidos(arr):
    """ Función para eliminar repeticiones en una lista
    (list) -> list"""

    if len(arr) == 0:
        return []
    
    resultado = [arr[0]]
    
    for i in range(1, len(arr)):
        if arr[i] != arr[i-1]:
            resultado.append(arr[i])
    
    return resultado

def main():
    entrada = input().split()
    entrada = [int(x) for x in entrada]

    sin_repetidos(entrada)
    salida = sin_repetidos(entrada)
    
    print(" ".join(map(str, salida)))

main()