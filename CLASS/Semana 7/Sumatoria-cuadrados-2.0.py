"""
=========================================
AYPR - Algorítmos y programación
Grupo 61
Ejercicio: Sumatoria de Cuadrados con dos
           funciones
=========================================
Fecha: 26 de Septiembre de 2024
Autor: Diego Prado Pardo
=========================================
"""
def sumatoria(n):
    num = 0

    while n > 0:
        num += n ** 2
        n -= 1
    return num

def main():
    n = int(input('Digite un valor entero: '))
    sumatoria(n)
    if n > 0:
        A = sumatoria(n)
        print(A)
    else:
        print('El numero no es mayor a cero.')
    
main()