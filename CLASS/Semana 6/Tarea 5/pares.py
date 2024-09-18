"""
=========================================
AYPR - Algorítmos y programación
Grupo 61
Programa: Pares
=========================================
Fecha: 17 de Septiembre de 2024
Autor: Diego Prado Pardo
=========================================
"""
def pares(a, b):
    if a % 2 != 0:
        a += 1

    if b % 2 != 0:
        b -= 1

    if a > b:
        return 0
    
    return (b - a) // 2 + 1

def main():
    valores = input("Ingrese los valores de a y b separados por comas: ")
    a, b = map(int, valores.split(','))
    resultado = pares(a, b)
    print(resultado)

main()
