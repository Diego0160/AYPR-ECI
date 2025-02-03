"""
=========================================
AYPR - Algorítmos y programación
Grupo 61
Intento de Programa Series
=========================================
Fecha: 1 de Octubre de 2024
Autor: Diego Prado Pardo
=========================================
"""

# V1
"""
def serie(n):
    """"""Genera la serie según el número ingresado.
    (int) -> None """""""
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
"""

# V2
"""
def generate_sequence(n):
    """ """
    result = []

    result.append(str(n) * n)
    result.append('1')

    pepperon = 1

    while pepperon < n:
        if pepperon % 2 == 1:
            result.append(str(n - pepperon) * (n - pepperon))
        else:
            result.append(str(pepperon) * pepperon)
        pepperon += 1


    return '\n'.join(result)

def main():
    input_number = int(input('Enter a number: '))

    output_sequence = generate_sequence(input_number)


    print('Output:\n' + output_sequence)

main()
"""