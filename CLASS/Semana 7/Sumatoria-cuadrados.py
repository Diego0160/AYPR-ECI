"""
=========================================
AYPR - Algorítmos y programación
Grupo 61
Ejercicio: Sumatoria de Cuadrados
=========================================
Fecha: 26 de Septiembre de 2024
Autor: Diego Prado Pardo
=========================================
"""
def main():
    n = int(input('Digite un valor entero: '))
    
    if n > 0:
        num = 0

        while n > 0:
            num += n ** 2
            n -= 1

        print(num)
    else:
        print('El numero no es mayor a cero.')
    
main()