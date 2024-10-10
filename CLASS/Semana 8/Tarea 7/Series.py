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
def serie(n):
    """Genera la serie según el número ingresado.
    (int) -> None """
    numero_actual = n

    while numero_actual > 0:
        if numero_actual % 2 == 0:
            print(str(numero_actual) * numero_actual)
            print(str(numero_actual - 5))
        else:
            print(str(numero_actual) * numero_actual)
            print(str(numero_actual + 1) * (numero_actual + 1))
        numero_actual -= 3

def main():
    n = int(input("Introduce un número: "))
    serie(n)

main()