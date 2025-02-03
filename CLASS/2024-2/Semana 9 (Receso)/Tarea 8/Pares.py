"""
=========================================
AYPR - Algorítmos y programación
Grupo 61
Programa: Pares
=========================================
Fecha: 10 de Octubre de 2024
Autor: Diego Prado Pardo
=========================================
"""
def pares(a, b):
    """ Genera la secuencia de pares en el intervalo cerrado [a,b]. a <= b
    (int, int) -> list """
    pares = []
    for num in range(a, b + 1):
        if num % 2 == 0:
            pares.append(num)
    return pares

def main():
    entrada = input()
    a, b = map(int, entrada.split(','))
    pares(a, b)
    resultado = pares(a, b)
    if resultado:
        print(",".join(map(str, resultado)))
    else:
        print("Vacía")

main()