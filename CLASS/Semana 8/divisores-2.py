"""
=========================================
AYPR - Algorítmos y programación
Grupo 61
Tema: Arreglos
=========================================
Fecha: 19 de Septiembre de 2024
Autor: Diego Prado Pardo
=========================================
"""
def divisores(n):
    """ Encuentra divisores de n, n>=2
    (int) -> list"""
    divi = []
    a = 1
    while a <= n:
        if n % a == 0:
            divi.append(a)
            
        a += 1

    return divi

def main():
    n = int(input())
    numeros = divisores(n)
    a = 0
    while a < len(numeros):
        print(numeros[a]) #Acceso indexado
        a += 1
    print('longitud del arreglo', len(numeros))
    numeros[0] = 0
    ultima = len(numeros)
    numeros[ultima-1] = 0
    a = 0
    while a < len(numeros):
        print(numeros[a]) #Acceso indexado
        a += 1

main()
