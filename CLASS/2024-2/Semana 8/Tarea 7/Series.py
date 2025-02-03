"""
=========================================
AYPR - Algorítmos y programación
Grupo 61
Programa: Series
=========================================
Fecha: 1 de Octubre de 2024
Autor: Diego Prado Pardo
=========================================
"""
# Corrección hecha
def imprime_s(num):
    """ Imprime serie daada
    (int) -> None
    """
    cont_1 = num
    cont_2 = 1

    while  cont_1 >= cont_2:

        print(str(cont_1) * cont_1)
        print(str(cont_2) * cont_2)

        cont_1 -= 1
        cont_2 += 1

    if num % 2 == 0:
        print(str(cont_1) * cont_1)


def main():
    num = int(input())
    imprime_s(num)
main()