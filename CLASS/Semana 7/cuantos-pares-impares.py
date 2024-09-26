"""
=========================================
AYPR - Algorítmos y programación
Grupo 61
Ejercicio: Cuantos pares e impares
=========================================
Fecha: 26 de Septiembre de 2024
Autor: Diego Prado Pardo
=========================================
"""
def es_par(n):
    """ 
     """
    par = n % 2
    if par == 0:
        return True
    else: 
        return False

def main():
    n = int(input('Digite un valor entero positivo: '))
    es_par(n)
    
    while n > 0:
        n = int(input('Digite otro valor: '))
        es_par(n)
        a = 0
        b = 0
        while es_par == True:
            a += 1
        else:
            b += 1

        suma = a + b
        print(f'Los valores en total que fueron pares son {a}')
        print(f'Los valores en total que fueron impares son {b}')
        print(f'Los valores en total digitados fueron {suma}')

    else:
        print('El numero no es mayor a cero.')

main()