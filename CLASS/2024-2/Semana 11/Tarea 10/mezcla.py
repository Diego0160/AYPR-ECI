"""
=========================================
AYPR - Algorítmos y programación
Grupo 61
Tema:  Mezcla
=========================================
Fecha: 29 de Octubre de 2024
Autor: Diego Prado Pardo
=========================================
"""
def mezclar_secuencia(input, n):
    """Función que divide la secuencia en n partes, invierte cada parte y luego las combina.
    (str, int) -> list"""
    lista = list(map(int, input.split(',')))
    l_parte = len(lista) // n
    l_invert = []

    for i in range(n):
        parte = lista[i * l_parte:(i + 1) * l_parte]
        l_invert.extend(reversed(parte))

    return l_invert

def main():
    i = input()
    n = int(input())
    resultado = mezclar_secuencia(i, n)
    print(resultado)

main()