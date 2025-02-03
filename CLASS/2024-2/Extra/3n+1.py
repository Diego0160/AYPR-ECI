"""
=========================================
AYPR - Algorítmos y programación
Grupo 61
Programa: 3n+1
=========================================
Fecha: 
Autor: koko tactil
=========================================
"""
from sys import stdin

def cycle_length(n):
    length = 1
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        length += 1
    return length

def max_cycle_length(i, j):
    max_length = 0
    for number in range(min(i, j), max(i, j) + 1):
        current_length = cycle_length(number)
        if current_length > max_length:
            max_length = current_length
    return max_length

def main():
    input = stdin.read().strip().split()
    
    it = iter(input)
    results = []
    
    for i, j in zip(it, it):
        i, j = int(i), int(j)
        max_length = max_cycle_length(i, j)
        results.append(f"{i} {j} {max_length}")
    
    print("\n".join(results))
main()