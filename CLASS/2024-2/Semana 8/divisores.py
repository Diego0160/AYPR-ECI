"""
=========================================
AYPR - Algorítmos y programación
Grupo 61
Tema: Arreglos
=========================================
Fecha: 19 de Septiembre de 2024
Autor: Diego Prado Pardo
=========================================
"""
def divisores(n):
    """ Encuentra divisores de n, n>=2
    (int) -> bool"""
    a = 1
    while a <= n:
        if n % a == 0:
            print(a, end = ',')

        a += 1

    print(n)


def main():
    n = int(input())
    divisores(n)
    
main()