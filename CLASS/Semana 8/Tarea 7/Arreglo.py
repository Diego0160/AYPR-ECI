"""
=========================================
AYPR - Algorítmos y programación
Grupo 61
Programa: Crear Arreglo
=========================================
Fecha: 1 de Octubre de 2024
Autor: Diego Prado Pardo
=========================================
"""
#
def arreglo(n):
    """ Crea un arreglo con n elementos dados por el usuario.
    (int) -> list """
    arreglo = []
    contador = 0
    while contador < n:
        elemento = input().strip()
        
        if elemento:
            try:
                arreglo.append(int(elemento))
            except ValueError:
                arreglo.append(elemento)
            contador += 1
        else:
            print("Entrada vacía, por favor ingresa un valor.")
    return arreglo

def main():
    n = int(input())
    arreglo(n)
    r = arreglo(n)
    print(r)

main()
