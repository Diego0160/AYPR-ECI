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
# 
def serie(n):
    """ Genera la serie según el número ingresado.
    (int) -> None """
    numero_actual = n
    while numero_actual >= 1:
        if numero_actual % 2 == 0:  # Si es par
            print(str(numero_actual) * numero_actual)  # Imprime n veces el número
        else:  # Si es impar
            for i in range(n, 0, -1):  # Itera desde n hasta 1
                if i % 2 != 0:  # Si i es impar
                    print(str(i) * i)  # Imprime i veces el número i 
                    break  # Sale del bucle interno después de imprimir
        numero_actual -= 1

def main():
    n = int(input())
    serie(n)

main()