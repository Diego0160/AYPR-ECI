"""
=========================================
AYPR - Algorítmos y programación
Grupo 61
Correcion Parcial Segundo Tercio
=========================================
Fecha: 24 de Octubre de 2024
Autor: Diego Prado Pardo
=========================================
"""
def cuadratica(a, b, c, d, m):
    cont = 0
    for i in range(0, m+1):
        x = a* i**2 + b*i + c
        if x % d == 0:
            cont += 1
    return cont

def main():
    v = input()
    a, b, c, d, m = map(int, v.split(' '))

    while d != 0 and m!= 0:
        f = cuadratica(a, b, c, d, m)
        print(f)
        v = input()
        a, b, c, d, m = map(int, v.split(' '))

main()