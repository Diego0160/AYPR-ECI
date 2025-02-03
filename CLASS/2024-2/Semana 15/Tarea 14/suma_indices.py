"""
===========================================
AYPR - Algorítmos y programación
Grupo 61
Programa: Suma de índices
===========================================
Fecha: 26 de Noviembre de 2024
Autor: Diego Prado Pardo
===========================================
"""
def sum_indices(numeros, objetivo):
    """ Suma los índices de los elementos de la lista que sean mayores que el número objetivo.
    (list[int], int) -> int """
    total_sum = 0
    for i, num in enumerate(numeros):
        if num > objetivo:
            total_sum += i
    return total_sum

def main():
    numeros = list(map(int, input().split()))
    objetivo = int(input())
    ans = sum_indices(numeros, objetivo)
    print(ans)

main()