"""
=========================================
AYPR - Algorítmos y programación
Grupo 61
Tema: Parejas
=========================================
Fecha: 29 de Octubre de 2024
Autor: Diego Prado Pardo
=========================================
"""
def generar_parejas(input):
    """Función que genera una lista de parejas conformadas por el menor y mayor valor de la secuencia.
    (str) -> list"""
    lista = list(map(int, input.split(',')))
    parejas = []

    while lista:
        menor = min(lista)
        mayor = max(lista)
        parejas.append([menor, mayor])
        lista.remove(menor)
        lista.remove(mayor)

    return parejas

def main():
    I = input()
    resultado = generar_parejas(I)
    print(resultado)

main()