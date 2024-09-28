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
    """ Verifica si el numero es par o impar por medio de booleanos
    (int) -> bool """
    par = n % 2
    if par == 0:
        return True
    else: 
        return False

def main():
    n = int(input('Digite un valor entero positivo: '))
    n_centinela = 0
    par = 0
    impar = 0
    suma_par = 0
    suma_impar = 0

    try: 
        while n != n_centinela:
            if es_par(n):
                par += 1
                suma_par += n
            else:
                impar += 1
                suma_impar += n

            n = int(input('Digite otro valor: '))
        print(f'Los valores en total que fueron pares son {par} y su suma es {suma_par}')
        print(f'Los valores en total que fueron impares son {impar} y su suma es {suma_impar}')
    except :
        print('Valor incorrecto, intente nuevamente.')

main()