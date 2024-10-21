"""
=========================================
AYPR - Algorítmos y programación
Grupo 61
Contest 2
Programa: Prime numbers
=========================================
Autor: Diego Prado Pardo
=========================================
"""
def es_primo(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def main():
    a = int(input())
    b = int(input())

    primos = []
    n = a
    while n <= b:
        if es_primo(n):
            primos.append(n)
        n += 1

    if primos:
        print(",".join(map(str, primos)))
    else:
        print("No hay numeros primos en el rango dado")

main()