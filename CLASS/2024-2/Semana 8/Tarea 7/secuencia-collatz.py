"""
=========================================
AYPR - Algorítmos y programación
Grupo 61
Programa: Secuencia de Collatz
=========================================
Fecha: 1 de Octubre de 2024
Autor: Diego Prado Pardo
=========================================
"""
def collatz(n):
    while n != 1:
        print(n, end=", ")
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
    print(n)

def main():
    numero = int(input(""))
    if numero > 0:
        collatz(numero)
    else:
        print("Inténtalo nuevamente.")
        print("Ingresa un número entero positivo.")
        return main()

main()